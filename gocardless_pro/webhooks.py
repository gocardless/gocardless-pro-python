import json
import hmac
import hashlib
import sys

from gocardless_pro.resources.event import Event
from gocardless_pro.errors import InvalidSignatureError

# Python 3+ does not have the basestring type, so we alias it
try:
    basestring
except:
    basestring = str

# Python 3.0 < x < 3.4 does not support handing a mutable bytearray
# to the hmac constructor, so we need to make a record of it ...
SUPPORTS_BYTEARRAY = sys.version_info[0] == 2 or \
  sys.version_info[1] > 3

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
    if isinstance(string, basestring):
        if SUPPORTS_BYTEARRAY:
            return bytearray(string, 'utf-8')
        return bytes(string, 'utf-8')

    if SUPPORTS_BYTEARRAY:
        return string

    return bytes(string)

def to_string(byte_sequence):
    if isinstance(byte_sequence, bytearray):
        return byte_sequence.decode("utf-8")

    return byte_sequence
