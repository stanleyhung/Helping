DROP TABLE IF EXISTS INTERVIEWS CASCADE;
DROP TABLE IF EXISTS OFFERS;
CREATE table INTERVIEWS (row integer, season integer, jobnum integer, scheduler varchar(200), partnum varchar(200), interviewType VARCHAR(100), interviewDate Date, interviewTime Time, interviewEndTime Time, organization VARCHAR(400), jobtitle	VARCHAR(400), jobtype VARCHAR(400),	function VARCHAR(400), ucid integer, program VARCHAR(200), roundD varchar(200),	industry VARCHAR(200));
COPY INTERVIEWS FROM '/home/vagrant/Helping/Modified_Interviews.csv' DELIMITER ',' CSV;
CREATE table OFFERS (row integer, season integer, audited varchar(200), jobtypeoffer varchar(200), classyear varchar(200), relationshipmanager varchar(200), industry varchar(200), jobfunction varchar(200), jobfunctionother varchar(200), organization varchar(400), divisionname varchar(200), ucid integer, program varchar(200), programenrolled varchar(200), cohort varchar(200), visastatus varchar(200), citizenship varchar(200), ethnicity varchar(200), undergraduatemajor varchar(200), workexperiencemonths varchar(200), workexperienceyears varchar(200), gender varchar(200), maritalstatus varchar(200), expectedgradquarter varchar(200), graduationdate varchar(200), monthspostgraduationdate varchar(200), offerdate Date, offerstatus varchar(200), decisiondate varchar(200), dateadded varchar(200), internedfororganization varchar(200), jobtitle varchar(200), joboffersource varchar(200), joboffersourceother varchar(200), city varchar(200), state varchar(200), country varchar(200), jobreportingspecialnotes varchar(1000), basesalary varchar(200), basesalarynegotiated varchar(200), reasonfornobasesalary varchar(200), signingstartingbonusamount varchar(200), signingstartingbonuscomment varchar(200), signingstartingbonusnegotiated varchar(200), summerinternshipbonusamount varchar(200), summerinternshipbonuscomment varchar(200), summerinternshipbonusnegotiated varchar(200), earlysignonamount varchar(200), earlysignoncomment varchar(200), earlysignonnegotiated varchar(200), guaranteedyearendamount varchar(200), guaranteedyearendcomment varchar(200), guaranteedyearendnegotiated varchar(200), variableperformanceamount varchar(200), variableperformancecomment varchar(200), variableperformancenegotiated varchar(200), relocationmovingexpensesamount varchar(200), relocationmovingexpensescomment varchar(200), relocationmovingexpensesnegotiat varchar(200), housingamount varchar(200), housingcomment varchar(200), housingnegotiated varchar(200), tuitionreimbursementamount varchar(200), tuitionreimbursementcomment varchar(200), tuitionreimbursementnegotiated varchar(200), stockoptionsamount varchar(200), stockoptionscomment varchar(200), stockoptionsnegotiated varchar(200), profitsharingamount varchar(200), profitsharingcomment varchar(200), profitsharingnegotiated varchar(200), otheramount varchar(200), othercomment varchar(200), othernegotiated varchar(200), startmonthyear varchar(200), internshiplength varchar(200), offerchoice varchar(200), careerchange varchar(200), firstchoicefunction varchar(200), firstchoiceindustry varchar(200), reasoncompensation varchar(200), reasondissatisfaction varchar(200), reasoninternational varchar(200), reasononlyjoboffer varchar(200), reasonpotential varchar(200), reasontraining varchar(200), reasonculture varchar(200), reasonfirmsize varchar(200), reasonlocation varchar(200), reasonpersonal varchar(200), reasonreputation varchar(200), reasontravel varchar(200), reasonother varchar(200), authorizepublishacceptedoffers varchar(200), authorizepublishdeclinedoffers varchar(200), v105 varchar(200), offerlocked varchar(200));
COPY OFFERS FROM '/home/vagrant/Helping/Modified_Offers.csv' DELIMITER ',' CSV;

"""
Finds matches between interviews and offers on ucid, org, season, jobtype, date difference with following fields:
TODO: we can specify field names
"""
CREATE VIEW SameSeasonMatches(interviewNumber, offerNumber, season, ucid, organization, interviewDate, offerDate, interviewJobType, OfferJobType, 
	InterviewJobTitle, OfferJobTitle, InterviewFunction, OfferFunction, interviewType, offerType, bidRestriction, city, state, country) AS 
	(SELECT A.row, B.row, A.season, A.ucid, A.organization, A.interviewDate, B.offerDate, A.jobtype, B.jobtypeoffer, A.jobtitle, B.jobtitle, A.function, B.jobfunction, 
		A.interviewType, B.joboffersource, B.city, B.state, B.country, 
		CASE WHEN 
			((A.interviewType = 'Bid' AND NOT B.joboffersource = 'Interview on campus - invite schedule') OR 
			((A.interviewType = 'Invite' OR A.interviewType = 'Invited') AND NOT (B.joboffersource = 'Interview on campus - bid schedule' OR B.joboffersource = 'Interview on campus - open schedule')))
		THEN
			1
		ELSE
			0
		END
	FROM INTERVIEWS A INNER JOIN OFFERS B
	ON A.ucid = B.ucid AND A.season = B.season AND A.organization = B.organization A.jobtype = B.jobtypeoffer AND B.offerDate >= A.interviewDate);


"""
Finds the rows from the offers table that are not matched on the Matches simple join with 4 fields
"""
CREATE VIEW UnmatchedOffers(ucid, season, jobtypeoffer, organization) AS 
(SELECT ucid, season, jobtypeoffer, organization 
	FROM OFFERS EXCEPT 
	SELECT A.ucid, A.season, A.jobtype, A.organization 
	FROM INTERVIEWS A INNER JOIN OFFERS B 
	ON A.ucid = B.ucid AND A.season = B.season AND A.jobtype = B.jobtypeoffer AND A.organization = B.organization);

"""
TODO: INSERT COMMENT HERE
"""
CREATE VIEW Duplicates(ucid, org, season, type) AS 
(SELECT ucid, organization, season, jobtype from INTERVIEWS GROUP BY ucid, organization, season, jobtype HAVING COUNT(*) > 1);


"""
TODO: INSERT COMMENT HERE
"""
CREATE VIEW MultiSeasonMatches(interviewNumber, offerNumber, season, ucid, organization, interviewDate, offerDate, interviewJobType, OfferJobType, 
	InterviewJobTitle, OfferJobTitle, InterviewFunction, OfferFunction, interviewType, offerType, bidRestriction, city, state, country) AS 
	(SELECT A.row, B.row, A.season, A.ucid, A.organization, A.interviewDate, B.offerDate, A.jobtype, B.jobtypeoffer, A.jobtitle, B.jobtitle, A.function, B.jobfunction, 
		A.interviewType, B.joboffersource, B.city, B.state, B.country, 
		CASE WHEN 
			((A.interviewType = 'Bid' AND NOT B.joboffersource = 'Interview on campus - invite schedule') OR 
			((A.interviewType = 'Invite' OR A.interviewType = 'Invited') AND NOT (B.joboffersource = 'Interview on campus - bid schedule' OR B.joboffersource = 'Interview on campus - open schedule')))
		THEN
			1
		ELSE
			0
		END
	FROM INTERVIEWS A INNER JOIN OFFERS B
	ON A.ucid = B.ucid AND (A.season + 1) = B.season AND A.organization = B.organization AND B.offerDate >= A.interviewDate);



