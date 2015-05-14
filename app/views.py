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
		'name': 'Mark',
		'is_public': True,
		'address': {
			"state": "MO",
			"street": "Concord St",
			'number': '8100'
		}
	}
	
	form = PolicyForm.from_json(json)
	flash('data=%s' % str(form.data))
              
	print form.data
	return render_template('policy.html', 
                           title='Policy Form',
                           form=form)
						   
	
		