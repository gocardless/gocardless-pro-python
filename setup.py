from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as file:
    long_description = file.read()

setup(
    name = 'gocardless_pro',
    version = '0.2.3',
    packages = find_packages(exclude=['tests']),
    install_requires = ['requests>=2.6'],
    author = 'GoCardless',
    author_email = 'engineering@gocardless.com',
    description = 'A client library for the GoCardless Pro API.',
    long_description = long_description,
    license = 'MIT',
    keywords = 'gocardless directdebit payments sepa bacs',
    url = 'https://github.com/gocardless/gocardless-pro-python',
)
