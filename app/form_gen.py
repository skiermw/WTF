# generated from swagger Policy model on 06/12/15 16:14:29 
 
from flask.ext.wtf import Form
from wtforms.fields import BooleanField, StringField, TextField, FloatField, FormField, IntegerField, DateField, SubmitField, FieldList
from wtforms.validators import DataRequired, InputRequired
 
class Policy(Form):
	applicant = FormField(InquiryApplicant)
	address = FormField(InquiryAddress)
	channelOfOrigin = StringField('channelOfOrigin')
	clueReferenceNumbers = FieldList(FormField(String))
	company = StringField('company')
	compositeDriverRatingFactorWithoutPoints = FloatField('compositeDriverRatingFactorWithoutPoints')
	compositeDriverRatingFactorWithPoints = FloatField('compositeDriverRatingFactorWithPoints')
	coverages = FieldList(FormField(InquiryCoverage))
	discounts = FieldList(FormField(Discount))
	drivers = FieldList(FormField(InquiryDriver))
	effectiveDate = StringField('effectiveDate')
	expirationDate = StringField('expirationDate')
	evidenceOfPriorInsurance = BooleanField('evidenceOfPriorInsurance')
	familyNumber = StringField('familyNumber')
	fcraNoticeRequired = BooleanField('fcraNoticeRequired')
	firstPolicyEffectiveDate = StringField('firstPolicyEffectiveDate')
	forms = FieldList(FormField(String))
	flyers = FieldList(FormField(String))
	id = StringField('id')
	lineOfBusiness = StringField('lineOfBusiness')
	namedInsureds = FieldList(FormField(InquiryApplicant))
	notices = FieldList(FormField(String))
	policyNumber = StringField('policyNumber')
	status = StringField('status')
	term = IntegerField('term')
	totalPremium = FloatField('totalPremium')
	totalDiscount = FloatField('totalDiscount')
	territory = StringField('territory')
	vehicles = FormField(InquiryVehicle)
	nonDescribedVehicle = FormField(NonDescribedVehicle)

class InquiryApplicant(Form):
	firstName = StringField('firstName')
	lastName = StringField('lastName')
	birthDate = StringField('birthDate')
	age = IntegerField('age')
	id = StringField('id')
	creditReport = FormField(CreditReport)

class InquiryAddress(Form):
	id = StringField('id')
	street = StringField('street')
	street2 = StringField('street2')
	city = StringField('city')
	state = StringField('state')
	zip = StringField('zip')
	county = StringField('county')
	latitude = FloatField('latitude')
	longitude = FloatField('longitude')

class InquiryCoverage(Form):
	id = StringField('id')
	type = StringField('type')
	limits = FieldList(FormField(Limit))
	premium = FloatField('premium')

class Discount(Form):
	id = StringField('id')
	type = StringField('type')

class InquiryDriver(Form):
	accidentPreventionCourse = StringField('accidentPreventionCourse')
	age = IntegerField('age')
	birthDate = StringField('birthDate')
	claims = FieldList(FormField(Claim))
	creditReport = FormField(CreditReport)
	firstName = StringField('firstName')
	gender = StringField('gender')
	id = StringField('id')
	lastName = StringField('lastName')
	manualMinorViolationCount = IntegerField('manualMinorViolationCount')
	maritalStatus = StringField('maritalStatus')
	middleName = StringField('middleName')
	licenseNumber = StringField('licenseNumber')
	licenseState = StringField('licenseState')
	licenseStatus = StringField('licenseStatus')
	sequence = IntegerField('sequence')
	suffix = StringField('suffix')
	suspensions = FieldList(FormField(Suspension))
	violationPoints = IntegerField('violationPoints')
	violations = FieldList(FormField(Violation))

class InquiryVehicle(Form):
	id = StringField('id')
	sequence = IntegerField('sequence')
	year = IntegerField('year')
	make = StringField('make')
	model = StringField('model')
	trim = StringField('trim')
	trimCode = StringField('trimCode')
	costSymbol = StringField('costSymbol')
	vin = StringField('vin')
	lengthOfOwnership = StringField('lengthOfOwnership')
	previouslyInsured = BooleanField('previouslyInsured')
	pseudoVin = StringField('pseudoVin')
	ownership = StringField('ownership')
	businessUse = StringField('businessUse')
	coverages = FieldList(FormField(InquiryCoverage))
	permissiveUserCoverages = FieldList(FormField(Coverage))
	financeCompany = FormField(InquiryFinanceCompany)

class NonDescribedVehicle(Form):
	id = StringField('id')
	coverages = FieldList(FormField(Coverage))
	permissiveUserCoverages = FieldList(FormField(Coverage))

class CreditReport(Form):
	id = StringField('id')
	referenceNumber = StringField('referenceNumber')
	score = IntegerField('score')
	status = StringField('status')
	reasons = FieldList(FormField(CreditScoreReason))

class Limit(Form):
	id = StringField('id')
	type = StringField('type')
	value = IntegerField('value')

class Claim(Form):
	id = StringField('id')
	claimDate = StringField('claimDate')
	fault = StringField('fault')
	chargeable = BooleanField('chargeable')
	payments = FieldList(FormField(ClaimPayment))

class Suspension(Form):
	id = StringField('id')
	code = StringField('code')
	suspensionDate = FormField(Object)
	reinstatementDate = FormField(Object)

class Violation(Form):
	id = StringField('id')
	code = StringField('code')
	violationDate = FormField(Object)
	convictionDate = FormField(Object)

class Coverage(Form):
	id = StringField('id')
	type = StringField('type')
	limits = FieldList(FormField(Limit))

class InquiryFinanceCompany(Form):
	address = FormField(InquiryFinanceCompanyAddress)
	id = StringField('id')
	loanNumber = StringField('loanNumber')
	name = StringField('name')

class CreditScoreReason(Form):
	id = StringField('id')
	code = StringField('code')
	description = StringField('description')

class ClaimPayment(Form):
	id = StringField('id')
	type = StringField('type')
	amount = FloatField('amount')
	status = StringField('status')

class InquiryFinanceCompanyAddress(Form):
	id = StringField('id')
	street = StringField('street')
	street2 = StringField('street2')
	city = StringField('city')
	state = StringField('state')
	zip = StringField('zip')

