from flask import render_template, flash, redirect, request, session
from app import app
from .forms import PolicyForm, SelectPolForm, Drivers, Vehicles
#form .forms import SelectPolForm
#from .form_gen import Policy, InquiryDrivers, Vehicles

import json
import urllib2


	
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
	
	#if request.method == 'POST' and form.validate():
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