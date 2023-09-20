# Disable Job
Il faut ajouter un point devant le nom du job
```bash
.disable-job:
  script:
```

# SHARED VAR
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
