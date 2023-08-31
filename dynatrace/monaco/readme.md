# Download

# Configuration

## Génération du fichier config.json
En vous mettant dans un dossier exporté, vous pouvez générer votre fichier config.json sans ID qui sera plus facile à gérer dans un repo. Les commandes sont des bases à adapter en fonction de vos besoins. N'hésitez pas à utiliser jq si installé. 

### builtinmanagement-zones
```bash
echo configs:;for i in `ls | grep -v config`; do name=`grep name $i | cut -d '"' -f4`; description=`grep description $i | cut -d '"' -f4`; echo -e "- id: ${name}\n  type:\n    settings:\n      schema: builtin:management-zones\n      schemaVersion: 1.0.5\n      scope: environment\n  config:\n    name: ${name}\n    template: ../templates/builtinmanagement-zones.json\n    skip: false\n    parameters:\n      laposte:\n        type: value\n        value:\n          description: $description"; done```
