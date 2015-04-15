"""This file generates a csv containing all the distinct organization found in both tables sorted in alphabetical order (two identical columns are outputted)"""
import setup, csv

"""Output file name"""
OUTPUTFILE = setup.DIR + 'orgs.csv'

db = setup.initialize()
#Generate distinct orgs from the UNION of the two tables and write to file
db.execute("WITH intorgs AS (SELECT DISTINCT organization FROM INTERVIEWS), offorgs AS (SELECT DISTINCT organization FROM OFFERS) SELECT * FROM intorgs UNION SELECT * FROM offorgs ORDER BY organization ASC;")
results = db.fetchall()
f = open(OUTPUTFILE, 'wb')
writer = csv.DictWriter(f, fieldnames = ['Organization1', 'Organization2'])
for row in results:
	writer.writerow({'Organization1' : row[0], 'Organization2' : row[0]})
print "***Output file is " + OUTPUTFILE + " ***"

