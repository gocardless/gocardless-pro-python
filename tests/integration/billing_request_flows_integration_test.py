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
def test_billing_request_flows_create():
    fixture = helpers.load_fixture('billing_request_flows')['create']
    helpers.stub_response(fixture)
    response = helpers.client.billing_request_flows.create(*fixture['url_params'])
    body = fixture['body']['billing_request_flows']

    assert isinstance(response, resources.BillingRequestFlow)
    assert responses.calls[-1].request.headers.get('Idempotency-Key') is not None
    assert response.authorisation_url == body.get('authorisation_url')
    assert response.auto_fulfil == body.get('auto_fulfil')
    assert response.created_at == body.get('created_at')
    assert response.customer_details_captured == body.get('customer_details_captured')
    assert response.exit_uri == body.get('exit_uri')
    assert response.expires_at == body.get('expires_at')
    assert response.id == body.get('id')
    assert response.language == body.get('language')
    assert response.lock_bank_account == body.get('lock_bank_account')
    assert response.lock_currency == body.get('lock_currency')
    assert response.lock_customer_details == body.get('lock_customer_details')
    assert response.redirect_uri == body.get('redirect_uri')
    assert response.session_token == body.get('session_token')
    assert response.show_redirect_buttons == body.get('show_redirect_buttons')
    assert response.show_success_redirect_button == body.get('show_success_redirect_button')
    assert response.links.billing_request == body.get('links')['billing_request']
    assert response.prefilled_bank_account.account_type == body.get('prefilled_bank_account')['account_type']
    assert response.prefilled_customer.address_line1 == body.get('prefilled_customer')['address_line1']
    assert response.prefilled_customer.address_line2 == body.get('prefilled_customer')['address_line2']
    assert response.prefilled_customer.address_line3 == body.get('prefilled_customer')['address_line3']
    assert response.prefilled_customer.city == body.get('prefilled_customer')['city']
    assert response.prefilled_customer.company_name == body.get('prefilled_customer')['company_name']
    assert response.prefilled_customer.country_code == body.get('prefilled_customer')['country_code']
    assert response.prefilled_customer.danish_identity_number == body.get('prefilled_customer')['danish_identity_number']
    assert response.prefilled_customer.email == body.get('prefilled_customer')['email']
    assert response.prefilled_customer.family_name == body.get('prefilled_customer')['family_name']
    assert response.prefilled_customer.given_name == body.get('prefilled_customer')['given_name']
    assert response.prefilled_customer.postal_code == body.get('prefilled_customer')['postal_code']
    assert response.prefilled_customer.region == body.get('prefilled_customer')['region']
    assert response.prefilled_customer.swedish_identity_number == body.get('prefilled_customer')['swedish_identity_number']

@responses.activate
def test_timeout_billing_request_flows_create_retries():
    fixture = helpers.load_fixture('billing_request_flows')['create']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.billing_request_flows.create(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['billing_request_flows']

    assert isinstance(response, resources.BillingRequestFlow)

def test_502_billing_request_flows_create_retries():
    fixture = helpers.load_fixture('billing_request_flows')['create']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.billing_request_flows.create(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['billing_request_flows']

    assert isinstance(response, resources.BillingRequestFlow)
  

@responses.activate
def test_billing_request_flows_initialise():
    fixture = helpers.load_fixture('billing_request_flows')['initialise']
    helpers.stub_response(fixture)
    response = helpers.client.billing_request_flows.initialise(*fixture['url_params'])
    body = fixture['body']['billing_request_flows']

    assert isinstance(response, resources.BillingRequestFlow)
    assert responses.calls[-1].request.headers.get('Idempotency-Key') is not None
    assert response.authorisation_url == body.get('authorisation_url')
    assert response.auto_fulfil == body.get('auto_fulfil')
    assert response.created_at == body.get('created_at')
    assert response.customer_details_captured == body.get('customer_details_captured')
    assert response.exit_uri == body.get('exit_uri')
    assert response.expires_at == body.get('expires_at')
    assert response.id == body.get('id')
    assert response.language == body.get('language')
    assert response.lock_bank_account == body.get('lock_bank_account')
    assert response.lock_currency == body.get('lock_currency')
    assert response.lock_customer_details == body.get('lock_customer_details')
    assert response.redirect_uri == body.get('redirect_uri')
    assert response.session_token == body.get('session_token')
    assert response.show_redirect_buttons == body.get('show_redirect_buttons')
    assert response.show_success_redirect_button == body.get('show_success_redirect_button')
    assert response.links.billing_request == body.get('links')['billing_request']
    assert response.prefilled_bank_account.account_type == body.get('prefilled_bank_account')['account_type']
    assert response.prefilled_customer.address_line1 == body.get('prefilled_customer')['address_line1']
    assert response.prefilled_customer.address_line2 == body.get('prefilled_customer')['address_line2']
    assert response.prefilled_customer.address_line3 == body.get('prefilled_customer')['address_line3']
    assert response.prefilled_customer.city == body.get('prefilled_customer')['city']
    assert response.prefilled_customer.company_name == body.get('prefilled_customer')['company_name']
    assert response.prefilled_customer.country_code == body.get('prefilled_customer')['country_code']
    assert response.prefilled_customer.danish_identity_number == body.get('prefilled_customer')['danish_identity_number']
    assert response.prefilled_customer.email == body.get('prefilled_customer')['email']
    assert response.prefilled_customer.family_name == body.get('prefilled_customer')['family_name']
    assert response.prefilled_customer.given_name == body.get('prefilled_customer')['given_name']
    assert response.prefilled_customer.postal_code == body.get('prefilled_customer')['postal_code']
    assert response.prefilled_customer.region == body.get('prefilled_customer')['region']
    assert response.prefilled_customer.swedish_identity_number == body.get('prefilled_customer')['swedish_identity_number']

def test_timeout_billing_request_flows_initialise_doesnt_retry():
    fixture = helpers.load_fixture('billing_request_flows')['initialise']
    with helpers.stub_timeout(fixture) as rsps:
      with pytest.raises(requests.ConnectTimeout):
        response = helpers.client.billing_request_flows.initialise(*fixture['url_params'])
      assert len(rsps.calls) == 1

def test_502_billing_request_flows_initialise_doesnt_retry():
    fixture = helpers.load_fixture('billing_request_flows')['initialise']
    with helpers.stub_502(fixture) as rsps:
      with pytest.raises(MalformedResponseError):
        response = helpers.client.billing_request_flows.initialise(*fixture['url_params'])
      assert len(rsps.calls) == 1
  
