from setuptools import setup, find_packages

# Install requeried dependecies
pip3 install -r requests

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='kodi',
    version='0.1.4',
    description='Script that uses Kodis jsonrpc',
    long_description=readme,
    author='Oscar Törnroth',
    author_email='oscar@vettig.se',
    url='https://github.com/h0yta/kodiScript',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)