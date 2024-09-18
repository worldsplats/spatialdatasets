# setup.py
from setuptools import setup, find_packages

setup(
    name='spatialdatasets',
    version='0.1',
    description='A package to load and manage 3D datasets',
    author='zaikun',
    author_email='xuzaikun@huaga3d.com',
    packages=find_packages(),
    install_requires=[
        'requests',  # For HTTP requests
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
