from flask.ext.wtf import Form
#from wtforms import Form
from wtforms.fields import BooleanField, StringField, TextField, FloatField, FormField, IntegerField, DateField
from wtforms.validators import DataRequired, InputRequired


class Address(Form):
	street = TextField('Street', validators=[InputRequired()])
	street2 = TextField('Street2')
	city = TextField('City', validators=[InputRequired()])
	state = TextField('State', validators=[InputRequired()])
	zip = TextField('Zip', validators=[InputRequired()])
	county = TextField('County', validators=[InputRequired()])
	latitude = FloatField('Latitude')
	longitude = FloatField('Longitude')
	id = StringField('ID')
	
class Applicant(Form):
	firstName = TextField('First Name', validators=[InputRequired()])
	lastName = TextField('Last Name', validators=[InputRequired()])
	birthDate = DateField('Birth Date', validators=[InputRequired()])
	age = IntegerField('Age', validators=[InputRequired()])
	id = StringField('ID')

class PolicyForm(Form):
	policyNumber = TextField('Policy Number')
	applicant = FormField(Applicant, label='Applicant')
	address = FormField(Address, label='Address')

