# Projet-quantique Vendredi 11 Novembre 23H00
## Emmanuelle Bouchard, Félix Moras, Elliot Ouellet, Guillaume Blouin

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
Suivre les étapes que git vous dit


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
