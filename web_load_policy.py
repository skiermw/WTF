#!/usr/bin/env python
#   web_load_policy.py
#
import sys
import json
from pprint import pprint
import urllib2
import urllib
import requests
from collections import defaultdict

def ReadPolJSON(env, filename):
    global policies_dict 
    policies_dict = []

    server = GetEnv(env)

    pol_json = []
    
    with open(filename) as pol_file:
        pol_json = json.load(pol_file)
        for policy in pol_json['policies']:
            policies_dict.append(CreateQuote(server, policy))
    
    return policies_dict

def LoadPolJSON(env, input_json):
    global policies_dict
    policies_dict = []

    server = GetEnv(env)
    print input_json
    pol_json = []
    #pol_json = input_json
    pol_json = json.loads(input_json)
    #pol_json = json.dumps(input_json)
    print pol_json
    for policy in pol_json['policies']:
        policies_dict.append(CreateQuote(server, policy))

    return policies_dict
def GetEnv(env):
    if env == "devl":
        server = "dcdevappsrv1"

    elif env == "demo":
        server = "dcdemoappsrv1"

    elif env == "test":
        server = "dctestappsrv1"

    else:
        server = 'UNKNOWN'

    return server


def CreateQuote(server, pol_json):
    
    # Set environment
    #environ = 'demo'
    # Address, Applicant,
    #  Create the quote with policy json body

    url = 'http://%s:8083/direct/quote' % server
    response = requests.post(url, data=json.dumps(pol_json))
    if response.status_code != 200:
        print('quote status: %s' % response.status_code)
        print('              %s' % response.text)
        #return response.text
        response_json = json.loads(response.text)
        for failure in response_json[0]['failureCodes']:
                    #print(failure)
                    return failure

    quote_auth_token = response.headers['quoteauthtoken']
    quote_json = json.loads(response.text)
    #print(quote_json)
    #print(' ')

    #print(quote_json)
    quote_stream_id = quote_json['streamId']
    #print(quote_stream_id)
    quote_stream_rev = quote_json['streamRevision']

    #print ('Stream ID: %s ' % quote_stream_id)
    #print ('Stream Rev: %s' % quote_stream_rev)
    #print ('Auth Token: %s' % quote_auth_token)

    # remove all vehicles
    veh_coll = []
    for veh in quote_json['events'][0]['quote']['vehicles']:
        veh_coll.append( veh['id'])
    url = 'http://%s:8083/direct/quote/%s/%s/vehicles' % (server, quote_stream_id, quote_stream_rev)
    payload = {'ids': json.dumps(veh_coll)}
    headers = {'quoteAuthToken': quote_auth_token}
    response = requests.delete(url, params=payload, headers=headers)
    response_json = json.loads(response.text)
    #print(response_json)
    #print('vehicle delete response:')
    quote_stream_rev = response_json['streamRevision']
    #print('vehicle delete response:')
    #print(response.text)
    if response.status_code != 200:
        print('vehicle delete response: %s' % response.status_code)
        print('              %s' % response.text)
        for failure in response_json[0]['failureCodes']:
                    #print(failure)
                    return failure

    #######################################################
    # add a wait to allow current state db to catch up
    #time.sleep(2)
    #######################################################

    # add vehicles from input json back on
    #  create json for coverages
    coverage_input = {}
    vehicles = []
    coverages = []
    for vehicle in pol_json['vehicles']:
        #print('@@@@@@@@@@ Vehicle')
        vehicle_body = {}
        veh = {}
        veh['year'] = vehicle['year']
        veh['make'] = vehicle['make']
        veh['model'] = vehicle['model']
        veh['trim'] = vehicle['trim']
        veh['vin'] = vehicle['vin']

        #print('vin = %s' % veh['vin'])

        veh['lengthOfOwnership'] = vehicle['lengthOfOwnership']
        veh['ownership'] = vehicle['ownership']
        veh['businessUse'] = vehicle['businessUse']
        if 'antiTheftDevice' in vehicle:
            veh['antiTheftDevice'] = vehicle['antiTheftDevice']
        #  write vehicle
        url = 'http://%s:8083/direct/quote/%s/%s/vehicle' % (server, quote_stream_id, quote_stream_rev)
        payload = json.dumps(veh)
        headers = {'quoteAuthToken': quote_auth_token}
        response = requests.post(url, data=payload, headers=headers)
        response_json = json.loads(response.text)

        #print(quote_stream_rev)
        if response.status_code != 200:
            print('Add vehicle status: %s' % response.status_code)
            print(response_json)
            for failure in response_json[0]['failureCodes']:
                    #print(failure)
                    return failure
        quote_stream_rev = response_json['streamRevision']
        # read the response to get new vehicle id
        #response_json = json.loads(response.text)
        vehicle_body['id'] = response_json['events'][0]['vehicle']['id']
        if 'financeCompany' in vehicle:
            #print('finance company')
            fin_co_input = {}
            fin_co_input['name'] = vehicle['financeCompany']['name']
            fin_co_input['loanNumber'] = vehicle['financeCompany']['loanNumber']
            fin_co_input['address'] = {}
            fin_co_input['address']['street'] = vehicle['financeCompany']['address']['street']
            fin_co_input['address']['street2'] = vehicle['financeCompany']['address']['street2']
            fin_co_input['address']['city'] = vehicle['financeCompany']['address']['city']
            fin_co_input['address']['state'] = vehicle['financeCompany']['address']['state']
            fin_co_input['address']['zip'] = vehicle['financeCompany']['address']['zip']

            #write finance company
            url = 'http://%s:8083/direct/quote/%s/%s/vehicle/%s/financeCompany' % (server, quote_stream_id, quote_stream_rev, vehicle_body['id'])
            payload = json.dumps(fin_co_input)
            headers = {'quoteAuthToken': quote_auth_token}
            response = requests.post(url, data=payload, headers=headers)
            response_json = json.loads(response.text)
            if response.status_code == 200:
                quote_stream_rev = response_json['streamRevision']
                #print(response_json)

            if response.status_code != 200:
                print('Add finance co status: %s' % response.status_code)
                print('response.text:   %s' % response.text)
                print('response_json: %s' % response_json[0]['failureCodes'][0])
                for failure in response_json[0]['failureCodes']:
                    #print(failure)
                    return failure
            #print(response.text)

        coverages = []
        for coverage in vehicle['coverages']:
            coverage_body = {}
            limits = []
            if coverage['type'] == 'RoadsideAssistance':
                continue
            else:
                for limit in coverage['limits']:
                    limit_body = {}
                    limit_body['type'] = limit['type']
                    limit_body['value'] = limit['value']
                    limits.append(limit_body)

            coverage_body['type'] = coverage['type']
            coverage_body['limits'] = limits
            coverages.append(coverage_body)

        vehicle_body['coverages'] = coverages
        #print('vehicle body')
        #print(vehicle_body)
        vehicles.append(vehicle_body)


    coverage_input['vehicles'] = vehicles
    #print('coverage_input = %s' % coverage_input)
    url = 'http://%s:8083/direct/quote/%s/%s/coverages' % (server, quote_stream_id, quote_stream_rev)
    payload = json.dumps(coverage_input)
    headers = {'quoteAuthToken': quote_auth_token}
    response = requests.put(url, data=payload, headers=headers)
    if response.status_code != 200:
        print('Update Coverages status: %s' % response.status_code)
        print(response.text)
        for failure in response_json[0]['failureCodes']:
                    #print(failure)
                    return failure

    response_json = json.loads(response.text)
    if response.status_code == 200:
        quote_stream_rev = response_json['streamRevision']

    else:
        print(' ')
        print(response.url)
        print(response.text)
        for failure in response_json[0]['failureCodes']:
                    #print(failure)
                    return failure


    #print(response.url)

    #print ('Stream Rev: %s' % quote_stream_rev)

    ########################################################################################
    ##### delete all drivers
    drivers_coll = []
    applicant_id = quote_json['events'][0]['quote']['applicant']['id']
    for driver in quote_json['events'][0]['quote']['drivers']:
        #  Special processing for driver that is also applicant (can't delete that driver)
        if driver['id'] == applicant_id:
            continue
        else:
            drivers_coll.append( driver['id'])
    url = 'http://%s:8083/direct/quote/%s/%s/drivers' % (server, quote_stream_id, quote_stream_rev)
    payload = {'ids': json.dumps(drivers_coll)}
    headers = {'quoteAuthToken': quote_auth_token}
    response = requests.delete(url, params=payload, headers=headers)
    response_json = json.loads(response.text)
    quote_stream_rev = response_json['streamRevision']
    #quote_stream_rev =  quote_stream_rev + 1
    #print('Delete driver response:')
    #print(response.text)
    if response.status_code != 200:
        print('driver delete response: %s' % response.status_code)
        print(response_json)
        for failure in response_json[0]['failureCodes']:
                    #print(failure)
                    return failure

    # add drivers from input json back on
    #  create json for coverages

    drivers = []
    driver_ct = 0
    for driver in pol_json['drivers']:
        #print('@@@@@@@@@@ Driver: %s' % driver['firstName'])
        driver_body = {}
        driver_body['firstName'] = driver['firstName']
        driver_body['middleName'] = driver['middleName']
        driver_body['lastName'] = driver['lastName']
        driver_body['birthDate'] = driver['birthDate']
        driver_body['email'] = driver['email']
        driver_body['phoneNumber'] = driver['phoneNumber']
        driver_body['gender'] = driver['gender']
        driver_body['ssn'] = driver['ssn']
        driver_body['maritalStatus'] = driver['maritalStatus']
        driver_body['licenseNumber'] = driver['licenseNumber']
        driver_body['licenseState'] = driver['licenseState']

        #  write driver

        payload = json.dumps(driver_body)
        headers = {'quoteAuthToken': quote_auth_token}
        # assuming first driver is the applicant (which can't be deleted) so update with needed info
        #   all other drivers will be deleted from quote then re-added from json
        if driver_ct == 0:
            #print('driver put')
            url = 'http://%s:8083/direct/quote/%s/%s/driver/%s' % (server, quote_stream_id, quote_stream_rev, applicant_id)
            response = requests.put(url, data=payload, headers=headers)
            #print('Update Driver Quote stream ID: %s' % quote_stream_id)
            if response.status_code != 200:
                print('Update driver status: %s' % response.status_code)
                for failure in response_json[0]['failureCodes']:
                    #print(failure)
                    return failure
            #print(response.text)
            response_json = json.loads(response.text)
            quote_stream_rev = response_json['streamRevision']
        else:
            #print('driver post')
            url = 'http://%s:8083/direct/quote/%s/%s/driver' % (server, quote_stream_id, quote_stream_rev)
            response = requests.post(url, data=payload, headers=headers)
            #print('Add Driver Quote stream ID: %s' % quote_stream_id)
            if response.status_code != 200:
                print('Add driver status: %s' % response.status_code)
                for failure in response_json[0]['failureCodes']:
                    #print(failure)
                    return failure
            response_json = json.loads(response.text)
            #print('Add Driver: %s' % response_json)
            quote_stream_rev = response_json['streamRevision']

        driver_ct = driver_ct + 1

    ### get Clue and MVR
    url = 'http://%s:8083/direct/quote/%s/%s/drivingRecord' % (server, quote_stream_id, quote_stream_rev)
    headers = {'quoteAuthToken': quote_auth_token}
    data = urllib.urlencode(pol_json)
    response = requests.post(url, data=payload, headers=headers)
    #print('MVR Quote stream ID: %s' % quote_stream_id)
    if response.status_code != 200:
        print("Clue/MVR: %s" % response.status_code)
        for failure in response_json[0]['failureCodes']:
                    #print(failure)
                    return failure
    #print(response.url)
    response_json = json.loads(response.text)
    #print('MVR: %s' % response_json)
    quote_stream_rev = response_json['streamRevision']

    #####  Start Purchase processing  ######

    ### Set Payment Plan
    payment_plan = {"paymentPlan":'F6'}
    url = 'http://%s:8083/direct/quote/%s/%s' % (server, quote_stream_id, quote_stream_rev)
    headers = {'quoteAuthToken': quote_auth_token}
    data = json.dumps(payment_plan)
    #print('Payment Plan Quote stream ID: %s' % quote_stream_id)
    response = requests.patch(url, data=data, headers=headers)
    response_json = json.loads(response.text)
    if response.status_code != 200:
        print("Payment Plan: %s" % response.status_code)
        print('url'+url)
        print('auth_token ' + quote_auth_token)
        print('data: %s' % data)
        print('response_json: %s' % response_json)
        for failure in response_json[0]['failureCodes']:
                    #print(failure)
                    return failure
    #print(response.url)

    quote_stream_rev = response_json['streamRevision']

    ### Rate this puppy
    rating_channel = {"ratingChannel":"PublicWebsite"}
    url = 'http://%s:8083/direct/quote/%s/%s/rate' % (server, quote_stream_id, quote_stream_rev)
    headers = {'quoteAuthToken': quote_auth_token}
    data = json.dumps(rating_channel)
    response = requests.post(url, data=data, headers=headers)
    quote_stream_rev =  quote_stream_rev + 1
    #print(response.text)
    if response.status_code != 200:
        print("Rate: %s" % response.status_code)
        for failure in response_json[0]['failureCodes']:
                    #print(failure)
                    return failure
    response_json = json.loads(response.text)
    if response.status_code == '200':
        quote_stream_rev = response_json['streamRevision']

    ### Answer Speed Racer question
    speed_racer = {"isASpeedRacer":'false'}
    url = 'http://%s:8083/direct/quote/%s/%s' % (server, quote_stream_id, quote_stream_rev)
    headers = {'quoteAuthToken': quote_auth_token}
    data = json.dumps(speed_racer)
    response = requests.patch(url, data=data, headers=headers)
    response_json = json.loads(response.text)
    #print(response.text)
    if response.status_code != 200:
        print("Speed Racer: %s" % response.status_code)
        for failure in response_json[0]['failureCodes']:
                    #print(failure)
                    return failure
    #print(response.url)
    quote_stream_rev = response_json['streamRevision']

    ### Generate Policy Number
    url = 'http://%s:8083/direct/quote/%s/%s/policyNumber' % (server, quote_stream_id, quote_stream_rev)
    headers = {'quoteAuthToken': quote_auth_token}
    response = requests.post(url, headers=headers)
    response_json = json.loads(response.text)
    #print(response.text)
    if response.status_code != 200:
        print("Policy Number: %s" % response.status_code)
        for failure in response_json[0]['failureCodes']:
                    #print(failure)
                    return failure
    #print(response.url)CreateQuote(pol_json)
    quote_stream_rev = response_json['streamRevision']
    policy_number = response_json['events'][0]['policyNumber']
    ### Purchase
    body = {}
    body['quoteId'] = quote_stream_id
    body['ipAddress'] = '10.8.30.145'
    body['expectedStreamRevision'] = quote_stream_rev
    body['channelOfOrigin'] = 'PublicWebsite'
    data = urllib.urlencode(body)
    #print(data)
    url = 'http://%s:8083/direct/policy?%s' % (server, data)
    headers = {'quoteAuthToken': quote_auth_token}
    response = requests.post(url, headers=headers)
    #print(response.text)
    if response.status_code != 200:
        print("Purchase: %s" % response.status_code)
        print("           %s " % response.text)
        for failure in response_json[0]['failureCodes']:
                    #print(failure)
                    return failure
    #print(response.url)
    response_json = json.loads(response.text)
    policy_stream_id = response_json['streamId']
    policy_stream_rev = response_json['streamRevision']

    policy_return = {}
    policy_return['policy_desc'] = pol_json['testPolicyDescription']
    policy_return['policy_number'] = policy_number
    policy_return['policy_stream_ID'] = response_json['streamId']
    policy_return['policy_eff_date'] = response_json['timestamp']
    #print('policy_return %s' % policy_return)
    return policy_return


def main():
   

   x_policies_dict = []
   x_policies_dict = ReadPolJSON('devl', 'load_policy.json')

   for policies in x_policies_dict:
        print(policies)
   #return policies_dict
   
   
   

      
# Start program
if __name__ == "__main__":
   main()

