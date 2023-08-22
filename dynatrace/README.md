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
https://dynatrace.github.io/dynatrace-configuration-as-code

## Generate config.yaml
```bash
echo "configs:" > config.yaml; for i in `ls`; do echo -e "- id: ${i%.*}\n  config:\n    name: ${i%.*}\n    template: ${i%.*}.json\n    skip: false\n  type:\n    settings:\n    schema: builtin:management-zones\n    scope: environment" >> config.yaml; done
```

