# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import json

import requests
import responses
from nose.tools import assert_equals, assert_in, assert_raises

from gocardless_pro import api_client
from gocardless_pro import errors

from . import helpers

access_token = 'access-token-xyz'
client = api_client.ApiClient('http://example.com', access_token)

@responses.activate
def test_uses_correct_url():
    responses.add(responses.GET, 'http://example.com/test', body='{}')
    client.get('/test')

@responses.activate
def test_authorization_header_present():
    responses.add(responses.GET, 'http://example.com/test', body='{}')
    client.get('/test')
    assert_equals(responses.calls[0].request.headers['authorization'],
                  'Bearer ' + access_token)

@responses.activate
def test_includes_query_params():
    responses.add(responses.GET, 'http://example.com/test', body='{}')
    client.get('/test', params={'page': '1'})
    assert_in('?page=1', responses.calls[0].request.url)

@responses.activate
def test_post_includes_json_body():
    responses.add(responses.POST, 'http://example.com/test', body='{}')
    client.post('/test', body={'name': 'Billy Jean'})
    assert_equals(responses.calls[0].request.body, '{"name": "Billy Jean"}')

@responses.activate
def test_put_includes_json_body():
    responses.add(responses.PUT, 'http://example.com/test', body='{}')
    client.put('/test', body={'name': 'Billy Jean'})
    assert_equals(responses.calls[0].request.body, '{"name": "Billy Jean"}')

@responses.activate
def test_handles_validation_failed_error():
    fixture = helpers.load_fixture('validation_failed_error')
    responses.add(responses.POST, 'http://example.com/test',
                  body=json.dumps(fixture), status=fixture['error']['code'])

    with assert_raises(errors.ValidationFailedError) as assertion:
        client.post('/test', body={'name': 'Billy Jean'})

    assert_equals(assertion.exception.documentation_url,
                  fixture['error']['documentation_url'])
    assert_equals(assertion.exception.errors, fixture['error']['errors'])

@responses.activate
def test_handles_invalid_api_usage_error():
    fixture = helpers.load_fixture('invalid_api_usage_error')
    responses.add(responses.POST, 'http://example.com/test',
                  body=json.dumps(fixture), status=fixture['error']['code'])

    with assert_raises(errors.InvalidApiUsageError) as assertion:
        client.post('/test', body={'name': 'Billy Jean'})

    assert_equals(assertion.exception.code, fixture['error']['code'])
    assert_equals(assertion.exception.errors, fixture['error']['errors'])

@responses.activate
def test_handles_invalid_state_error():
    fixture = helpers.load_fixture('invalid_state_error')
    responses.add(responses.POST, 'http://example.com/test',
                  body=json.dumps(fixture), status=fixture['error']['code'])

    with assert_raises(errors.InvalidStateError) as assertion:
        client.post('/test', body={'name': 'Billy Jean'})

    assert_equals(assertion.exception.message, fixture['error']['message'])
    assert_equals(assertion.exception.errors, fixture['error']['errors'])

@responses.activate
def test_handles_gocardless_error():
    fixture = helpers.load_fixture('gocardless_error')
    responses.add(responses.POST, 'http://example.com/test',
                  body=json.dumps(fixture), status=fixture['error']['code'])

    with assert_raises(errors.GoCardlessInternalError) as assertion:
        client.post('/test', body={'name': 'Billy Jean'})

    assert_equals(assertion.exception.type, fixture['error']['type'])
    assert_equals(assertion.exception.request_id, fixture['error']['request_id'])

@responses.activate
def test_handles_malformed_response():
    responses.add(responses.POST, 'http://example.com/test',
                  body='not valid json...', status=200)

    with assert_raises(errors.MalformedResponseError) as assertion:
        client.post('/test', body={'name': 'Billy Jean'})
