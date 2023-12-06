# PYTHON

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

### FILE
Probleme d'encodage ascii
```bash
f = open('/REP/file.json', 'rb')
data = f.read().decode('utf8', 'ignore')
```

### JSON
#### Build a JSON
```bash
myDict = dict()
myDict["content"] = {}
for j in items:
  myDict["content"][project] = dict()
  myDict["content"][project]["type"] = j["projectType"]
  #Append if exist and affect if don't exist
  try:
    myDict["content"][project]["users"].append(user)
  except KeyError:
    myDict["content"][project]["users"] = [user]
```

#### Merge JSON files
```bash
json_files = ["file1.json", "file2.json"]
files_merged = list()
for f1 in json_files:
  with open(f1, 'r') as infile:
    files_merged.extend(json.load(infile))
```
### Proxy
Exclude proxy for somes server/ip
```bash
os.environ['no_proxy'] = 'server1,ip1,server2,ip2'
```

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

### YAML

#### Read file
```bash
stream = open("docker-compose.yml", "r")
docs = yaml.load_all(stream, Loader=yaml.FullLoader)
for doc in docs:
  for k,v in doc.items():
```
