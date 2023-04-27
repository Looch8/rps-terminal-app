#!/bin/bash

# To run entire file 
# ./run.sh

# Setup, start virtual environment, install requirements and run main
python3 -m venv rps-venv
source rps-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 src/main.py


# to run test (While in rps-venv)
# python -m pytest 
# Or just run pytest (in rps-venv)

# To run .sh file
# sh run.sh