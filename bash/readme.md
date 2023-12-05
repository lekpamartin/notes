# Variables 

## Extraction prefix / suffix 
```bash
tmp=${a#*_}   # remove prefix ending in "_"
b=${tmp%_*}   # remove suffix starting with "_"
```
Exemple
```bash
a=file1.json
b=file2.json
echo ${a%.*}
echo ${b#*.}
```

## Extract
VAR_TO_EXTRACT="hier,aujourd'hui,demain"
```bash
IFS=, read -r EXTRACT1 EXTRACT2 EXTRACT3 <<< ${VAR_TO_EXTRACT}
```
## Nombre de caractères
```bash
${#CCX} -> Nombre de caractères du contenu de la variable
```
# Encodage fichier 

## Afficher 
```bash
file -i input.file
```
## Convertir 
Convertir l'encodage d'un fichier 
```bash
iconv -f ISO-8859-1 -t UTF-8//TRANSLIT input.file -o out.file
```
