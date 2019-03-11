# OpenDJ

## REST API
```bash
_prettyPrint=true : format JSON
```
### USER

User info
```bash
URL/api/users/<group_name>

### GROUP

Create group
```bash
curl --request PUT --header "Content-Type:application/json" --user user:password --data '{ "cn" : "value", "members" : [ { "uid" : "uid1" } ] }' https://localhost:8380/api/groups/groupname
```

Group info
```bash
URL/api/groups/<group_name>
```
