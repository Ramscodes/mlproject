from setuptools import find_packages, setup
from typing import List

# Declaring variable for setup functions 
PROJECT_NAME = "housing - predictor"
VERSION = "0.0.3"
AUTHOR = "Ram"
DESCRIPTION = "This is my first ml project"
PACKAGES = ["housing"] # instead of this we can also function find_packages()
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description : This function is going to read the requirements.txt file

    return This function is going to return a list which contains
     the libraries written in the requirements.txt file 
    """
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readlines()


setup(name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),#PACKAGES,
install_requires = get_requirements_list()
)
"""
w->here ever we find __init__ file we call it as a package 
->we add -e . in requirements.txt in order to install the current project packages["housing"] 
along with the external packages["numpy"..]
->or else we also can use pip install -e .
->to write -e . in the reuiremnts.txt the setup.py file is mandatory. 
->if we add -e . in the requirements.txt we have to remove the -e . from the list that is returning 
from the get_requirements_list()
"""