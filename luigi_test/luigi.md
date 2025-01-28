Github Luigi
https://github.com/spotify/luigi/blob/master/luigi/cmdline_parser.py

Doc luigi
https://luigi.readthedocs.io/en/stable/

Pypi
https://pypi.org/project/luigi/1.0.3/#description

medium
https://medium.com/big-data-processing/getting-started-with-luigi-what-why-how-f8e639a1f2a5

slack
https://app.slack.com/client/TMUQFBJMV/CMV4EME3G


echo "# test" >> README.md
git log
git status
git init
git add README.md
git commit -m "first commit"
git branch -M main
git checkout -b <branch name>
git branch <name>
git merge <name>
git remote add origin https://github.com/shuan3/test.git
git push -u origin main
git revert <id>
git reset --hard <id>
git reset --hard origin/branch name
# delete branch->git branch -D <branch name>

#another way
git checkout develop
git pull
git checkout <branch name>
git merge develop
# solve any conflicts

git remote add origin https://github.com/XXX/XX.git
git remote set-url origin https://username@github.com/XXX/XX.git
# put password or tokrn ->setting in github developer setting->presonal access token
git push --set-upstream origin <branch name>


git clone url


vi  ~/.zshrc



pre-commit run --all-files




https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/13-Web-Scraping/02-Web-Scraping-Exercise-Solutions.ipynb



git add .pre-commit-config.yaml


set up python library
pip config set global.cert C:Users/ID/XXX.cer
pip config set global.index-url https://......
pip config set global.extra-index-url http://....


pip install -v poetry
poetry init
poetry update
poetry install

#create virtual env
python -m venv luigienv
virtualenv luigienv --python=python3.12
source luigienv/bin/activate
. luigienv/Scripts/activate
pip install luigi
luigi --module luigi_test.src.li_test1 HelloWorld --my-parameter 100 --local-scheduler
PYTHONPATH='.' luigi --module li_test1 HelloWorld --local-scheduler
pip install luigi
luigi --module src.li_test1 HelloWorld --local-scheduler

luigi --module src.li_test1 HelloWorld --scheduler-host localhost

# to start server using luigid
# https://luigi.readthedocs.io/en/stable/central_scheduler.html#the-luigid-server
luigi --module src.li_test1 HelloWorld
luigi --module src.top_artists AggregateArtists --date-interval 2012-06




pip install <package-name>: Installs the package and shows the output of the module being installed.
poetry install: Installs the dependencies and shows the modules being installed.
pip show <package-name>: Shows information about an installed package.
pip freeze: Lists all installed modules and their versions.
pip list: Lists all installed packages.
Verbose mode (-v): Provides more detailed output for pip install.


import importlib

module_name = "math"  # This could be dynamically set
math = importlib.import_module(module_name)


import numpy as np
print(dir(np))

import pkgutil
import numpy

for module_info in pkgutil.iter_modules(numpy.__path__):
    print(module_info.name)


# List files inside a package
import os
import package_name

package_path = os.path.dirname(package_name.__file__)  # Get package path
print(f"Package location: {package_path}")

# List files in the package directory
print("Files in the package:")
print(os.listdir(package_path))

import pkgutil
import package_name

print(f"Modules and submodules in '{package_name.__name__}':")
for module_info in pkgutil.walk_packages(package_name.__path__):
    print(module_info.name)



import importlib.resources as resources
import package_name

with resources.path(package_name, "__init__.py") as path:
    print(f"Path to the __init__.py file: {path}")

# Iterate over files in a package
package_path = package_name.__path__[0]
for root, dirs, files in os.walk(package_path):
    for file in files:
        print(os.path.join(root, file))
