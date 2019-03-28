## Install 
It is a plugin for elasticsearch and kibana
```bash
bin/elasticsearch-plugin install -v -b com.amazon.opendistroforelasticsearch:elasticsearch-security:0.7.0.0
```
## Configuration 

### Load configuration 
For demo :
```bash
/usr/share/elasticsearch/plugins/opendistro_security/tools/install_demo_configuration.sh -y -i -s
```
For Production env
```bash
/usr/share/elasticsearch/plugins/opendistro_security/tools/securityadmin.sh -cd "/usr/share/elasticsearch/plugins/opendistro_security/securityconfig" -icl -key "/usr/share/elasticsearch/config/kirk-key.pem" -cert "/usr/share/elasticsearch/config/kirk.pem" -cacert "/usr/share/elasticsearch/config/root-ca.pem" -nhnv
```

## API

### Role

```bash
payload = '{ "cluster" : [ "CLUSTER_COMPOSITE_OPS" ], "indices" : { "<REGEX>" : { "*" : [ "UNLIMITED" ] }, "?kibana*" : { "*" : [ "CRUD" ] } } }'
```

### Role mapping


### Documentation
https://opendistro.github.io/for-elasticsearch-docs/docs/security/api
