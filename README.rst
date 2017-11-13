.. |circle-badge| image:: https://circleci.com/gh/gocardless/gocardless-pro-python.svg?style=shield&circle-token=:circle-token
    :target: https://circleci.com/gh/gocardless/gocardless-pro-python
.. |pypi-badge| image:: https://badge.fury.io/py/gocardless_pro.svg
    :target: https://pypi.python.org/pypi/gocardless_pro

GoCardless Pro Python client library
============================================

A Python client for interacting with the GoCardless Pro API.

|circle-badge| |pypi-badge|

Tested against Python 2.7, 3.3, 3.4, 3.5, and 3.6.

- `"Getting Started" guide <https://developer.gocardless.com/getting-started/api/introduction/?lang=python>`_ with copy and paste Python code samples
- `API reference <https://developer.gocardless.com/api-reference>`_
------------

Install from PyPI:

.. code:: bash

    $ pip install gocardless_pro


Usage
-----

Create a ``Client`` instance, providing your access token and the environment
you want to use:

.. code:: python

    import gocardless_pro
    token = os.environ['ACCESS_TOKEN']
    client = gocardless_pro.Client(access_token=token, environment='live')

Access API endpoints using the corresponding methods on the client object:

.. code:: python

    # Create a new customer. We automatically add idempotency keys to requests to create
    # resources, stopping duplicates accidentally getting created if something goes wrong
    # with the API (e.g. networking problems) - see https://developer.gocardless.com/api
    # -reference/#making-requests-idempotency-keys for details
    customer = client.customers.create(params={'email': 'jane@example.com'})

    # Fetch a payment by its ID
    payment = client.payments.get("PA123")

    # Loop through a page of payments, printing each payment's amount
    for payment in client.payments.list().records:
        decimal_amount = decimal.Decimal(payment.amount) / 100
        print('Payment for £{0}'.format(decimal_amount))

    # Create a mandate PDF in a specific language
    client.mandate_pdfs.create(
        params={'links': {'mandate': 'MD00001234XYZ'}},
        headers={'Accept-Language': 'fr'}
    )

For full documentation, see our `API reference`_.

.. _API reference: https://developer.gocardless.com/api-reference


Available resources
```````````````````

Bank details lookups
''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    # Perform a bank details lookup
    client.bank_details_lookups.create(params={...})

Creditors
''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    # Create a creditor
    client.creditors.create(params={...})

    # List creditors
    client.creditors.list(params={...})

    # Iterate through all creditors
    client.creditors.all(params={...})

    # Get a single creditor
    client.creditors.get('CR123', params={...})

    # Update a creditor
    client.creditors.update('CR123', params={...})

Creditor bank accounts
''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    # Create a creditor bank account
    client.creditor_bank_accounts.create(params={...})

    # List creditor bank accounts
    client.creditor_bank_accounts.list(params={...})

    # Iterate through all creditor_bank_accounts
    client.creditor_bank_accounts.all(params={...})

    # Get a single creditor bank account
    client.creditor_bank_accounts.get('BA123', params={...})

    # Disable a creditor bank account
    client.creditor_bank_accounts.disable('BA123', params={...})

Customers
''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    # Create a customer
    client.customers.create(params={...})

    # List customers
    client.customers.list(params={...})

    # Iterate through all customers
    client.customers.all(params={...})

    # Get a single customer
    client.customers.get('CU123', params={...})

    # Update a customer
    client.customers.update('CU123', params={...})

Customer bank accounts
''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    # Create a customer bank account
    client.customer_bank_accounts.create(params={...})

    # List customer bank accounts
    client.customer_bank_accounts.list(params={...})

    # Iterate through all customer_bank_accounts
    client.customer_bank_accounts.all(params={...})

    # Get a single customer bank account
    client.customer_bank_accounts.get('BA123', params={...})

    # Update a customer bank account
    client.customer_bank_accounts.update('BA123', params={...})

    # Disable a customer bank account
    client.customer_bank_accounts.disable('BA123', params={...})

Events
''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    # List events
    client.events.list(params={...})

    # Iterate through all events
    client.events.all(params={...})

    # Get a single event
    client.events.get('EV123', params={...})

Mandates
''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    # Create a mandate
    client.mandates.create(params={...})

    # List mandates
    client.mandates.list(params={...})

    # Iterate through all mandates
    client.mandates.all(params={...})

    # Get a single mandate
    client.mandates.get('MD123', params={...})

    # Update a mandate
    client.mandates.update('MD123', params={...})

    # Cancel a mandate
    client.mandates.cancel('MD123', params={...})

    # Reinstate a mandate
    client.mandates.reinstate('MD123', params={...})

Mandate pdfs
''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    # Create a mandate PDF
    client.mandate_pdfs.create(params={...})

Payments
''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    # Create a payment
    client.payments.create(params={...})

    # List payments
    client.payments.list(params={...})

    # Iterate through all payments
    client.payments.all(params={...})

    # Get a single payment
    client.payments.get('PM123', params={...})

    # Update a payment
    client.payments.update('PM123', params={...})

    # Cancel a payment
    client.payments.cancel('PM123', params={...})

    # Retry a payment
    client.payments.retry('PM123', params={...})

Payouts
''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    # List payouts
    client.payouts.list(params={...})

    # Iterate through all payouts
    client.payouts.all(params={...})

    # Get a single payout
    client.payouts.get('PO123', params={...})

Payout items
''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    # Get all payout items in a single payout
    client.payout_items.list(params={...})

    # Iterate through all payout_items
    client.payout_items.all(params={...})

Redirect flows
''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    # Create a redirect flow
    client.redirect_flows.create(params={...})

    # Get a single redirect flow
    client.redirect_flows.get('RE123456', params={...})

    # Complete a redirect flow
    client.redirect_flows.complete('RE123456', params={...})

Refunds
''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    # Create a refund
    client.refunds.create(params={...})

    # List refunds
    client.refunds.list(params={...})

    # Iterate through all refunds
    client.refunds.all(params={...})

    # Get a single refund
    client.refunds.get('RF123', params={...})

    # Update a refund
    client.refunds.update('RF123', params={...})

Subscriptions
''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    # Create a subscription
    client.subscriptions.create(params={...})

    # List subscriptions
    client.subscriptions.list(params={...})

    # Iterate through all subscriptions
    client.subscriptions.all(params={...})

    # Get a single subscription
    client.subscriptions.get('SB123', params={...})

    # Update a subscription
    client.subscriptions.update('SB123', params={...})

    # Cancel a subscription
    client.subscriptions.cancel('SB123', params={...})



Running tests
-------------

First, install the development dependencies:

.. code:: bash

    $ pip install -r requirements-dev.txt

To run the test suite against the current Python version, run ``nosetests``.

To run the test suite against multiple Python versions, run ``tox``.

If you don't have all versions of Python installed, you can run the tests in
a Docker container by running ``make``.
