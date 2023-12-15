from setuptools import setup, find_packages

setup(
    name='LPVutils',
    version='1.0.0',
    author='Kristof Floch',
    author_email='kristof.floch@gmail.com',
    description='Python implementation of common utility functions and algorithms for linear parameter-varying (LPV) systems',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ]
)
