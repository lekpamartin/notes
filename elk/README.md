# ELK

### ELASTICSEARCH

### KIBANA

### LOGSTASH

#### Input

##### tcp (over SSL)
Config
```bash
tcp {
	#mode => "server"
	port => 5044
	ssl_enable => true
	#ssl_verify => false
	ssl_extra_chain_certs => ["/REP/ca.cer"]
	ssl_cert => "/REP/server.cer"
	ssl_key => "/REP/server-pkcs8.key"
	#dns_reverse_lookup_enabled => false
}
```
Test
```bash
echo 'LOG_MESSAGE' | nc -v --ssl --ssl-cert server.cer --ssl-key server.key hostname_IP 5044
```
##### HTTP (over SSL)
Config
```bash
```
Test
```bash
curl -X POST https://hostname_IP:5044 -d 'LOG_MESSAGE' --cert server.cer --key server.key 
```
