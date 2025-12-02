from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    "this function will return something something"
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
setup(
    name="PR",                      # Your package name
    version="0.0.1",                       # Package version
    author="diya",                    # Your name
    author_email="diyavirmani41@gmail.com",  # Your email
    packages=find_packages(),              # Detect all packages automatically
    install_requires=get_requirements('requirements.txt')                # Dependencies will install automatical
)
