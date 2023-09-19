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
