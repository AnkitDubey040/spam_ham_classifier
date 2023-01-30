from setuptools import find_packages,setup
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"
# NOw to trigger reuirements.txt file wqe use this : 
HYPHEN_E_DOT = "-e ."



def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
 
    requirement_list = [requirement_name.replace("\n" , "") for requirement_name in requirement_list]

    # Since we don't require -e. in our lisst so we remove it: 
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


setup(
    name = "spam_ham",
    version = "0.0.1",
    author = "AnkitDubey040",
    author_email="ankitdubey04052001@gmail.com",
    packages = find_packages(), 
    install_requires = get_requirements(),
    )