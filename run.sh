#!/bin/bash

# Setup, start virtual environment, install requirements and run main
python3 -m venv rps-venv
source rps-venv/bin/activate
pip3 install -r requirements.txt
python3 src/main.py

# to run test (While in rps-venv)
# python -m pytest 

# To run .sh file
# sh run.sh