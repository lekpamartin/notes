https://pkg.go.dev/text/template

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
