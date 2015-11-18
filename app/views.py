from flask import Flask, render_template, Response, send_file,\
    flash, redirect, request, session, send_from_directory, make_response, abort

from app import app
import web_load_policy 
from .forms import PolicyForm, SelectPolForm
from .inputforms import InputPolicyForm
from .model import Quote
from time import strftime
import json
import urllib2
import requests
#import json_delta


	
@app.route('/')
@app.route('/index')
def index():

    return render_template("index.html")

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/select_pol', methods=['GET', 'POST'])
def select_pol():
    form = SelectPolForm()
    if form.validate_on_submit():
        session['polnum'] = (str(form.selPolicyNumber.data)).zfill(9)
        return redirect('/policy')
    
    return render_template("select_pol.html",
                           title='Policy Selection',
                           form=form)	
						   

@app.route('/policy', methods=['GET', 'POST'])
def policy():
	
	polnum = session['polnum']
	url = 'http://dctestappsrv1:8081/direct/policy?policyNumber=%s&everything=true&discounts=true&coverages=true&vehicles=true&nonDescribedVehicle=true&applicant=true&drivers=true&namedInsureds=true&additionalListedInsureds=true' % polnum
	response = urllib2.urlopen(url).read()
	pol_json = json.loads(response)
	session['policy'] = pol_json
	form = PolicyForm.from_json(pol_json)
		
	if form.validate_on_submit():
		return redirect('/index')
		
	return render_template('policy.html', 
                           title='Policy Form',
                           form=form)
						   
	
@app.route('/load')
def load():
    policies = web_load_policy.ReadPolJSON('test', 'load_policy.json')
    run = strftime("%Y-%m-%d %H:%M:%S")
    #run = 'sssss'

    #print('failureCode = %s' % policies['failureCodes'])
    if 'defaultMessage' in policies[0]:
        return render_template("loaderror.html",
                           title="Whoa! We can't do that.",
                           errors=policies)
    else:
        return render_template("loadsuccess.html",
                           title='Test Policies',
                           run=run,
                           policies=policies)

@app.route('/upload_file')
def upload_file():

    return render_template("upload.html")


@app.route('/import', methods= ['POST'])
def import_objects():
        file = request.files['file']
        app.logger.debug('uploading file ' + file.filename)
        if file and allowed_file(file.filename):
            #extract content
            content = file.read()
            policies = web_load_policy.LoadPolJSON('test', content)
            run = strftime("%Y-%m-%d %H:%M:%S")

            if 'defaultMessage' in policies[0]:
                return render_template("loaderror.html",
                                   title="Whoa! We can't do that.",
                                   errors=policies)
            else:
                return render_template("loadsuccess.html",
                                   title='Test Policies',
                                   run=run,
                                   policies=policies)
            '''
            print content

            jsonResponse = json.dumps({'file_content':content})
            print jsonResponse
            response = Response(jsonResponse,  mimetype='application/json')
            return response
            '''
        else:
             abort(make_response("File extension not acceptable", 400))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route("/load_policy.json")
def getFile():
    file_name = 'load_policy.json'
    return send_file(file_name, as_attachment=True)
    '''
    headers = {"Content-Disposition": "attachment; filename=%s" % file_name}
    with open(file_name, 'r') as f:
        body = f.read()
    return make_response((body, headers))
    '''
