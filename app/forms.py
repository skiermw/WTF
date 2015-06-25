from flask.ext.wtf import Form
from wtforms.fields import BooleanField, StringField, TextField, FloatField, FormField, IntegerField, DateField, SubmitField, FieldList, DecimalField
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
	middleName = TextField('Middle Name')
	lastName = TextField('Last Name', validators=[InputRequired()])
	birthDate = DateField('Birth Date', validators=[InputRequired()])
	age = IntegerField('Age', validators=[InputRequired()])
	id = StringField('ID')
	
class Reason(Form):
	code = TextField('Code')
	Description = StringField('Description')
	id = StringField('ID')
	
class CreditReport(Form):
	id = TextField('Id')
	reasons = FieldList(FormField(Reason))
	referenceNumber = TextField('Reference Number')
	score = IntegerField('Score')
	status = TextField('Status')
	
class Discount(Form):
	id = TextField('Id')
	type = TextField('Type')
	
class Violation(Form):
	id = TextField('Id')
	code = TextField('Code')
	
class Driver(Form):
	age = IntegerField('Age', validators=[InputRequired()])
	birthDate = DateField('Birth Date', validators=[InputRequired()])
	creditReport = FormField(CreditReport)
	firstName = TextField('First Name', validators=[InputRequired()])
	lastName = TextField('Last Name', validators=[InputRequired()])
	gender = TextField('Gender')
	id = StringField('ID')
	licenseNumber = StringField('License Num')
	licenseState = StringField('License State')
	licenseStatus = StringField('License Status')
	maritalStatus = StringField('Marital Status')
	sequence = StringField('sequence')
	ssn = StringField('SSN')
	violationPoints = StringField('Violation Points')
	violations = FieldList(FormField(Violation, label='Violations'))
	
class NamedInsured(Form):
	age = IntegerField('Age', validators=[InputRequired()])
	birthDate = DateField('Birth Date', validators=[InputRequired()])
	firstName = TextField('First Name', validators=[InputRequired()])
	lastName = TextField('Last Name', validators=[InputRequired()])
	gender = TextField('Gender')
	id = StringField('ID')
	maritalStatus = StringField('Marital Status')
	ssn = StringField('SSN')
	
class Limit(Form):
	id = StringField('ID')
	type = StringField('Type')
	value = IntegerField('Value')
	
class Coverage(Form):
	type = StringField('Type')
	id = StringField('ID')
	limits = FieldList(FormField(Limit, label='Limits'))
	premium = DecimalField('Premium')
	
class Vehicle(Form):
	businessUse = StringField('Bus. Use')
	costSymbol = StringField('Cost Symbol')
	coverages = FieldList(FormField(Coverage, label='Coverages'))
	id = StringField('ID')
	make = StringField('Make')
	model = StringField('Model')
	ownership = StringField('Ownership')
	permissiveUserCoverages = FieldList(FormField(Coverage, label='Permissive User Coverages'))
	previouslyInsured = StringField('Prev Ins?')
	pseudoVin = StringField('Pseudo VIN')
	sequence = StringField('Sequence')
	trim = StringField('Trim')
	trimCode = StringField('Trim Code')
	vin = StringField('VIN')
	year = StringField('Year')
	
class NonDescribedVehicle(Form):
	coverages = FieldList(FormField(Coverage, label='Coverages'))
	id = StringField('ID')
	permissiveUserCoverages = FieldList(FormField(Coverage, label='Permissive User Coverages'))
		
class PolicyForm(Form):
	policyNumber = TextField('Policy Number')
	applicant = FormField(Applicant)
	address = FormField(Address)
	
	channelOfOrigin = TextField('Channel of Origin')
	clueReferenceNumbers = TextField('CLUE Reference')
	company = TextField('Company')
	compositeDriverRatingFactorWithPoints = FloatField('Comp. Rate. Fact w/ Points')
	compositeDriverRatingFactorWithoutPoints = FloatField('Comp. Rate. Fact w/o Points')
#   coverages	
	discounts = FieldList(FormField(Discount))
	drivers = FieldList(FormField(Driver))
	effectiveDate = StringField('Effective Date')
	evidenceOfPriorInsurance = StringField('Evidence of Prior Ins')
	expirationDate = StringField('Expiration Date')
	familyNumber = StringField('Family No')
	fcraNoticeRequired = StringField('FCRA Notice Req')
	firstPolicyEffectiveDate = StringField('First Pol Eff Date')
	forms = FieldList(StringField('Form Number'))
	id = StringField('Pol ID')
	lineOfBusiness = StringField('LOB')
	namedInsureds = FieldList(FormField(NamedInsured))
	vehicles = FieldList(FormField(Vehicle))
	nonDescribedVehicle = FormField(NonDescribedVehicle)
	policyNumber = StringField('Policy Num')
	revision = StringField('Revision')
	revisionTimestamp = StringField('Revison Timestamp')
	status = StringField('Status')
	term = IntegerField('Term')
	territory = StringField('Territory')
	totalDiscount = FloatField('Total Discount')
	totalPremium = FloatField('Total Premium')

class SelectPolForm(Form):
	selPolicyNumber = TextField('Policy Number to Select')
	

class Drivers(Form):
	drivers = FieldList(FormField(Driver))
	
class Vehicles(Form):
	vehicles = FieldList(FormField(Vehicle))

class CreateQuoteFromPolicy(Form):
	selPolicyNumber = TextField('Policy Number to Copy to Quote')

class QuoteForm(Form):
	applicant = FormField(Applicant)
	address = FormField(Address)
	channelOfOrigin = TextField('Channel of Origin')
	clueReferenceNumbers = TextField('CLUE Reference')
	company = TextField('Company')
	compositeDriverRatingFactorWithPoints = FloatField('Comp. Rate. Fact w/ Points')
	compositeDriverRatingFactorWithoutPoints = FloatField('Comp. Rate. Fact w/o Points')
    #coverages	FieldList(FormField(Coverage))
	discounts = FieldList(FormField(Discount))
	drivers = FieldList(FormField(Driver))
	effectiveDate = StringField('Effective Date')
	evidenceOfPriorInsurance = StringField('Evidence of Prior Ins')
	expirationDate = StringField('Expiration Date')
	familyNumber = StringField('Family No')
	fcraNoticeRequired = StringField('FCRA Notice Req')
	firstPolicyEffectiveDate = StringField('First Pol Eff Date')
	forms = FieldList(StringField('Form Number'))
	id = StringField('Pol ID')
	lineOfBusiness = StringField('LOB')
	namedInsureds = FieldList(FormField(NamedInsured))
	vehicles = FieldList(FormField(Vehicle))
	nonDescribedVehicle = FormField(NonDescribedVehicle)
	policyNumber = StringField('Policy Num')
	revision = StringField('Revision')
	revisionTimestamp = StringField('Revison Timestamp')
	status = StringField('Status')
	term = IntegerField('Term')
	territory = StringField('Territory')
	totalDiscount = FloatField('Total Discount')
	totalPremium = FloatField('Total Premium')
	
class EventsForm(Form):
	changeQuote = FormField(QuoteForm)
		
class ChangeQuote(Form):
	effectiveTimestamp = StringField('Effective Timestamp')
	events = FieldList(FormField(EventsForm))
	storeRevision = IntegerField('Store Revision')
	streamId = StringField('Stream ID')
	streamRevision = IntegerField('Stream Revision')
	timestamp = StringField('Timestamp')
	
class NewQuote(Form):
	firstName = StringField('First Name', validators=[InputRequired()])
	middleName = StringField('Middle Name')
	lastName = StringField('First Name', validators=[InputRequired()])
	suffix = StringField('Suffix')
	birthDate = DateField('Birth Date', validators=[InputRequired()], format='%m-%d-%Y')
	email = StringField('email', validators=[InputRequired()])
	phoneNumber = StringField('Phone', validators=[InputRequired()])
	street = TextField('Street', validators=[InputRequired()])
	street2 = TextField('Street2')
	city = TextField('City', validators=[InputRequired()])
	state = TextField('State', validators=[InputRequired()])
	zip = TextField('Zip', validators=[InputRequired()])
	