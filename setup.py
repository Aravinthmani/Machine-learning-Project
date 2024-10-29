from setuptools import find_packages,setup
from typing import List

HYPEN_E_DDOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DDOT in requirements:
            requirements.remove(HYPEN_E_DDOT)
    
    return requirements

setup(
    name = "MlProject",
    version = "0.0.1",
    author = "aravinth",
    author_email = "aravinthsubramanian9@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)