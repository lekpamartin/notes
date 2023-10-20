# Doc

## Jenkinsfile
```bash
https://www.jenkins.io/doc/book/pipeline/syntax/
```

### Pipeline 

#### Agent

#### Parameters
Doc : https://www.jenkins.io/doc/book/pipeline/syntax/#parameters 

#### Environment
Recupérer l'id du user qui lance le pipeline : Voir https://JENKINS_URL/job/JOB_NAME/job/SUBJOB_NAME/job/main/JOB_ID/api/json?pretty=true
```bash
USER_ID = ${currentBuild.getBuildCauses()[0].userId}
```
Le mieux est d'utiliser le plugin https://plugins.jenkins.io/build-user-vars-plugin/ 
Créer une variable avec un identifiant : 
##### Secret text
```bash
TOKEN     = credentials('TOKEN')
```
##### Nom d'utilisateur et mot de passe
```bash
withCredentials()
```
#### Stages
