from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """Function to return a list of requirements from the requirements.txt file"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.rstrip("/n") for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements


setup(
    name='end-to-end-ml',
    version='0.0.1',
    author='Shanice',
    author_email='shanice.williams@live.co.uk',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
