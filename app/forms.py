from flask.ext.wtf import Form
from wtforms.fields import BooleanField, StringField, StringField, FloatField, FormField, IntegerField, DateField, SubmitField, FieldList, DecimalField
from wtforms.validators import DataRequired, InputRequired


class Address(Form):
	street = StringField('Street', validators=[InputRequired()])
	street2 = StringField('Street2')
	city = StringField('City', validators=[InputRequired()])
	state = StringField('State', validators=[InputRequired()])
	zip = StringField('Zip', validators=[InputRequired()])
	county = StringField('County', validators=[InputRequired()])
	latitude = FloatField('Latitude')
	longitude = FloatField('Longitude')

	
class Applicant(Form):
	firstName = StringField('First Name', validators=[InputRequired()])
	middleName = StringField('Middle Name')
	lastName = StringField('Last Name', validators=[InputRequired()])
	birthDate = DateField('Birth Date', validators=[InputRequired()])
	age = IntegerField('Age', validators=[InputRequired()])
	#id = StringField('ID')
	
class Reason(Form):
	code = StringField('Code')
	Description = StringField('Description')
	#id = StringField('ID')
	
class CreditReport(Form):
	#id = StringField('Id')
	reasons = FieldList(FormField(Reason))
	referenceNumber = StringField('Reference Number')
	score = IntegerField('Score')
	status = StringField('Status')
	
class Discount(Form):
	#id = StringField('Id')
	type = StringField('Type')
	
class Violation(Form):
	#id = StringField('Id')
	code = StringField('Code')
	
class Driver(Form):
	firstName = StringField('First Name', validators=[InputRequired()])
	lastName = StringField('Last Name', validators=[InputRequired()])
	gender = StringField('Gender')
	#id = StringField('ID')
	age = IntegerField('Age', validators=[InputRequired()])
	birthDate = DateField('Birth Date', validators=[InputRequired()])
	#creditReport = FormField(CreditReport)
	licenseNumber = StringField('License Num')
	licenseState = StringField('License State')
	licenseStatus = StringField('License Status')
	maritalStatus = StringField('Marital Status')
	sequence = StringField('sequence')
	ssn = StringField('SSN')
	violationPoints = StringField('Violation Points')
	violations = FieldList(FormField(Violation, label='Violations'))
	
class NamedInsured(Form):
	firstName = StringField('First Name', validators=[InputRequired()])
	lastName = StringField('Last Name', validators=[InputRequired()])
	age = IntegerField('Age', validators=[InputRequired()])
	birthDate = DateField('Birth Date', validators=[InputRequired()])
	gender = StringField('Gender')
	#id = StringField('ID')
	maritalStatus = StringField('Marital Status')
	ssn = StringField('SSN')
	
class Limit(Form):
	#id = StringField('ID')
	type = StringField('Type')
	value = IntegerField('Value')
	
class Coverage(Form):
	type = StringField('Type')
	#id = StringField('ID')
	limits = FieldList(FormField(Limit, label='Limits'))
	premium = DecimalField('Premium')
	
class Vehicle(Form):
	year = StringField('Year')
	make = StringField('Make')
	model = StringField('Model')
	trim = StringField('Trim')
	trimCode = StringField('Trim Code')
	businessUse = StringField('Bus. Use')
	costSymbol = StringField('Cost Symbol')
	coverages = FieldList(FormField(Coverage, label='Coverages'))
	#id = StringField('ID')
	ownership = StringField('Ownership')
	permissiveUserCoverages = FieldList(FormField(Coverage, label='Permissive User Coverages'))
	previouslyInsured = StringField('Prev Ins?')
	pseudoVin = StringField('Pseudo VIN')
	sequence = StringField('Sequence')
	
	vin = StringField('VIN')
	
	
class NonDescribedVehicle(Form):
	coverages = FieldList(FormField(Coverage, label='Coverages'))
	#id = StringField('ID')
	permissiveUserCoverages = FieldList(FormField(Coverage, label='Permissive User Coverages'))
		
class PolicyForm(Form):
	policyNumber = StringField('Policy Number')
	applicant = FormField(Applicant)
	address = FormField(Address)
	
	channelOfOrigin = StringField('Channel of Origin')
	clueReferenceNumbers = StringField('CLUE Reference')
	company = StringField('Company')
	compositeDriverRatingFactorWithPoints = FloatField('Composite Rate. Fact w/ Points')
	compositeDriverRatingFactorWithoutPoints = FloatField('Composite Rate. Fact w/o Points')
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
	#id = StringField('Pol ID')
	lineOfBusiness = StringField('LOB')
	namedInsureds = FieldList(FormField(NamedInsured))
	vehicles = FieldList(FormField(Vehicle))
	nonDescribedVehicle = FormField(NonDescribedVehicle)
	#policyNumber = StringField('Policy Num')
	revision = StringField('Revision')
	revisionTimestamp = StringField('Revison Timestamp')
	status = StringField('Status')
	term = IntegerField('Term')
	territory = StringField('Territory')
	totalDiscount = FloatField('Total Discount')
	totalPremium = FloatField('Total Premium')

class SelectPolForm(Form):
	selPolicyNumber = StringField('Policy Number to Select')
	

class Drivers(Form):
	drivers = FieldList(FormField(Driver))
	
class Vehicles(Form):
	vehicles = FieldList(FormField(Vehicle))

class CreateQuoteFromPolicy(Form):
	selPolicyNumber = StringField('Policy Number to Copy to Quote')

class LoadForm(Form):
	testPolicyDescription = StringField('Test Policy Description')
	applicant = FormField(Applicant)
	address = FormField(Address)
	channelOfOrigin = StringField('Channel of Origin')
	clueReferenceNumbers = StringField('CLUE Reference')
	company = StringField('Company')

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
	#id = StringField('Pol ID')
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
	


class LoadTest(Form):
	policy_desc = StringField('Test Policy Description')
	policy_number = StringField('Policy Number')
	policy_stream_ID = StringField('Stream ID')
	policy_eff_date = StringField('Effective Date')
	