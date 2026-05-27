import json
import hmac
import hashlib

from gocardless_pro.resources.event import Event
from gocardless_pro.errors import InvalidSignatureError


class WebhookParseResult:
    """
    Represents the result of parsing a webhook, containing both the events
    and the webhook metadata.
    """
    def __init__(self, events, webhook_id):
        self._events = events
        self._webhook_id = webhook_id

    @property
    def events(self):
        """Returns the list of events included in the webhook."""
        return self._events

    @property
    def webhook_id(self):
        """Returns the webhook ID from the meta field, or None if not present."""
        return self._webhook_id


def parse(body, webhook_secret, signature_header):
    _verify_signature(body, webhook_secret, signature_header)

    events_data = json.loads(to_string(body))
    return [Event(attrs, None) for attrs in events_data['events']]


def parse_with_meta(body, webhook_secret, signature_header):
    """
    Validates that a webhook was genuinely sent by GoCardless, and then parses
    it into a WebhookParseResult containing both the events and the webhook ID
    from the meta field.
    """
    _verify_signature(body, webhook_secret, signature_header)

    parsed = json.loads(to_string(body))
    events = [Event(attrs, None) for attrs in parsed['events']]
    webhook_id = parsed.get('meta', {}).get('webhook_id')

    return WebhookParseResult(events, webhook_id)

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
