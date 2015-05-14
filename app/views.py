from flask import render_template
from app import app
from .forms import EventForm
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
						   
@app.route('/event', methods=['GET', 'POST'])
def event():
	json = {
		'name': 'First Event',
		'location': {'name': 'some location'}
	}
	
	form = EventForm.from_json(json)
	
	return render_template('event.html', 
                           title='Event Form',
                           form=form)