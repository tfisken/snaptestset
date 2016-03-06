from datadog import initialize, api
import time
import datetime
import json
import sys
 
#must pass in api key and app key from teamcity
options = {
    'api_key': sys.argv[1],
    'app_key': sys.argv[2]
}

path = sys.argv[3]
 
initialize(**options)
 
start = round(time.time() - 600) #10 minutes
end = round(time.time())

#system.load.1 = The average system load over one minute.
query_cpu = 'system.cpu.idle{farm_role:cpt-oembed-web, environment:staging} by {host}' 
results = api.Metric.query(start=start, end=end, query=query_cpu)

with open(path+'/cpu.json', 'w') as file_:
    file_.write(json.dumps(results))

#system.mem.used = The amount of RAM in use shown as byte
query_memory = 'system.mem.used{farm_role:cpt-oembed-web, environment:staging} by {host}'
results = api.Metric.query(start=start, end=end, query=query_memory)

with open(path+'/memory.json', 'w') as file_:
    file_.write(json.dumps(results))

print json.dumps(results)
print path+'/memory.json'
