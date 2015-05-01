from setuptools import setup, find_packages

setup(
    name = 'gocardless_pro',
    version = '0.1.0',
    packages = find_packages(),
    install_requires = ['requests>=2.6'],
    author = 'GoCardless',
    author_email = 'engineering@gocardless.com',
    description = 'A client library for the GoCardless Pro API.',
    license = 'MIT',
    keywords = 'gocardless directdebit payments sepa bacs',
    url = 'https://github.com/gocardless/gocardless-pro-python',
)
