from flask import render_template, flash, redirect
from app import app
from .forms import PolicyForm
#from flask.ext.wtf import Form
#from wtforms.fields import BooleanField, TextField

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
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
						   
@app.route('/policy', methods=['GET', 'POST'])
def policy():
	json = {
		"policyNumber": "000000003",
		"applicant": {
			"firstName": "KATHY",
			"lastName": "BOCKETT",
			"age": 58,
			"birthDate": "1956-09-10",
			"id": "e306e295bd1747b5b7422e85393cf7f0"
		},
		"address": {
			"city": "Skokie",
			"county": "Cook",
			"id": "216bdffd48ec4769a460c32f4330dfb4",
			"latitude": 42.0101,
			"longitude": -87.75354,
			"state": "IL",
			"street": "5014 Estes Ave",
			"zip": "60077-3520"
		}
	}
	
	form = PolicyForm.from_json(json)
	flash('data=%s' % str(form.data))
              
	print form.data
	return render_template('policy.html', 
                           title='Policy Form',
                           form=form)
						   
	
		