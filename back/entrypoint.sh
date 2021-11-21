#!/bin/bash

# Create Virtualenv for Python

if [ -d "./venv" ]
then
    echo "VENV Exist"
else
    pip install virtualenv
    virtualenv venv
fi

source venv/bin/activate

# Install all requirements

/usr/local/bin/python -m pip install --upgrade pip
pip install -r requirements.txt

cd app
python manage.py runserver 0.0.0.0:8000
echo "Backend is Running on localhost:8000"