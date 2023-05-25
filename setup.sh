#!/bin/bash

echo "Creating a anaconda enviroment"
# create an conda enviroment
conda create --name gpt-python-api python=3.8

# activate it
conda activate gpt-python 
echo "Conda env created successfully"

# install dependencies
pip install Flask

pip install openai

pip install gunicorn 

echo "Everything is setup, to run the development use the development.sh script"