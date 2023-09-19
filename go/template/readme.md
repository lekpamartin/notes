# Variables 
Appeler une variable 
```bash
{{ title }}
```
Appeler une variable et définir une valeur par defaut
```bash
{{ or title "valeur par defaut" }}
```

# Conditions 

## If / else / end

Si title existe 
```bash
{{ if title }}
```

Si title est vide 
```bash
{{if eq title "" }}
  <title>{{template "title"}} - {{ .SiteTitle }}</title>
{{else}}
  <title>{{ .SiteTitle }}</title>
{{end}}
```

# Pour aller plus loin
https://pkg.go.dev/text/template
https://developer.hashicorp.com/nomad/tutorials/templates/go-template-syntax

