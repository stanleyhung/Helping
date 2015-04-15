import psycopg2

conn = psycopg2.connect(database='vagrant', user='vagrant')
#conn.set_session(readonly=True)
db = conn.cursor()
open('/home/vagrant/Helping/Kelly_Interviews.csv', 'Ub')
open('/home/vagrant/Helping/Kelly_Offers2.csv', 'Ub') 

#change encoding because excel is annoying
db.execute('set client_encoding to "latin 1"');

#delete tables in case they aready exist
db.execute('DROP TABLE IF EXISTS INTERVIEWS CASCADE;')
db.execute('DROP TABLE IF EXISTS OFFERS CASCADE;')

#create INTERVIEWS and OFFERS table from the csv sources
db.execute('CREATE table INTERVIEWS (season varchar(200), jobnum varchar(200), scheduler varchar(200), partnum varchar(200), interviewType VARCHAR(100), interviewDate VARCHAR(100), interviewTime VARCHAR(100), interviewEndTime VARCHAR(100), organization VARCHAR(400), jobtitle	VARCHAR(400), jobtype VARCHAR(400),	function VARCHAR(400), ucid varchar(200), program VARCHAR(200), roundD varchar(200),	industry VARCHAR(200));')
db.execute("COPY INTERVIEWS FROM '/home/vagrant/Helping/Kelly_Interviews.csv' DELIMITER ',' CSV;")
db.execute("CREATE table OFFERS (season varchar(200), audited varchar(200), jobtypeoffer varchar(200), classyear varchar(200), relationshipmanager varchar(200), industry varchar(200), jobfunction varchar(200), jobfunctionother varchar(200), organization varchar(400), divisionname varchar(200), ucid varchar(200), program varchar(200), programenrolled varchar(200), cohort varchar(200), visastatus varchar(200), citizenship varchar(200), ethnicity varchar(200), undergraduatemajor varchar(200), workexperiencemonths varchar(200), workexperienceyears varchar(200), gender varchar(200), maritalstatus varchar(200), expectedgradquarter varchar(200), graduationdate varchar(200), monthspostgraduationdate varchar(200), offerdate varchar(200), offerstatus varchar(200), decisiondate varchar(200), dateadded varchar(200), internedfororganization varchar(200), jobtitle varchar(200), joboffersource varchar(200), joboffersourceother varchar(200), city varchar(200), state varchar(200), country varchar(200), jobreportingspecialnotes varchar(1000), basesalary varchar(200), basesalarynegotiated varchar(200), reasonfornobasesalary varchar(200), signingstartingbonusamount varchar(200), signingstartingbonuscomment varchar(200), signingstartingbonusnegotiated varchar(200), summerinternshipbonusamount varchar(200), summerinternshipbonuscomment varchar(200), summerinternshipbonusnegotiated varchar(200), earlysignonamount varchar(200), earlysignoncomment varchar(200), earlysignonnegotiated varchar(200), guaranteedyearendamount varchar(200), guaranteedyearendcomment varchar(200), guaranteedyearendnegotiated varchar(200), variableperformanceamount varchar(200), variableperformancecomment varchar(200), variableperformancenegotiated varchar(200), relocationmovingexpensesamount varchar(200), relocationmovingexpensescomment varchar(200), relocationmovingexpensesnegotiat varchar(200), housingamount varchar(200), housingcomment varchar(200), housingnegotiated varchar(200), tuitionreimbursementamount varchar(200), tuitionreimbursementcomment varchar(200), tuitionreimbursementnegotiated varchar(200), stockoptionsamount varchar(200), stockoptionscomment varchar(200), stockoptionsnegotiated varchar(200), profitsharingamount varchar(200), profitsharingcomment varchar(200), profitsharingnegotiated varchar(200), otheramount varchar(200), othercomment varchar(200), othernegotiated varchar(200), startmonthyear varchar(200), internshiplength varchar(200), offerchoice varchar(200), careerchange varchar(200), firstchoicefunction varchar(200), firstchoiceindustry varchar(200), reasoncompensation varchar(200), reasondissatisfaction varchar(200), reasoninternational varchar(200), reasononlyjoboffer varchar(200), reasonpotential varchar(200), reasontraining varchar(200), reasonculture varchar(200), reasonfirmsize varchar(200), reasonlocation varchar(200), reasonpersonal varchar(200), reasonreputation varchar(200), reasontravel varchar(200), reasonother varchar(200), authorizepublishacceptedoffers varchar(200), authorizepublishdeclinedoffers varchar(200), v105 varchar(200), offerlocked varchar(200));")
db.execute("COPY OFFERS FROM '/home/vagrant/Helping/Kelly_Offers2.csv' DELIMITER ',' CSV;")

#verify the integrity of the tables with known row lengths
db.execute("SELECT COUNT(*) FROM INTERVIEWS;")
i = db.fetchall()[0]
assert i[0] == 89560
db.execute("SELECT COUNT(*) FROM OFFERS;")
i = db.fetchall()[0]
assert i[0] == 7615
print "***Constructed INTERVIEWS and OFFERS tables from csv files***"




















"""
DROP TABLE IF EXISTS INTERVIEWS CASCADE;
DROP TABLE IF EXISTS OFFERS;
CREATE table INTERVIEWS (season varchar(200), jobnum varchar(200), scheduler varchar(200), partnum varchar(200), interviewType VARCHAR(100), interviewDate VARCHAR(100), interviewTime VARCHAR(100), interviewEndTime VARCHAR(100), organization VARCHAR(400), jobtitle	VARCHAR(400), jobtype VARCHAR(400),	function VARCHAR(400), ucid varchar(200), program VARCHAR(200), roundD varchar(200),	industry VARCHAR(200));
COPY INTERVIEWS FROM '/home/vagrant/kelly/Kelly_Interviews.csv' DELIMITER ',' CSV;
CREATE table OFFERS (season varchar(200), audited varchar(200), jobtypeoffer varchar(200), classyear varchar(200), relationshipmanager varchar(200), industry varchar(200), jobfunction varchar(200), jobfunctionother varchar(200), organization varchar(400), divisionname varchar(200), ucid varchar(200), program varchar(200), programenrolled varchar(200), cohort varchar(200), visastatus varchar(200), citizenship varchar(200), ethnicity varchar(200), undergraduatemajor varchar(200), workexperiencemonths varchar(200), workexperienceyears varchar(200), gender varchar(200), maritalstatus varchar(200), expectedgradquarter varchar(200), graduationdate varchar(200), monthspostgraduationdate varchar(200), offerdate varchar(200), offerstatus varchar(200), decisiondate varchar(200), dateadded varchar(200), internedfororganization varchar(200), jobtitle varchar(200), joboffersource varchar(200), joboffersourceother varchar(200), city varchar(200), state varchar(200), country varchar(200), jobreportingspecialnotes varchar(1000), basesalary varchar(200), basesalarynegotiated varchar(200), reasonfornobasesalary varchar(200), signingstartingbonusamount varchar(200), signingstartingbonuscomment varchar(200), signingstartingbonusnegotiated varchar(200), summerinternshipbonusamount varchar(200), summerinternshipbonuscomment varchar(200), summerinternshipbonusnegotiated varchar(200), earlysignonamount varchar(200), earlysignoncomment varchar(200), earlysignonnegotiated varchar(200), guaranteedyearendamount varchar(200), guaranteedyearendcomment varchar(200), guaranteedyearendnegotiated varchar(200), variableperformanceamount varchar(200), variableperformancecomment varchar(200), variableperformancenegotiated varchar(200), relocationmovingexpensesamount varchar(200), relocationmovingexpensescomment varchar(200), relocationmovingexpensesnegotiat varchar(200), housingamount varchar(200), housingcomment varchar(200), housingnegotiated varchar(200), tuitionreimbursementamount varchar(200), tuitionreimbursementcomment varchar(200), tuitionreimbursementnegotiated varchar(200), stockoptionsamount varchar(200), stockoptionscomment varchar(200), stockoptionsnegotiated varchar(200), profitsharingamount varchar(200), profitsharingcomment varchar(200), profitsharingnegotiated varchar(200), otheramount varchar(200), othercomment varchar(200), othernegotiated varchar(200), startmonthyear varchar(200), internshiplength varchar(200), offerchoice varchar(200), careerchange varchar(200), firstchoicefunction varchar(200), firstchoiceindustry varchar(200), reasoncompensation varchar(200), reasondissatisfaction varchar(200), reasoninternational varchar(200), reasononlyjoboffer varchar(200), reasonpotential varchar(200), reasontraining varchar(200), reasonculture varchar(200), reasonfirmsize varchar(200), reasonlocation varchar(200), reasonpersonal varchar(200), reasonreputation varchar(200), reasontravel varchar(200), reasonother varchar(200), authorizepublishacceptedoffers varchar(200), authorizepublishdeclinedoffers varchar(200), v105 varchar(200), offerlocked varchar(200));
COPY OFFERS FROM '/home/vagrant/kelly/Kelly_Offers2.csv' DELIMITER ',' CSV;

SELECT COUNT(*) FROM OFFERS A LEFT JOIN INTERVIEWS B ON A.ucid = B.ucid AND A.season = B.season AND A.jobtypeoffer = B.jobtype
	WHERE NOT B.organization SIMILAR TO 'Mock%' AND NOT B.organization SIMILAR TO 'mock%';

WITH intorgs AS (SELECT DISTINCT organization FROM INTERVIEWS)
offorgs AS (SELECT DISTINCT organization FROM OFFERS)
SELECT * FROM intorgs UNION offorgrgas;

SELECT DISTINCT A.organization FROM OFFERS A where A.organization NOT IN (SELECT organization FROM INTERVIEWS);
"""
