#building an application as a package  which can be used by others
from setuptools import find_packages,setup
from typing import List
h='-e .'
# this will trigger the function requirements in requirement.txt 
# but also include in that so we need to remove this 
 
def get_requirements(file_path:str)->List[str]:
    '''
    this will return list of requiremets 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if h in requirements:
            requirements.remove(h)
setup(
    name='mlproject',
    version='0.0.1',
    author='vaishu',
    author_email='vaishnaviakula00@gmail.com',
    packages=find_packages(),
    #install_requires=['pandas','numpy','seaborn'] all cnanot be mentioned heere
    install_requires=get_requirements('requirements.txt')
)