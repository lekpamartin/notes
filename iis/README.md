# Instalaltion 

# Configuration 

# Modules 

## ARR
Pour activer le Proxy
```bash
%windir%\system32\inetsrv\appcmd set config  -section:system.webServer/proxy /enabled:"True"  /commit:apphost
```
