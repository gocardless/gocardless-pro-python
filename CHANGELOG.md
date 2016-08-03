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
