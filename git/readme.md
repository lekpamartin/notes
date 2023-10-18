# CMD
## Push
Créer la nouvelle branche sur le distant 
```bash
git push --set-upstream origin NOUVELLE_BRANCHE
```
Demander la création d'une PR/MR lors du push
```bash
git push -o merge_request.create
```
D'autres options pour le merge request : https://docs.gitlab.com/ee/user/project/push_options.html#push-options-for-merge-requests 

# Errors
error: src refspec BRANCH does not match any
```bash
git remote add origin https://USER:PASSWORD6TOKEN@HOSTNAME/REPO.git
```
Vous pouvez avoir une erreur 
```bash
git remote set-url origin https://USER:PASSWORD6TOKEN@HOSTNAME/REPO.git
```
