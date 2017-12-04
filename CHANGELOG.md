# 1.3.0 / 2017-12-04

* Add `can_create_refunds` to `creditor` response.

# 1.2.0 / 2017-11-13

Add `payout_items` API.

# 1.1.0 / 2017-09-18

* Add `confirmation_url` to Redirect Flows

# 1.0.0 / 2017-05-19

* Add safe retrying for requests where possible:
  * Automatically retry requests that fail due to network or GoCardless errors.
  * Automatically add an [idempotency key](https://developer.gocardless.com/api-reference/#making-requests-idempotency-keys) for POST requests if not provided manually
  * **Breaking change**: Automatically retrieve and return the existing resource in the event of a `409 idempotent_creation_conflict` response. This changes previous behaviour - instead of seeing an exception at this point, the client will now automatically retrieve the original resource that was created with that idempotency key.
* Support the new `verification_status` attribute in the Creditors API, which may be either `action_required`, `in_review` or `successful`. See the new ["Helping your users get verified" section in the partner guide](https://developer.gocardless.com/getting-started/partners/helping-your-users-get-verified/) for details.
* Add `GoCardless-Client-Library` and `GoCardless-Client-Version` headers to aid identification of requests
* Add support for Python 3.5 and Python 3.6

# 0.3.0 / 2017-02-22

* Add `scheme_identifiers` and `logo_url` to `creditor` resource
* Updates documentation
* Add `new_mandate` to `event` `Links`
* Add `new_mandate` and `customer` to `mandate` `Links`
* Remove unused `count` from `subscription` response

# 0.2.5 / 2017-02-21

* Add `six` dependency

# 0.2.4 / 2017-01-17

* Fix bug in setup.py preventing installation for some users (see #9)

# 0.2.3 / 2016-08-03

* Allow passing in custom headers (e.g. Accept-Language)
* Add `payments_require_approval` to Mandates
* Add `deducted_fees` to Payouts

# 0.2.2 / 2016-03-16

* Fix duplicate bank account error string representation (#4)

# 0.2.1 / 2016-02-05

* Exclude tests from the installed package

# 0.2.0 / 2015-12-15

* Add new API attributes to resource classes:
  * `BankDetailsLookup.bic`
  * `Creditor.default_sek_payout_account`
  * `Customer.language`
  * `Customer.swedish_identity_number`
  * `Event.organisation`
  * `RedirectFlow.customer`
  * `Refund.reference`

# 0.1.2 / 2015-07-13

* Fix support for endpoints that use "data" as the request envelope
* Make exception string representations more detailed


# 0.1.1 / 2015-07-08

* Update to api version 2015-07-06
* Add more detailed user agent header


# 0.1.0 / 2015-07-08

Initial public release. This library is in beta until it hits 1.0, so backwards
incompatible changes may be made in minor version releases.
