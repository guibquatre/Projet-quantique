# Projet-quantique Vendredi 11 Novembre 23H00
# Emmanuelle Bouchard, Félix Moras, Elliot Ouellet, Guillaume Blouin
## Python 3.10 est requis pour démarrer le programme main.py
## Vous devez avoir numpy et matplotlib pour python3.10
`python3.10 -m pip install numpy matplotlib`
#### Assurez vous d'avoir un environnement virtuel au besoin et lancez le programme avec Python3.10
### Telechargez le rendu visuel pour MatplotLib
`sudo apt-get install python3-tk
`

|Fichiers|Dossiers|Description|
|:---|---|---:|
|main.py| |fichier pour lancer au workflow|
|main.ipynb| |fichier de remise|
|quickGit| |programme pour sauvegarder les sources rapidement|
|.github/workflows/blank.yml| |lance l'intégration continue|

[Environnement virtuel python sur ubuntu ou gitBash](https://thkernel.medium.com/comment-cr%C3%A9er-un-environnement-virtuel-python-sur-ubuntu-18-04-gikspirit-3fad29d284e1)
[Environnement virtuel python sur macOs](https://www.studytonight.com/post/python-virtual-environment-setup-on-mac-osx-easiest-way)

## Creer une branche github
```
git checkout -b nomDeBranche
git push
```
##### Suivre les étapes que git vous dit


## Obtenir un environnement virtuel et pycodestyle
```bash
sudo apt-get install python3-tk
sudo apt install pycodestyle
pycodestyle -vv main.py
sudo apt install python3-venv
python3 -m venv projet-quantique-env
source projet-quantique-env/bin/activate
pip install numpy
pip install matplotlib
```

# Démarrer le programme, soyez à la racine du dépôt et écrivez la commande
`python main.py`
`python3 main.py`
`python3.10 main.py`
