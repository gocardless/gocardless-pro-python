import json
import hmac
import hashlib

from gocardless_pro.resources.event import Event
from gocardless_pro.errors import InvalidSignatureError

def parse(body, webhook_secret, signature_header):
    _verify_signature(body, webhook_secret, signature_header)

    events_data = json.loads(to_string(body))
    return [Event(attrs, None) for attrs in events_data['events']]

def _verify_signature(body, key, expected_signature):
    digest = hmac.new(
        to_bytes(key),
        to_bytes(body),
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(expected_signature, digest):
        raise InvalidSignatureError()

def to_bytes(string):
    if isinstance(string, str):
        return bytearray(string, 'utf-8')
    return string

def to_string(byte_sequence):
    if isinstance(byte_sequence, bytearray):
        return byte_sequence.decode("utf-8")

    return byte_sequence
