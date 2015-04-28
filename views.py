"""File to keep track of all views"""
import useModifiedData, setup, psycopg2

VIEWSFILE = setup.DIR + 'views.sql'

buff = []
db = useModifiedData.reinitialize()
fd = open(VIEWSFILE, 'r')

seenComment = False
for line in fd:
	if "\"\"\"" in line:
		seenComment = not seenComment
	else:
		if not seenComment:
			buff.append(line)

allLines = ""
for line in buff:
	allLines = allLines + line

sqlCommands = allLines.split(';')

for command in sqlCommands:
	try:
		db.execute(command)
	except psycopg2.ProgrammingError as e:
		print "***ERROR but continuing after command: " + command