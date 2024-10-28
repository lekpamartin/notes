# Configuration 
SL0 => Anomaly detection (metrics events) => alerting profile => pb notification

## Management zone 
Ajouter dans la zone de management les services indirects : DB, ...
```bash
"entitySelector": "type(service),toRelationships.calls(type(service),tag(key:VALUE)),agentTechnologyType(N/A)"
```
Ajouter dans la zone de management d'un projet GCP les instances Cloud Run : cloud:gcp:cloud_run_revision
```bash
"entitySelector": "type("cloud:gcp:cloud_run_revision"),fromRelationships.isChildOf(<entitySelector pour selectionner le projet>)"
```
Vous pouvez faire de même pour les autres éléments contenus dans le projet. Pour voir les éléments dans un projet GCP
```bash
curl -X 'GET' \
  'URL/v2/entities/PROJECTID' \
  -H 'accept: application/json; charset=utf-8' \
  -H 'Authorization: Api-Token TOKEN'
```

# Collect 

# Détection de deploiement d'une nouvelle version
https://www.dynatrace.com/support/help/platform-modules/cloud-automation/release-monitoring/version-detection-strategies

## Gestion des evenements 
https://www.dynatrace.com/support/help/platform-modules/cloud-automation/release-monitoring/version-detection-strategies

## Jenkins to Dynatrace 
https://www.dynatrace.com/news/blog/simplify-and-standardize-dynatrace-integration-to-jenkins-software-delivery-pipelines-with-shared-libraries/

# Infrastructure as Code

## API V2
https://www.dynatrace.com/support/help/dynatrace-api

# Configuration as Code
https://www.dynatrace.com/support/help/manage/configuration-as-code
https://github.com/Dynatrace/dynatrace-configuration-as-code

https://github.com/dynatrace-perfclinics/dynatrace-getting-started

https://github.com/dynatrace-ace-services/fundamentals
https://github.com/dynatrace-ace-services/slo-simply-smarter

https://dynatrace.github.io/BizOpsConfigurator/
https://dynatrace.github.io/dynatrace-configuration-as-code
