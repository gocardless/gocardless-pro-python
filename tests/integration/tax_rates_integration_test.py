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
def test_tax_rates_list():
    fixture = helpers.load_fixture('tax_rates')['list']
    helpers.stub_response(fixture)
    response = helpers.client.tax_rates.list(*fixture['url_params'])
    body = fixture['body']['tax_rates']

    assert isinstance(response, list_response.ListResponse)
    assert isinstance(response.records[0], resources.TaxRate)

    assert response.before == fixture['body']['meta']['cursors']['before']
    assert response.after == fixture['body']['meta']['cursors']['after']
    assert responses.calls[-1].request.headers.get('Idempotency-Key') is None
    assert [r.end_date for r in response.records] == [b.get('end_date') for b in body]
    assert [r.id for r in response.records] == [b.get('id') for b in body]
    assert [r.jurisdiction for r in response.records] == [b.get('jurisdiction') for b in body]
    assert [r.percentage for r in response.records] == [b.get('percentage') for b in body]
    assert [r.start_date for r in response.records] == [b.get('start_date') for b in body]
    assert [r.type for r in response.records] == [b.get('type') for b in body]

@responses.activate
def test_timeout_tax_rates_list_retries():
    fixture = helpers.load_fixture('tax_rates')['list']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.tax_rates.list(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['tax_rates']

    assert isinstance(response, list_response.ListResponse)
    assert isinstance(response.records[0], resources.TaxRate)

    assert response.before == fixture['body']['meta']['cursors']['before']
    assert response.after == fixture['body']['meta']['cursors']['after']

def test_502_tax_rates_list_retries():
    fixture = helpers.load_fixture('tax_rates')['list']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.tax_rates.list(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['tax_rates']

    assert isinstance(response, list_response.ListResponse)
    assert isinstance(response.records[0], resources.TaxRate)

    assert response.before == fixture['body']['meta']['cursors']['before']
    assert response.after == fixture['body']['meta']['cursors']['after']

@responses.activate
def test_tax_rates_all():
    fixture = helpers.load_fixture('tax_rates')['list']

    def callback(request):
        if 'after=123' in request.url:
          fixture['body']['meta']['cursors']['after'] = None
        else:
          fixture['body']['meta']['cursors']['after'] = '123'
        return [200, {}, json.dumps(fixture['body'])]

    url = 'http://example.com' + fixture['path_template']
    responses.add_callback(fixture['method'], url, callback)

    all_records = list(helpers.client.tax_rates.all())
    assert len(all_records) == len(fixture['body']['tax_rates']) * 2
    for record in all_records:
      assert isinstance(record, resources.TaxRate)
    
  

@responses.activate
def test_tax_rates_get():
    fixture = helpers.load_fixture('tax_rates')['get']
    helpers.stub_response(fixture)
    response = helpers.client.tax_rates.get(*fixture['url_params'])
    body = fixture['body']['tax_rates']

    assert isinstance(response, resources.TaxRate)
    assert responses.calls[-1].request.headers.get('Idempotency-Key') is None
    assert response.end_date == body.get('end_date')
    assert response.id == body.get('id')
    assert response.jurisdiction == body.get('jurisdiction')
    assert response.percentage == body.get('percentage')
    assert response.start_date == body.get('start_date')
    assert response.type == body.get('type')

@responses.activate
def test_timeout_tax_rates_get_retries():
    fixture = helpers.load_fixture('tax_rates')['get']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.tax_rates.get(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['tax_rates']

    assert isinstance(response, resources.TaxRate)

def test_502_tax_rates_get_retries():
    fixture = helpers.load_fixture('tax_rates')['get']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.tax_rates.get(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['tax_rates']

    assert isinstance(response, resources.TaxRate)
  
