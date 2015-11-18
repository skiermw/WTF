from flask.ext.wtf import Form
from wtforms.fields import BooleanField, StringField, FloatField, FormField, IntegerField, DateField, SubmitField, FieldList, DecimalField
from wtforms.validators import DataRequired, InputRequired, AnyOf


class InputAddress(Form):
	street = StringField('Street', validators=[InputRequired()])
	street2 = StringField('Street2')
	city = StringField('City', validators=[InputRequired()])
	state = StringField('State', validators=[InputRequired()])
	zip = StringField('Zip', validators=[InputRequired()])

class InputApplicant(Form):
	firstName = StringField('First Name', validators=[InputRequired()])
	middleName = StringField('Middle Name')
	lastName = StringField('Last Name', validators=[InputRequired()])
	birthDate =StringField('Birth Date', validators=[InputRequired()])

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
	
class InputDiscount(Form):
	type = StringField('Type')
	
class InputViolation(Form):
	code = StringField('Code')
	
class InputDriver(Form):

	firstName = StringField('First Name', validators=[InputRequired()])
	lastName = StringField('Last Name', validators=[InputRequired()])
	middleName = StringField('Middle Name')
	gender = StringField('Gender')
	email = StringField('eMail')
	age = IntegerField('Age', validators=[InputRequired()])
	birthDate = StringField('Birth Date', validators=[InputRequired()])
	licenseNumber = StringField('License Num')
	licenseState = StringField('License State')
	licenseStatus = StringField('License Status')
	maritalStatus = StringField('Marital Status')
	phoneNumber = StringField('Phone Number')
	ssn = StringField('SSN')
	violationPoints = StringField('Violation Points')
	violations = FieldList(FormField(InputViolation, label='Violations'))
	
class InputNamedInsured(Form):
	firstName = StringField('First Name', validators=[InputRequired()])
	lastName = StringField('Last Name', validators=[InputRequired()])
	age = IntegerField('Age', validators=[InputRequired()])
	birthDate = StringField('Birth Date', validators=[InputRequired()])
	gender = StringField('Gender')
	#id = StringField('ID')
	maritalStatus = StringField('Marital Status')
	ssn = StringField('SSN')

class InputFinanceCompany(Form):
	name = StringField('Name')
	loanNumber = StringField('Loan Number')
	address = FormField(InputAddress, label='Address')

class InputLimit(Form):
	#id = StringField('ID')
	type = StringField('Type')
	value = IntegerField('Value')
	
class InputCoverage(Form):
	type = StringField('Type')
	#id = StringField('ID')
	limits = FieldList(FormField(InputLimit, label='Limits'))

	
class InputVehicle(Form):
	year = StringField('Year')
	make = StringField('Make')
	model = StringField('Model')
	trim = StringField('Trim')
	trimCode = StringField('Trim Code')
	businessUse = StringField('Bus. Use')
	#costSymbol = StringField('Cost Symbol')
	coverages = FieldList(FormField(InputCoverage, label='Coverages'))
	#id = StringField('ID')
	ownership = StringField('Ownership')
	#permissiveUserCoverages = FieldList(FormField(Coverage, label='Permissive User Coverages'))
	previouslyInsured = StringField('Prev Ins?')
	#pseudoVin = StringField('Pseudo VIN')
	#sequence = StringField('Sequence')
	vin = StringField('VIN')
	financeCompany = FormField(InputFinanceCompany, label='Finance Company')
	lengthOfOwnership = StringField('Length of Ownership', validators=[InputRequired(), AnyOf('ShorterThan90Days', message='ShorterThan90Days or')] )

class NonDescribedVehicle(Form):
	coverages = FieldList(FormField(InputCoverage, label='Coverages'))
	#id = StringField('ID')
	permissiveUserCoverages = FieldList(FormField(InputCoverage, label='Permissive User Coverages'))
		
class InputPolicyForm(Form):
	testPolicyDescription = StringField('Test Policy Description')
	applicant = FormField(InputApplicant)
	address = FormField(InputAddress)
	channelOfOrigin = StringField('Channel of Origin')
	#clueReferenceNumbers = StringField('CLUE Reference')
	#company = StringField('Company')
	#compositeDriverRatingFactorWithPoints = FloatField('Composite Rate. Fact w/ Points')
	#compositeDriverRatingFactorWithoutPoints = FloatField('Composite Rate. Fact w/o Points')
#   coverages	
	discounts = FieldList(FormField(InputDiscount))
	drivers = FieldList(FormField(InputDriver))
	effectiveDate = StringField('Effective Date')
	evidenceOfPriorInsurance = StringField('Evidence of Prior Ins')
	#expirationDate = StringField('Expiration Date')
	#familyNumber = StringField('Family No')
	fcraNoticeRequired = StringField('FCRA Notice Req')
	#firstPolicyEffectiveDate = StringField('First Pol Eff Date')
	#forms = FieldList(StringField('Form Number'))
	#id = StringField('Pol ID')
	#lineOfBusiness = StringField('LOB')
	#namedInsureds = FieldList(FormField(InputNamedInsured))
	vehicles = FieldList(FormField(InputVehicle))
	#nonDescribedVehicle = FormField(NonDescribedVehicle)
	#policyNumber = StringField('Policy Num')
	#revision = StringField('Revision')
	#revisionTimestamp = StringField('Revison Timestamp')
	#status = StringField('Status')
	term = IntegerField('Term')



class SelectPolForm(Form):
	selPolicyNumber = StringField('Policy Number to Select')
	

#class Drivers(Form):
	#drivers = FieldList(FormField(Driver))
	
#
# class Vehicles(Form):
	#vehicles = FieldList(FormField(Vehicle))

class CreateQuoteFromPolicy(Form):
	selPolicyNumber = StringField('Policy Number to Copy to Quote')

