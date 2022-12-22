import codecs
from setuptools import setup, find_packages

with codecs.open('README.rst', 'r', 'utf-8') as file:
    long_description = file.read()

setup(
    name = 'gocardless_pro',
    version = '1.36.1',
    packages = find_packages(exclude=['tests']),
    install_requires = ['requests>=2.6', 'six'],
    author = 'GoCardless',
    author_email = 'engineering@gocardless.com',
    description = 'A client library for the GoCardless Pro API.',
    long_description = long_description,
    license = 'MIT',
    keywords = 'gocardless directdebit payments sepa bacs',
    url = 'https://github.com/gocardless/gocardless-pro-python',
)
