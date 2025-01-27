<!-- @format -->
# 2.2.0

- Added `status` filter parameter to Mandate Import Entries.
- Added `processing_errors` response field to Mandate Import Entry.

# 2.1.0

- Added `mandate_request[consent_type]` parameter to Billing Request creation.
- Added `constraints[payment_method]` parameter to Billing Request creation.
- Added `subscription_request` parameter to Billing Request creation.
- Added `instalment_schedule_request` parameter to Billing Request creation.

# 1.53.0

- Added `/exports` APIs and added `exports` as a new event type available for Embed merchants

# 1.52.0

- Added new endpoints `/branding/logos` and `/branding/payer_themes` available for Embed merchants

# 1.51.0

- Added `payer_requested_dual_signature` field for Billing Request Confirmation endpoint.
  
# 1.50.0

- Added `payment[faster_ach]` parameter to Payment creation.
- Added `payment[faster_ach]` response field to Payment responses.
- Added `mandate[next_possible_standard_ach_charge_date]` response field to Mandate responses.

# 1.49.0

- Expose the GET `/transferred_mandates` endpoint

# 1.48.0

- Added a new field `verification_status` to creditor_bank_accounts API's response

# 1.47.0

- Add rate limit response headers as properties on the client

# 1.46.2

- Remove nose in favour of pytest
- Remove inaccessible MandateRequestConstraints resource

# 1.46.1

- Fix throwing error on empty 204 responses

# 1.46.0

- Added refund_funds_returned to payout item types
- Added funds_settlement to the mandate model

# 1.45.0

- Added request_pointer to validation errors

# 1.44.0
- Update pagination definition (non-functional change)
# 1.43.0

- Added a new field, links[creditor] to the scheme identifier create API
- Added a new API to set and retrieve negative balances
- Added a new bank_reference_prefix to the creditor API
- Removed the bank_redirect field from the institutions API
- Added an autocompletes_collect_bank_account field to the institutions API
- Removed the creditor API endpoint to apply scheme identifiers

# 1.42.0

- Added `country_code` as a required parameter to the List Institutions for Billing Request API.

# 1.40.0

- Added `show_success_redirect_button` in the Billing Request Flow model.

# 1.39.0

- Adding GET `/verification_details` endpoint to allow integrators to list verification details for a creditor

# 1.38.0

- Adding POST `/verification_details` endpoint to allow integrators to submit information against creditors for KYC checks

- Expose scheme identifiers for CREATE/GET/LIST via the API and allow them to be applied to creditors via the `/creditors/:identity/actions/apply_scheme_identifier` route added

# 1.37.0

- Added background conversion of boolean values to string values in GET requests

# 1.36.1

- Added `authorisation_source` parameter to the Mandate creation API and `mandate_request[authourisation_source]` parameter to the BillingRequest creation API. This field is required for offline mandates.

# 1.36.0

- Added `authorisation_source` parameter to the Mandate creation API and `mandate_request[authourisation_source]` parameter to the BillingRequest creation API. This field is required for offline mandates.

# 1.34.0

- Added `language` parameter to [Billing Request Flow](https://developer.gocardless.com/api-reference#billing-request-flows-create-a-billing-request-flow) creation.

# 1.33.0

- Added `mandate_request[description]` and `mandate_request[constraints]` parameters to Billing Request creation
- Added `consent_parameters` to mandate

# 1.32.0

- Added support for `prefilled_customer` and `prefilled_bank_account` in Billing Request Flow

# 1.31.0

- Added `reference` field to Mandate Request in Billing Request

# 1.30.0

- Initial support for PayTo

# 1.29.0

- Added `ip_address` to `customer_billing_detail` property in Billing Request.

# 1.28.0

- Added support for billing request fallbacks

# 1.27.0

- Release Block API

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
