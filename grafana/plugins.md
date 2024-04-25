# Auto

# Manuel 
Dans cet exemple on va installer le plugin Flow. Attention le nom du plugin respecte cette norme: 
```
[AUTEUR]-[NAME]-panel
```
Ce qui nous donne :
```bash
grafana-cli plugins install andrewbmchugh-flow-panel
```
Il va récupérer le plugin sur cette URL
```
https://storage.googleapis.com/plugins-community/[AUTEUR]-[NAME]-panel/release/[VERSION]/[AUTEUR]-[NAME]-panel-[VERSION].zip
```
Vous pourrez donc l'installer avec cette commande 
```bash
grafana-cli --pluginURL /ZIP-DIR plugins install andrewbmchugh-flow-panel
```
