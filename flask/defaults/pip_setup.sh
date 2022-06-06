#! usr/bin/bash
#installs pipenv and flask in the current folder
echo 'Installing pipenv'
pipenv install
echo 'Installing flask'
pipenv install flask
#deletes file after installs
rm pip_setup.sh