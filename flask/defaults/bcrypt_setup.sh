#! usr/bin/bash
#installs bycrpyt inside the shell environment
pipenv shell
pipenv install flask-bcrypt
# deletes file after install
rm bcrypt_setup.sh