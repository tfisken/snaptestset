import re
import csv
import datetime

now = datetime.datetime.now()

#check for this line: "Percentage of the requests completed within given times"
#after matching it, read the 2nd line down (ms results line)
#endpoint, response time

data = {}

def convert_to_CSV():
	errorFlag = 0
	responseFlag = 0
	totalErrors = 0
	totalRequests = 0

	with open("stats.log") as f:
		for line in f:
			if(re.search('Percentage of the requests.',line)):
				responseFlag = 1
			 
			if(responseFlag == 2 and re.search('-------------------.',line)):
				responseFlag = 3

			if(responseFlag == 1 and re.search('-------------------.',line)):
				responseFlag = 2

			if(responseFlag == 2):
				responseTimes = line.split()
				try:
					if(responseTimes[7].isdigit()):
						data[responseTimes[1]] = responseTimes[7]
				except IndexError:
					print ''

def write_CSV_File():
	with open('/opt/tcagents/linuxtcagent/temp/agentTmp/responseTime.csv', 'w') as csvfile:
	    fieldnames = ['date', 'endpoint', 'responseTime']
	    writer = csv.writer(csvfile)

	    writer.writerow(fieldnames)
	    for key, value in data.iteritems():
	    	writer.writerow([now.strftime("%Y-%m-%d-%H-%M"), key, value])

convert_to_CSV()
write_CSV_File()