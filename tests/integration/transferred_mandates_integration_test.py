# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import json

import pytest
import requests
import responses

from gocardless_pro.errors import MalformedResponseError
from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers
  

@responses.activate
def test_transferred_mandates_transferred_mandates():
    fixture = helpers.load_fixture('transferred_mandates')['transferred_mandates']
    helpers.stub_response(fixture)
    response = helpers.client.transferred_mandates.transferred_mandates(*fixture['url_params'])
    body = fixture['body']['transferred_mandates']

    assert isinstance(response, resources.TransferredMandate)
    assert responses.calls[-1].request.headers.get('Idempotency-Key') is None
    assert response.encrypted_customer_bank_details == body.get('encrypted_customer_bank_details')
    assert response.encrypted_decryption_key == body.get('encrypted_decryption_key')
    assert response.public_key_id == body.get('public_key_id')
    assert response.links.customer_bank_account == body.get('links')['customer_bank_account']
    assert response.links.mandate == body.get('links')['mandate']

def test_timeout_transferred_mandates_transferred_mandates_doesnt_retry():
    fixture = helpers.load_fixture('transferred_mandates')['transferred_mandates']
    with helpers.stub_timeout(fixture) as rsps:
      with pytest.raises(requests.ConnectTimeout):
        response = helpers.client.transferred_mandates.transferred_mandates(*fixture['url_params'])
      assert len(rsps.calls) == 1

def test_502_transferred_mandates_transferred_mandates_doesnt_retry():
    fixture = helpers.load_fixture('transferred_mandates')['transferred_mandates']
    with helpers.stub_502(fixture) as rsps:
      with pytest.raises(MalformedResponseError):
        response = helpers.client.transferred_mandates.transferred_mandates(*fixture['url_params'])
      assert len(rsps.calls) == 1
  
