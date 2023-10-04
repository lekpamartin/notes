#!/usr/bin/python3
# Martin LEKPA
 
import json
import http.client
import os
from urllib.parse import urlparse
import ssl

DT_URL= os.environ['DT_URL']
DT_TOKEN= os.environ['DT_TOKEN']

DOMAIN = urlparse(DT_URL).netloc
ENV_ID = DT_URL.split("/")[4]

conn = http.client.HTTPSConnection(DOMAIN, context = ssl._create_unverified_context())

headers = {
  "accept": "application/json; charset=utf-8",
  "Authorization": "Api-Token " + DT_TOKEN + ""
}

conn.request("GET", "/e/" + ENV_ID + "/api/config/v1/managementZones", headers=headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

json = json.loads(data)
print(os.getcwd())
values = json['values']

output = {}
for i in values:
  output[i['name']] = i['id']

import json
json_output = json.dumps(output)

f = open("management_zones.json", "w")
f.write(json_output)
f.close()
