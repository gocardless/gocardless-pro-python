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
def test_customer_notifications_handle():
    fixture = helpers.load_fixture('customer_notifications')['handle']
    helpers.stub_response(fixture)
    response = helpers.client.customer_notifications.handle(*fixture['url_params'])
    body = fixture['body']['customer_notifications']

    assert isinstance(response, resources.CustomerNotification)
    assert responses.calls[-1].request.headers.get('Idempotency-Key') is not None
    assert response.action_taken == body.get('action_taken')
    assert response.action_taken_at == body.get('action_taken_at')
    assert response.action_taken_by == body.get('action_taken_by')
    assert response.id == body.get('id')
    assert response.type == body.get('type')
    assert response.links.customer == body.get('links')['customer']
    assert response.links.event == body.get('links')['event']
    assert response.links.mandate == body.get('links')['mandate']
    assert response.links.payment == body.get('links')['payment']
    assert response.links.refund == body.get('links')['refund']
    assert response.links.subscription == body.get('links')['subscription']

def test_timeout_customer_notifications_handle_doesnt_retry():
    fixture = helpers.load_fixture('customer_notifications')['handle']
    with helpers.stub_timeout(fixture) as rsps:
      with pytest.raises(requests.ConnectTimeout):
        response = helpers.client.customer_notifications.handle(*fixture['url_params'])
      assert len(rsps.calls) == 1

def test_502_customer_notifications_handle_doesnt_retry():
    fixture = helpers.load_fixture('customer_notifications')['handle']
    with helpers.stub_502(fixture) as rsps:
      with pytest.raises(MalformedResponseError):
        response = helpers.client.customer_notifications.handle(*fixture['url_params'])
      assert len(rsps.calls) == 1
  
