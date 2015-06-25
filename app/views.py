from flask import render_template, flash, redirect, request, session
from app import app
from .forms import NewQuote, PolicyForm, SelectPolForm, Drivers, Vehicles, CreateQuoteFromPolicy, ChangeQuote
from .model import Quote
import json
import urllib2
import requests


	
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Mark'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/select_pol', methods=['GET', 'POST'])
def select_pol():
    form = SelectPolForm()
    if form.validate_on_submit():
	
		#flash('pol selected =%s' % (str(form.selPolicyNumber.data)).zfill(9))
		session['polnum'] = (str(form.selPolicyNumber.data)).zfill(9)
		return redirect('/policy')
		
    return render_template("select_pol.html",
                           title='Policy Selection',
                           form=form)	
						   
@app.route('/copytoquote', methods=['GET', 'POST'])	
def copy_to_quote():
    form = CreateQuoteFromPolicy()
    if form.validate_on_submit():
		#flash('pol selected =%s' % (str(form.selPolicyNumber.data)).zfill(9))
		session['polnum'] = (str(form.selPolicyNumber.data)).zfill(9)
		return redirect('/changequote')
		
    return render_template("select_pol_copy_quote.html",
                           title='Copy Policy To Quote',
                           form=form)	
						   
@app.route('/newquote', methods=['GET', 'POST'])	
def new_quote():
	
	quote_obj = Quote()
	form = NewQuote(obj=quote_obj)
	#form.birthDate.data = 3-3-1988
	if form.validate_on_submit():
		payload = {}
		payload['applicant']= {}
		payload['address']={}
		payload['channelOfOrigin'] = 'PublicWebsite'
		payload['applicant']['firstName'] = form.firstName.data
		payload['applicant']['middleName'] = form.middleName.data
		payload['applicant']['lastName'] = form.lastName.data
		payload['applicant']['suffix'] = form.suffix.data
		payload['applicant']['birthDate'] = str(form.birthDate.data)
		payload['applicant']['email'] = form.email.data
		payload['applicant']['phoneNumber'] = form.phoneNumber.data
		payload['address']['street'] = form.street.data
		payload['address']['street2'] = form.street2.data
		payload['address']['city'] = form.city.data
		payload['address']['state'] = form.state.data
		payload['address']['zip'] = form.zip.data
		data = json.dumps(payload)
		url = 'http://dcdemoappsrv1:8081/direct/quote'
		headers={'content-type':'application/json'}
		response = requests.post(url, data, headers=headers)
		quote_json = response.json()
		session['quote'] = quote_json
		return redirect('/viewquote')
		#flash('session %s' % session['quote'])
		#return render_template("create_quote.html",
		#						title='Create Quote',
		#						form=form)			
		
	return render_template("create_quote.html",
                           title='Create Quote',
                           form=form)							   

@app.route('/viewquote', methods=['GET', 'POST'])
def view_quote():
	polnum = session['polnum']
	quote_json = session['quote']
	form = ChangeQuote.from_json(quote_json)
	return render_template('change_quote.html', 
                           title='View Quote',
                           form=form)
						   
@app.route('/changequote', methods=['GET', 'POST'])
def change_quote():
	polnum = session['polnum']
	url = 'http://dcdemoappsrv1:8081/direct/policy?policyNumber=%s&everything=true&discounts=true&coverages=true&vehicles=true&nonDescribedVehicle=true&applicant=true&drivers=true&namedInsureds=true&additionalListedInsureds=true' % polnum
	response = urllib2.urlopen(url).read()
	pol_json = json.loads(response)
	session['policy'] = pol_json
	
	polid = pol_json['id']
	streamrev = pol_json['revision']
	
	copy_to_quote_url = 'http://dcdemoappsrv1:8081/direct/policy/%s/%s/changeQuote' % (polid, streamrev)
	
	response = requests.post(copy_to_quote_url)
	quote_json = response.json()
	session['timestamp'] = quote_json['timestamp']
	session['quotenum'] = quote_json['events'][0]['changeQuote']['id']
	session['streamrev'] = quote_json['events'][0]['changeQuote']['revision']
	form = ChangeQuote.from_json(quote_json)
	
	
	if form.validate_on_submit():
		quotenum = session['quotenum']
		streamrev = str(session['streamrev'])
		rate_url = 'http://dcdemoappsrv1:8083/direct/changeQuote/%s/%s/rate' % (quotenum, streamrev)
		#rate_url = 'http://dcdemoappsrv1:8083/direct/changeQuote/d816f880829e4429b19a9b8c6b722485/1/rate' 
		response = requests.post(rate_url)
		rate_json = response.json()
		#session['ratejson'] = rate_json
		flash('rate_json=%s' % str(rate_json))
		return render_template('change_quote.html', 
                           title='Change Quote',
                           form=form)
		#return redirect('/changequote')
	#flash('rate_json=%s' % str(session['ratejson']))	
	flash('inital data=%s' % str(quote_json))
	return render_template('change_quote.html', 
                           title='Change Quote',
                           form=form)
	
@app.route('/policy', methods=['GET', 'POST'])
def policy():
	#url = 'http://dcdemoappsrv1:8081/direct/policy?policyNumber=000000005&everything=true&discounts=true&coverages=true&vehicles=true&nonDescribedVehicle=true&applicant=true&drivers=true&namedInsureds=true&additionalListedInsureds=true'
	#polnum = '000000005'
	polnum = session['polnum']
	url = 'http://dcdemoappsrv1:8081/direct/policy?policyNumber=%s&everything=true&discounts=true&coverages=true&vehicles=true&nonDescribedVehicle=true&applicant=true&drivers=true&namedInsureds=true&additionalListedInsureds=true' % polnum
	response = urllib2.urlopen(url).read()
	pol_json = json.loads(response)
	session['policy'] = pol_json
	form = PolicyForm.from_json(pol_json)
	#form = Policy.from_json(pol_json)
	
	if form.validate_on_submit():
		#flash('data=%s' % str(form.data))
		#flash('form pol no =%s' % str(form.policyNumber.data))
		return redirect('/index')
		
	#flash('inital data=%s' % str(form.data))
	return render_template('policy.html', 
                           title='Policy Form',
                           form=form)
						   
	
@app.route('/drivers', methods=['GET', 'POST'])
def drivers():
	pol_json = session['policy']
	form = Drivers.from_json(pol_json)
	
	return render_template("drivers.html",
                           title='Drivers',
                           form=form)		

@app.route('/vehicles', methods=['GET', 'POST'])						   
def vehicles():
	pol_json = session['policy']
	form = Vehicles.from_json(pol_json)
	
	return render_template("vehicles.html",
                           title='Vehicles',
                           form=form)		