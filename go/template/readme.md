https://pkg.go.dev/text/template

# Variables 
Appeler une variable 
```bash
{{ title }}
```
Appeler une variable et définir une valeur par defaut
Définir un valeur ```bash
{{ or title "dfault" }}
```

# Conditions 

## If / else / end

Si title existe 
```bash
{{ if "title" }}
```

Si title est vide 
```bash
{{if eq "title" "" }}
  <title>{{template "title"}} - {{ .SiteTitle }}</title>
{{else}}
  <title>{{ .SiteTitle }}</title>
{{end}}
```
