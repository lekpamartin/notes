import json
import http.client
import sys

DOMAIN= sys.argv[1]
ENV_ID= sys.argv[2] 
ENV_TOKEN= sys.argv[3] 

f = open("output.json", "w")

conn = http.client.HTTPSConnection(DOMAIN)

headers = {
  "accept": "application/json; charset=utf-8",
  "Authorization": "Api-Token " + ENV_TOKEN + ""
}

conn.request("GET", "/e/" + ENV_ID + "/api/config/v1/managementZones", headers=headers)

res = conn.getresponse()
data = res.read()

json = json.loads(data)

mgtzones = ""

for i in json['values']:
  if mgtzones == "":
    mgtzones = '"' + i['name'] + '"'
  else:
    mgtzones = mgtzones + ',"' + i['name'] + '"'

conn.request("GET", "/e/" + ENV_ID + "/api/v2/entities?entitySelector=type(host),state(RUNNING),not(mzName(" + mgtzones + "))", headers=headers)

res = conn.getresponse()
data = res.read()

f.write(data.decode("utf-8"))
f.close()

