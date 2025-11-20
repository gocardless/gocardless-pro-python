import os
import json

import pytest
import responses

from gocardless_pro import Client
from gocardless_pro import resources

fixture_path = os.path.join(
    os.path.dirname(__file__),
    'fixtures',
    'payment_account_transactions.json'
)
with open(fixture_path) as f:
    fixtures = json.load(f)

list_fixture = fixtures['list']

@responses.activate
def test_payment_account_transactions_list():
    url = 'https://api-sandbox.gocardless.com' + '/payment_accounts/BA0000107EBP2S/transactions'
    responses.add(
        responses.GET,
        url,
        json=list_fixture['body'],
        status=200
    )

    client = Client(access_token='test_token', environment='sandbox')
    response = client.payment_account_transactions.list('BA0000107EBP2S')

    assert len(response.records) == 2
    assert isinstance(response.records[0], resources.PaymentAccountTransaction)
    assert isinstance(response.records[1], resources.PaymentAccountTransaction)

    fixture_transactions = list_fixture['body']['payment_account_transactions']
    assert response.records[0].id == fixture_transactions[0]['id']
    assert response.records[0].amount == fixture_transactions[0]['amount']
    assert response.records[0].direction == fixture_transactions[0]['direction']
    assert response.records[0].counterparty_name == fixture_transactions[0]['counterparty_name']

    assert response.records[1].id == fixture_transactions[1]['id']
    assert response.records[1].amount == fixture_transactions[1]['amount']
    assert response.records[1].direction == fixture_transactions[1]['direction']
    assert response.records[1].counterparty_name == fixture_transactions[1]['counterparty_name']
