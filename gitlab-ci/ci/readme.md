# Jobs 
# Disable Job
Il faut ajouter un point devant le nom du job
```bash
.disable-job:
  script:
```
# Loops jobs 
https://docs.gitlab.com/ee/ci/yaml/#extends

# Variables 
## SHARED VAR
Il faut créer un artefact (fichier avec la liste des variables à exporter) : 
```bash
stage1:
  script:
    - ACTIONS STAGE1
    # Positionnement d'une variable pour partage
    - echo "MAVARIABLE='mavalue'" > file_with_shared_env_var
  artifacts:
    reports:
      dotenv: file_with_shared_env_var

stagen:
  stage: deploy
  script:
    - echo $MAVARIABLE # => mavalue
  dependencies:
    - stage1
```
Par exemple pour un job trigger (ou autre), le bloc dependencies peut être remlacé par 
```bash
  needs:
    - job: build
      artifacts: true
```

# Docs
https://docs.gitlab.com/ee/ci/pipelines/downstream_pipelines.html
https://repository.prace-ri.eu/git/help/user/project/push_options.md
