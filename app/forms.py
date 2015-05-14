from flask.ext.wtf import Form
#from wtforms import Form
from wtforms.fields import BooleanField, TextField, FormField, IntegerField
from wtforms.validators import DataRequired, InputRequired


class Address(Form):
	Street = TextField('streeT', validators=[InputRequired()])
	number = IntegerField('number', validators=[InputRequired()])
	state = TextField('State', validators=[InputRequired()])


class PolicyForm(Form):
	name = TextField('name', validators=[DataRequired()])
	is_public = BooleanField('is_public', default=False)
	address = FormField(Address, label='address')

