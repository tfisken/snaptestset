import os, sys
import csv

buildCount = []
csvRows = []
projectID = sys.argv[1] #%teamcity.project.id%
buildConfName = sys.argv[2] #%system.teamcity.buildConfName%
targetFile = sys.argv[3]
projectPath = '/opt/teamcity/.BuildServer/system/artifacts/'+projectID+'/'+buildConfName+'/' #/opt/teamcity/.BuildServer/system/artifacts/LoadTest/StartLoadTest/
projectPath = '/opt/teamcity/TeamCity'

print projectPath

#create a list of paths to previous artifacts
for dirname in os.walk(projectPath).next()[1]:
    buildCount.append(dirname)

#order the list from newest to oldest
buildCount.reverse() 

print buildCount

i = 0

#read all previous csv files and add rows to list
for buildNumber in buildCount:
    while i < 10:
        i = i + 1
        with open(projectPath+'/'+buildNumber+'/.teamcity/logs/'+targetFile, 'r') as fin:
            reader = csv.reader(fin)
            for row in reader:
                next(reader, None)  # skip the headers
            	try:
                    csvRows.append(row)
            	except IndexError:
            		pass

#create aggregated CSV file
with open('/opt/tcagents/linuxtcagent/temp/agentTmp/responseTimeAggregated.csv', 'w') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["Date", "endpoint", "responseTime"])
    for row in csvRows:
        writer.writerow(row)

#/opt/teamcity/.BuildServer/system/artifacts/LoadTest/StartLoadTest/136/.teamcity/logs/buildLog.msg5