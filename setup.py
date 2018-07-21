from setuptools import setup

setup(
    name='revfyawo.mongo',
    version='0.0.3',
    description='A mongo ODM',
    url='https://gitlab.com/revfyawo/mongo',
    author='Lucien Haurat',
    author_email='lucien.haurat@gmail.com',
    packages=['revfyawo.mongo'],
    install_requires=['pymongo~=3.7'],
)

