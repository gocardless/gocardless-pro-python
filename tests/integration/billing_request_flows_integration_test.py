# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import json

import requests
import responses
from nose.tools import (
  assert_equal,
  assert_is_instance,
  assert_is_none,
  assert_is_not_none,
  assert_not_equal,
  assert_raises
)

from gocardless_pro.errors import MalformedResponseError
from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers
  

@responses.activate
def test_billing_request_flows_create():
    fixture = helpers.load_fixture('billing_request_flows')['create']
    helpers.stub_response(fixture)
    response = helpers.client.billing_request_flows.create(*fixture['url_params'])
    body = fixture['body']['billing_request_flows']

    assert_is_instance(response, resources.BillingRequestFlow)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.authorisation_url, body.get('authorisation_url'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.expires_at, body.get('expires_at'))
    assert_equal(response.redirect_uri, body.get('redirect_uri'))
    assert_equal(response.links.billing_request,
                 body.get('links')['billing_request'])

@responses.activate
def test_timeout_billing_request_flows_create_retries():
    fixture = helpers.load_fixture('billing_request_flows')['create']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.billing_request_flows.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['billing_request_flows']

    assert_is_instance(response, resources.BillingRequestFlow)

def test_502_billing_request_flows_create_retries():
    fixture = helpers.load_fixture('billing_request_flows')['create']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.billing_request_flows.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['billing_request_flows']

    assert_is_instance(response, resources.BillingRequestFlow)
  
