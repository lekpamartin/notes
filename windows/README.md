# Configuration 
Modifier le PATH
```bash
Barre de recherche -> Afficher les paramètres de système avancés -> Variables d'environnement
```

# Certificates 
Ajouter un certificat dans les "Autorités de certification racines de confiance"
```bash
certutil.exe -addstore Root $CA-FILE
```

# ISO
https://download.boutique-pcland-officiel.fr/iso/

# Package 
Afficher les informations sur les packages installés
```bash
wmic product get IdentifyingNumber, name, version
```
# RDP

Activation (0D) / Désactivation (1)
```bash
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```
## NLA
Désactivation 
```bash
$ComputerName = hostname
(Get-WmiObject -class Win32_TSGeneralSetting -Namespace root\cimv2\terminalservices -ComputerName $ComputerName -Filter "TerminalName='RDP-tcp'").SetUserAuthenticationRequired(0)
```
Activation (recommandé)
```bash
(Get-WmiObject -class Win32_TSGeneralSetting -Namespace root\cimv2\terminalservices -ComputerName $ComputerName -Filter "TerminalName='RDP-tcp'").SetUserAuthenticationRequired(1)
```
