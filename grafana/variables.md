https://grafana.com/docs/grafana/latest/dashboards/variables/

Quelques conseils pour construire ses Query pour les variables en fonction des datasources : 

# Elastic
Lister les clés 
```
{"find": "fields", "type": "keyword"}
```
Prendre le champ à utiliser pour la liste de votre variable : 
```
{"find": "terms", "field": "FIELD.keyword"}
```
Pour en savoir plus : https://grafana.com/docs/grafana/latest/datasources/elasticsearch/template-variables/ 
