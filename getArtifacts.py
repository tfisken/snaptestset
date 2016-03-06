import urllib2
import json
import csv

apiKey = sys.argv[1]
project = sys.argv[2]
metric = sys.argv[3]

#get a list 
req = urllib2.Request('https://artifactory.gannettdigital.com/artifactory/api/storage/load-test-results/'+project+'/'+metric+'?list')
req.add_header('x-api-key', apiKey)
resp = urllib2.urlopen(req)
content = resp.read()

d = json.loads(content)
file_list = (d['files'])
#we want the newest files
file_list.sort(reverse=True)

i = 0
for value in file_list: # returns the dictionary as a list of value pairs -- a tuple.
	req = urllib2.Request('https://artifactory.gannettdigital.com/artifactory/load-test-results/'+project+'/'+metric+value['uri'])
	req.add_header('x-api-key', apiKey)
	resp = urllib2.urlopen(req)
	content = resp.read()
	i+=1
	if(i == 10)
		break
