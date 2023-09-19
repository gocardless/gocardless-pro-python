import os

import pytest

from gocardless_pro.webhooks import parse
from gocardless_pro.errors import InvalidSignatureError

fixture = open(
    os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        'webhook_body.json'
    )
).read().strip()

fixture_signature = "2693754819d3e32d7e8fcb13c729631f316c6de8dc1cf634d6527f1c07276e7e"
key = "ED7D658C-D8EB-4941-948B-3973214F2D49"

def test_it_parses_the_body():
    result = parse(fixture, key, fixture_signature)
    assert len(result) == 2

    first_event = result[0]
    assert first_event.id == "EV00BD05S5VM2T"

def test_it_parses_the_body_from_bytes():
    result = parse(bytearray(fixture, 'utf-8'), key, fixture_signature)
    assert len(result) == 2

    first_event = result[0]
    assert first_event.id == "EV00BD05S5VM2T"

def test_it_raises_with_invalid_signature():
    with pytest.raises(InvalidSignatureError):
        wrong_key = "anotherkey"
        parse(fixture, wrong_key, fixture_signature)
