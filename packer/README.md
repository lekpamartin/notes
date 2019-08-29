
# Configuration

## variables
## builders
### virtualbox-iso
#### vboxmanage et vboxmanage_post
Permettent de configurer les parametres de la machine virtuelle : RAM, CPU, disque dur , ... vboxmanage_post lance les commandes en fin de configuration. 
<br>
Ajouter un disque de 10 GO
```bash
["createhd", "--filename", "builds/packer-rhel-7-x86_64-virtualbox/sdb.vdi", "--size", "10240", "--format", "VDI"],
["storageattach", "{{.Name}}", "--storagectl", "IDE Controller", "--port", "1", "--device", "1", "--type", "hdd", "--medium",  "builds/packer-rhel-7-x86_64-virtualbox/sdb.vdi"]
````
Modifier la mémoire video (vram)
```bash
["modifyvm", "{{.Name}}", "--vram", "16"]
````
## post-processors
## provisioners
Des scripts existent dans le dossier scripts du builder
