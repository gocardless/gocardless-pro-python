# GoCardless Pro Python client library

A Python client for interacting with the GoCardless Pro API.

Tested against Python 2.7, 3.3, and 3.4.


## Installation

Install from PyPI:

```bash
$ pip install gocardless_pro
```


## Usage

Create a `Client` instance, providing your access token and the environment
you want to use:

```python
import gocardless_pro
token = os.environ['ACCESS_TOKEN']
client = gocardless_pro.Client(access_token=token, environment='live')
```

Access API endpoints using the corresponding methods on the client object:

```python
# Fetch a payment by its id
payment = client.payments.get("<id>")

# Create a new payment
payment = client.payments.create(params={...})

# Loop through a page of payments
for payment in client.payments.list():
    do_things_with(payment)
```

For full documentation, see our [API docs](https://developer.gocardless.com/pro).


## Running tests

First, install the development dependencies:

```bash
$ pip install -r requirements-dev.txt
```

To run the test suite against the current Python version, run `nosetests`.

To run the test suite against multiple Python versions, run `tox`.

If you don't have all versions of Python installed, you can run the tests in
a Docker container by running `make`.

