
```bash
semanage port -a -t $TAG -p tcp $HTTP-PORT
```

```bash
/usr/sbin/setsebool -P httpd_can_network_connect 1
```
