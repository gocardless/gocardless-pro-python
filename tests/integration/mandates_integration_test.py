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
def test_mandates_create():
    fixture = helpers.load_fixture('mandates')['create']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.create(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert isinstance(response, resources.Mandate)
    assert responses.calls[-1].request.headers.get('Idempotency-Key') is not None
    assert response.authorisation_source == body.get('authorisation_source')
    assert response.created_at == body.get('created_at')
    assert response.funds_settlement == body.get('funds_settlement')
    assert response.id == body.get('id')
    assert response.metadata == body.get('metadata')
    assert response.next_possible_charge_date == body.get('next_possible_charge_date')
    assert response.payments_require_approval == body.get('payments_require_approval')
    assert response.reference == body.get('reference')
    assert response.scheme == body.get('scheme')
    assert response.status == body.get('status')
    assert response.verified_at == body.get('verified_at')
    assert response.consent_parameters.end_date == body.get('consent_parameters')['end_date']
    assert response.consent_parameters.max_amount_per_payment == body.get('consent_parameters')['max_amount_per_payment']
    assert response.consent_parameters.periods == body.get('consent_parameters')['periods']
    assert response.consent_parameters.start_date == body.get('consent_parameters')['start_date']
    assert response.links.creditor == body.get('links')['creditor']
    assert response.links.customer == body.get('links')['customer']
    assert response.links.customer_bank_account == body.get('links')['customer_bank_account']
    assert response.links.new_mandate == body.get('links')['new_mandate']

@responses.activate
def test_mandates_create_new_idempotency_key_for_each_call():
    fixture = helpers.load_fixture('mandates')['create']
    helpers.stub_response(fixture)
    helpers.client.mandates.create(*fixture['url_params'])
    helpers.client.mandates.create(*fixture['url_params'])
    assert responses.calls[0].request.headers.get('Idempotency-Key') != responses.calls[1].request.headers.get('Idempotency-Key')

def test_timeout_mandates_create_idempotency_conflict():
    create_fixture = helpers.load_fixture('mandates')['create']
    get_fixture = helpers.load_fixture('mandates')['get']
    with helpers.stub_timeout_then_idempotency_conflict(create_fixture, get_fixture) as rsps:
      response = helpers.client.mandates.create(*create_fixture['url_params'])
      assert len(rsps.calls) == 2

    assert isinstance(response, resources.Mandate)

@responses.activate
def test_timeout_mandates_create_retries():
    fixture = helpers.load_fixture('mandates')['create']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.mandates.create(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['mandates']

    assert isinstance(response, resources.Mandate)

def test_502_mandates_create_retries():
    fixture = helpers.load_fixture('mandates')['create']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.mandates.create(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['mandates']

    assert isinstance(response, resources.Mandate)
  

@responses.activate
def test_mandates_list():
    fixture = helpers.load_fixture('mandates')['list']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.list(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert isinstance(response, list_response.ListResponse)
    assert isinstance(response.records[0], resources.Mandate)

    assert response.before == fixture['body']['meta']['cursors']['before']
    assert response.after == fixture['body']['meta']['cursors']['after']
    assert responses.calls[-1].request.headers.get('Idempotency-Key') is None
    assert [r.authorisation_source for r in response.records] == [b.get('authorisation_source') for b in body]
    assert [r.created_at for r in response.records] == [b.get('created_at') for b in body]
    assert [r.funds_settlement for r in response.records] == [b.get('funds_settlement') for b in body]
    assert [r.id for r in response.records] == [b.get('id') for b in body]
    assert [r.metadata for r in response.records] == [b.get('metadata') for b in body]
    assert [r.next_possible_charge_date for r in response.records] == [b.get('next_possible_charge_date') for b in body]
    assert [r.payments_require_approval for r in response.records] == [b.get('payments_require_approval') for b in body]
    assert [r.reference for r in response.records] == [b.get('reference') for b in body]
    assert [r.scheme for r in response.records] == [b.get('scheme') for b in body]
    assert [r.status for r in response.records] == [b.get('status') for b in body]
    assert [r.verified_at for r in response.records] == [b.get('verified_at') for b in body]

@responses.activate
def test_timeout_mandates_list_retries():
    fixture = helpers.load_fixture('mandates')['list']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.mandates.list(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['mandates']

    assert isinstance(response, list_response.ListResponse)
    assert isinstance(response.records[0], resources.Mandate)

    assert response.before == fixture['body']['meta']['cursors']['before']
    assert response.after == fixture['body']['meta']['cursors']['after']

def test_502_mandates_list_retries():
    fixture = helpers.load_fixture('mandates')['list']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.mandates.list(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['mandates']

    assert isinstance(response, list_response.ListResponse)
    assert isinstance(response.records[0], resources.Mandate)

    assert response.before == fixture['body']['meta']['cursors']['before']
    assert response.after == fixture['body']['meta']['cursors']['after']

@responses.activate
def test_mandates_all():
    fixture = helpers.load_fixture('mandates')['list']

    def callback(request):
        if 'after=123' in request.url:
          fixture['body']['meta']['cursors']['after'] = None
        else:
          fixture['body']['meta']['cursors']['after'] = '123'
        return [200, {}, json.dumps(fixture['body'])]

    url = 'http://example.com' + fixture['path_template']
    responses.add_callback(fixture['method'], url, callback)

    all_records = list(helpers.client.mandates.all())
    assert len(all_records) == len(fixture['body']['mandates']) * 2
    for record in all_records:
      assert isinstance(record, resources.Mandate)
    
  

@responses.activate
def test_mandates_get():
    fixture = helpers.load_fixture('mandates')['get']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.get(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert isinstance(response, resources.Mandate)
    assert responses.calls[-1].request.headers.get('Idempotency-Key') is None
    assert response.authorisation_source == body.get('authorisation_source')
    assert response.created_at == body.get('created_at')
    assert response.funds_settlement == body.get('funds_settlement')
    assert response.id == body.get('id')
    assert response.metadata == body.get('metadata')
    assert response.next_possible_charge_date == body.get('next_possible_charge_date')
    assert response.payments_require_approval == body.get('payments_require_approval')
    assert response.reference == body.get('reference')
    assert response.scheme == body.get('scheme')
    assert response.status == body.get('status')
    assert response.verified_at == body.get('verified_at')
    assert response.consent_parameters.end_date == body.get('consent_parameters')['end_date']
    assert response.consent_parameters.max_amount_per_payment == body.get('consent_parameters')['max_amount_per_payment']
    assert response.consent_parameters.periods == body.get('consent_parameters')['periods']
    assert response.consent_parameters.start_date == body.get('consent_parameters')['start_date']
    assert response.links.creditor == body.get('links')['creditor']
    assert response.links.customer == body.get('links')['customer']
    assert response.links.customer_bank_account == body.get('links')['customer_bank_account']
    assert response.links.new_mandate == body.get('links')['new_mandate']

@responses.activate
def test_timeout_mandates_get_retries():
    fixture = helpers.load_fixture('mandates')['get']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.mandates.get(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['mandates']

    assert isinstance(response, resources.Mandate)

def test_502_mandates_get_retries():
    fixture = helpers.load_fixture('mandates')['get']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.mandates.get(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['mandates']

    assert isinstance(response, resources.Mandate)
  

@responses.activate
def test_mandates_update():
    fixture = helpers.load_fixture('mandates')['update']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.update(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert isinstance(response, resources.Mandate)
    assert responses.calls[-1].request.headers.get('Idempotency-Key') is None
    assert response.authorisation_source == body.get('authorisation_source')
    assert response.created_at == body.get('created_at')
    assert response.funds_settlement == body.get('funds_settlement')
    assert response.id == body.get('id')
    assert response.metadata == body.get('metadata')
    assert response.next_possible_charge_date == body.get('next_possible_charge_date')
    assert response.payments_require_approval == body.get('payments_require_approval')
    assert response.reference == body.get('reference')
    assert response.scheme == body.get('scheme')
    assert response.status == body.get('status')
    assert response.verified_at == body.get('verified_at')
    assert response.consent_parameters.end_date == body.get('consent_parameters')['end_date']
    assert response.consent_parameters.max_amount_per_payment == body.get('consent_parameters')['max_amount_per_payment']
    assert response.consent_parameters.periods == body.get('consent_parameters')['periods']
    assert response.consent_parameters.start_date == body.get('consent_parameters')['start_date']
    assert response.links.creditor == body.get('links')['creditor']
    assert response.links.customer == body.get('links')['customer']
    assert response.links.customer_bank_account == body.get('links')['customer_bank_account']
    assert response.links.new_mandate == body.get('links')['new_mandate']

@responses.activate
def test_timeout_mandates_update_retries():
    fixture = helpers.load_fixture('mandates')['update']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.mandates.update(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['mandates']

    assert isinstance(response, resources.Mandate)

def test_502_mandates_update_retries():
    fixture = helpers.load_fixture('mandates')['update']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.mandates.update(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['mandates']

    assert isinstance(response, resources.Mandate)
  

@responses.activate
def test_mandates_cancel():
    fixture = helpers.load_fixture('mandates')['cancel']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.cancel(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert isinstance(response, resources.Mandate)
    assert responses.calls[-1].request.headers.get('Idempotency-Key') is not None
    assert response.authorisation_source == body.get('authorisation_source')
    assert response.created_at == body.get('created_at')
    assert response.funds_settlement == body.get('funds_settlement')
    assert response.id == body.get('id')
    assert response.metadata == body.get('metadata')
    assert response.next_possible_charge_date == body.get('next_possible_charge_date')
    assert response.payments_require_approval == body.get('payments_require_approval')
    assert response.reference == body.get('reference')
    assert response.scheme == body.get('scheme')
    assert response.status == body.get('status')
    assert response.verified_at == body.get('verified_at')
    assert response.consent_parameters.end_date == body.get('consent_parameters')['end_date']
    assert response.consent_parameters.max_amount_per_payment == body.get('consent_parameters')['max_amount_per_payment']
    assert response.consent_parameters.periods == body.get('consent_parameters')['periods']
    assert response.consent_parameters.start_date == body.get('consent_parameters')['start_date']
    assert response.links.creditor == body.get('links')['creditor']
    assert response.links.customer == body.get('links')['customer']
    assert response.links.customer_bank_account == body.get('links')['customer_bank_account']
    assert response.links.new_mandate == body.get('links')['new_mandate']

def test_timeout_mandates_cancel_doesnt_retry():
    fixture = helpers.load_fixture('mandates')['cancel']
    with helpers.stub_timeout(fixture) as rsps:
      with pytest.raises(requests.ConnectTimeout):
        response = helpers.client.mandates.cancel(*fixture['url_params'])
      assert len(rsps.calls) == 1

def test_502_mandates_cancel_doesnt_retry():
    fixture = helpers.load_fixture('mandates')['cancel']
    with helpers.stub_502(fixture) as rsps:
      with pytest.raises(MalformedResponseError):
        response = helpers.client.mandates.cancel(*fixture['url_params'])
      assert len(rsps.calls) == 1
  

@responses.activate
def test_mandates_reinstate():
    fixture = helpers.load_fixture('mandates')['reinstate']
    helpers.stub_response(fixture)
    response = helpers.client.mandates.reinstate(*fixture['url_params'])
    body = fixture['body']['mandates']

    assert isinstance(response, resources.Mandate)
    assert responses.calls[-1].request.headers.get('Idempotency-Key') is not None
    assert response.authorisation_source == body.get('authorisation_source')
    assert response.created_at == body.get('created_at')
    assert response.funds_settlement == body.get('funds_settlement')
    assert response.id == body.get('id')
    assert response.metadata == body.get('metadata')
    assert response.next_possible_charge_date == body.get('next_possible_charge_date')
    assert response.payments_require_approval == body.get('payments_require_approval')
    assert response.reference == body.get('reference')
    assert response.scheme == body.get('scheme')
    assert response.status == body.get('status')
    assert response.verified_at == body.get('verified_at')
    assert response.consent_parameters.end_date == body.get('consent_parameters')['end_date']
    assert response.consent_parameters.max_amount_per_payment == body.get('consent_parameters')['max_amount_per_payment']
    assert response.consent_parameters.periods == body.get('consent_parameters')['periods']
    assert response.consent_parameters.start_date == body.get('consent_parameters')['start_date']
    assert response.links.creditor == body.get('links')['creditor']
    assert response.links.customer == body.get('links')['customer']
    assert response.links.customer_bank_account == body.get('links')['customer_bank_account']
    assert response.links.new_mandate == body.get('links')['new_mandate']

def test_timeout_mandates_reinstate_doesnt_retry():
    fixture = helpers.load_fixture('mandates')['reinstate']
    with helpers.stub_timeout(fixture) as rsps:
      with pytest.raises(requests.ConnectTimeout):
        response = helpers.client.mandates.reinstate(*fixture['url_params'])
      assert len(rsps.calls) == 1

def test_502_mandates_reinstate_doesnt_retry():
    fixture = helpers.load_fixture('mandates')['reinstate']
    with helpers.stub_502(fixture) as rsps:
      with pytest.raises(MalformedResponseError):
        response = helpers.client.mandates.reinstate(*fixture['url_params'])
      assert len(rsps.calls) == 1
  
