"""
#This file generates new interview/offers csvs with the following adjustments:
	1. organization field is replaced with using the map contained within the passed-in input file
"""
import setup, csv, sys

"""Constants - CHANGE THESE IF NECSSARY"""
OUTPUTINTERVIEWS = setup.DIR + 'Modified_Interviews.csv'
OUTPUTOFFERS = setup.DIR + 'Modified_Offers.csv'

if len(sys.argv) != 2:
	print "Usage: Python generateNewData.py <organization csv file>"
	sys.exit(-1)

INPUTFILE = setup.DIR + sys.argv[1]
db = setup.initialize()

#Construct a hashmap to map original organizations to corrected organizations
orgMap = {}
reader = csv.DictReader(open(INPUTFILE, 'Urb'), fieldnames = ['original', 'corrected'])
for entry in reader:
	orgMap[entry['original']] = entry['corrected']
print '***Constructed in-memory hashmap to re-write organization names'

writer = csv.DictWriter(open(OUTPUTINTERVIEWS, 'wb'), fieldnames = ['season', 'jobnum', 'schedulenum', 'partnum', 'interviewtype', 'interviewdate', 'interviewstarttime', 'interviewendtime', 'organization', 'jobtitle', 'jobtype', 'function', 'ucid', 'program', 'round', 'industry'])
reader = csv.DictReader(open(setup.INTERVIEWS, 'Ur'), fieldnames = ['season', 'jobnum', 'schedulenum', 'partnum', 'interviewtype', 'interviewdate', 'interviewstarttime', 'interviewendtime', 'organization', 'jobtitle', 'jobtype', 'function', 'ucid', 'program', 'round', 'industry'])
for originalRow in reader:
	#Replace the organization from the original using the orgMap we generated earlier
	newRow = originalRow.copy()
	newRow['organization'] = orgMap[originalRow['organization']]
	writer.writerow(newRow)
print '***Wrote ' + OUTPUTINTERVIEWS + ' ***'

writer = csv.DictWriter(open(OUTPUTOFFERS, 'wb'), fieldnames = ['season', 'audited', 'jobtypeoffer', 'classyear', 'relationshipmanager', 'industry', 'jobfunction', 'jobfunctionother', 'organization', 'divisionname', 'ucid', 'program', 'programenrolled', 'cohort', 'visastatus', 'citizenship', 'ethnicity', 'undergraduatemajor', 'workexperiencemonths', 'workexperienceyears', 'gender', 'maritalstatus', 'expectedgradquarter', 'graduationdate', 'monthspostgraduationdate', 'offerdate', 'offerstatus', 'decisiondate', 'dateadded', 'internedfororganization', 'jobtitle', 'joboffersource', 'joboffersourceother', 'city', 'state', 'country', 'jobreportingspecialnotes', 'basesalary', 'basesalarynegotiated', 'reasonfornobasesalary', 'signingstartingbonusamount', 'signingstartingbonuscomment', 'signingstartingbonusnegotiated', 'summerinternshipbonusamount', 'summerinternshipbonuscomment', 'summerinternshipbonusnegotiated', 'earlysignonamount', 'earlysignoncomment', 'earlysignonnegotiated', 'guaranteedyearendamount', 'guaranteedyearendcomment', 'guaranteedyearendnegotiated', 'variableperformanceamount', 'variableperformancecomment', 'variableperformancenegotiated', 'relocationmovingexpensesamount', 'relocationmovingexpensescomment', 'relocationmovingexpensesnegotiat', 'housingamount', 'housingcomment', 'housingnegotiated', 'tuitionreimbursementamount', 'tuitionreimbursementcomment', 'tuitionreimbursementnegotiated', 'stockoptionsamount', 'stockoptionscomment', 'stockoptionsnegotiated', 'profitsharingamount', 'profitsharingcomment', 'profitsharingnegotiated', 'otheramount', 'othercomment', 'othernegotiated', 'startmonthyear', 'internshiplength', 'offerchoice', 'careerchange', 'firstchoicefunction', 'firstchoiceindustry', 'reasoncompensation', 'reasondissatisfaction', 'reasoninternational', 'reasononlyjoboffer', 'reasonpotential', 'reasontraining', 'reasonculture', 'reasonfirmsize', 'reasonlocation', 'reasonpersonal', 'reasonreputation', 'reasontravel', 'reasonother', 'authorizepublishacceptedoffers', 'authorizepublishdeclinedoffers', 'v105', 'offerlocked'])
reader = csv.DictReader(open(setup.OFFERS, 'Ur'), fieldnames = ['season', 'audited', 'jobtypeoffer', 'classyear', 'relationshipmanager', 'industry', 'jobfunction', 'jobfunctionother', 'organization', 'divisionname', 'ucid', 'program', 'programenrolled', 'cohort', 'visastatus', 'citizenship', 'ethnicity', 'undergraduatemajor', 'workexperiencemonths', 'workexperienceyears', 'gender', 'maritalstatus', 'expectedgradquarter', 'graduationdate', 'monthspostgraduationdate', 'offerdate', 'offerstatus', 'decisiondate', 'dateadded', 'internedfororganization', 'jobtitle', 'joboffersource', 'joboffersourceother', 'city', 'state', 'country', 'jobreportingspecialnotes', 'basesalary', 'basesalarynegotiated', 'reasonfornobasesalary', 'signingstartingbonusamount', 'signingstartingbonuscomment', 'signingstartingbonusnegotiated', 'summerinternshipbonusamount', 'summerinternshipbonuscomment', 'summerinternshipbonusnegotiated', 'earlysignonamount', 'earlysignoncomment', 'earlysignonnegotiated', 'guaranteedyearendamount', 'guaranteedyearendcomment', 'guaranteedyearendnegotiated', 'variableperformanceamount', 'variableperformancecomment', 'variableperformancenegotiated', 'relocationmovingexpensesamount', 'relocationmovingexpensescomment', 'relocationmovingexpensesnegotiat', 'housingamount', 'housingcomment', 'housingnegotiated', 'tuitionreimbursementamount', 'tuitionreimbursementcomment', 'tuitionreimbursementnegotiated', 'stockoptionsamount', 'stockoptionscomment', 'stockoptionsnegotiated', 'profitsharingamount', 'profitsharingcomment', 'profitsharingnegotiated', 'otheramount', 'othercomment', 'othernegotiated', 'startmonthyear', 'internshiplength', 'offerchoice', 'careerchange', 'firstchoicefunction', 'firstchoiceindustry', 'reasoncompensation', 'reasondissatisfaction', 'reasoninternational', 'reasononlyjoboffer', 'reasonpotential', 'reasontraining', 'reasonculture', 'reasonfirmsize', 'reasonlocation', 'reasonpersonal', 'reasonreputation', 'reasontravel', 'reasonother', 'authorizepublishacceptedoffers', 'authorizepublishdeclinedoffers', 'v105', 'offerlocked'])
for originalRow in reader:
	#Replace the organization from the original using the orgMap we generated earlier
	newRow = originalRow.copy()
	newRow['organization'] = orgMap[originalRow['organization']]
	writer.writerow(newRow)
print '***Wrote ' + OUTPUTOFFERS + ' ***'