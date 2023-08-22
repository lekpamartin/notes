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
