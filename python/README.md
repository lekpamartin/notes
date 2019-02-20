#PYTHON

### REST

#### Requests
```bash
payload = '{ "cn" : "%s", "members" : [ %s ] }' %(cn,members)
response = requests.request("PUT", url, data=payload, headers=headers, auth=("user", "password"), verify=False)
```

Disable "InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised."
```bash
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
```

##### Proxy
Exclude proxy for somes server/ip
```bash
os.environ['no_proxy'] = 'server1,ip1,server2,ip2'
```

### LOOP

#### FOR

##### JSON
If you know the key
```bash
for key in data["content"]:
  print(key)
```

If you don't know the key
```bash
for key, value in data.items():
  print(key, value)
```
```bash
for i in data.keys():
  print(i)
```
