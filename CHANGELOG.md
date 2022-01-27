<!-- @format -->
# 1.27.0

- Release Block API

# 1.26.0

- Adds support for recent Billing Request Changes:
  - Allows the payer to confirm the details provided before creating the mandate as per the scheme compliance rules
  - Adds BillingRequestTemplate which can be used to create many child Billing Request and Flows

# 1.22.0

- Added a new resource called payer_authorisatons
  - This is our new API dedicated to building custom payment pages. It encapsulates the creation of customer, bank account and mandate under this single resource.

# 1.21.0

- Added a new event called `payer_authorisation_completed` for an upcoming resource type called `payer_authorisation` which provides `customer`, `customer_bank_account`, `mandate` and `payer_authorisation` links

# 1.20.0

- Added support for applying tax to transaction and surcharge fees.
  - Added `taxes` to payout_items.
  - Added `tax_currency` to payout.
  - Added `tax_rates` endpoint.
  - Added a payout `tax_exchange_rates_confirmed` webhook to know when the exchange rate has been finalised for all fees in the payout.

# 1.19.0

- adds `not_retried_reason` to payment failed event

# 1.18.0

* support new update instalment schedules route

# 1.17.0

* fix: support new keys in creditor events
* support payout metadata
* support new update payouts route

# 1.16.1

* Adds metadata param to redirect flow creation endpoint
* Adds the ability to pause and resume a subscription
* Modify the earliest charge date for paused subscriptions

# 1.16.0

* uses new instalment schedules schema (with two different create methods)
* adds 'count' field to subscriptions response

# 1.15.1

* Add support for `currency_exchange_rates`

# 1.15.0

* support for creditor webhooks
* support for raising an error on Idempotency Key Conflicts

# 1.14.0

* add `will_attempt_retry` field to payment failed events

# 1.13.0

* add `retry_if_possible` field on payments, subscriptions and instalment_schedules

# 1.12.1

* Adds 3 additional fields on the creditors API

# 1.12.0

* Adds support for Instalment Schedules
* Exposed 'bounced' status on payouts

# 1.11.0

* Add fx_payout_currency to creditor
* Add fx to payment, payout and refund

# 1.10.0

* Addition of the customer removal API
* Support account_type in bank account API

# 1.9.0

* Add webhooks module for parsing webhook bodies.

# 1.8.0

* Add support for passing customer address fields to the Mandate PDFs
  creation endpoint.

# 1.7.0

* Add support for the new `app_fee` attribute returned by the Subscriptions API
* Improve the documentation of the Mandate PDFs API

# 1.6.0

* Add new [Mandate Imports API](https://developer.gocardless.com/api-reference/#core-endpoints-mandate-imports)

# 1.5.0 / 2018-04-11

* Add `mandate` to `Refund` links
* Add `mandate` to `PayoutItem` links
* Add `default_aud_payout_account` to `Creditor` links

# 1.4.0 / 2018-03-16

* Add `default_dkk_payout_account` to Creditor
* Add `danish_identity_number` to Customer

# 1.3.1 / 2017-12-04

* Fix README.rst for correct display on PyPI.

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
