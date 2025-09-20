from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e.'
def get_requirements(filepath:str)->List[str]: ### mentioning that this will contain list and that list is string


    """
    this function will return the list of requirements
    """
    requirements=[]
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)


setup(

    name="FastAPI",
    version='0.0.1',
    author='Nisha',
    author_email='nishaganesan63@gmail.com',
    packages=find_packages(), ## this package will look for the __init.py__ file, so that file will make as the src as the package and try to build that init file so that we can import that package anywhere we want
    install_requires=get_requirements('requirements.txt')
)