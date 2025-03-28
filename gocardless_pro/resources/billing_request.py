# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class BillingRequest(object):
    """A thin wrapper around a billing_request, providing easy access to its
    attributes.

    Example:
      billing_request = client.billing_requests.get()
      billing_request.id
    """

    def __init__(self, attributes, api_response):
        self.attributes = attributes
        self.api_response = api_response

    @property
    def actions(self):
        return self.attributes.get('actions')
  

    @property
    def created_at(self):
        return self.attributes.get('created_at')
  

    @property
    def fallback_enabled(self):
        return self.attributes.get('fallback_enabled')
  

    @property
    def fallback_occurred(self):
        return self.attributes.get('fallback_occurred')
  

    @property
    def id(self):
        return self.attributes.get('id')
  

    @property
    def instalment_schedule_request(self):
        return self.InstalmentScheduleRequest(self.attributes.get('instalment_schedule_request'))
  

    @property
    def links(self):
        return self.Links(self.attributes.get('links'))
  

    @property
    def mandate_request(self):
        return self.MandateRequest(self.attributes.get('mandate_request'))
  

    @property
    def metadata(self):
        return self.attributes.get('metadata')
  

    @property
    def payment_request(self):
        return self.PaymentRequest(self.attributes.get('payment_request'))
  

    @property
    def purpose_code(self):
        return self.attributes.get('purpose_code')
  

    @property
    def resources(self):
        return self.Resources(self.attributes.get('resources'))
  

    @property
    def status(self):
        return self.attributes.get('status')
  

    @property
    def subscription_request(self):
        return self.SubscriptionRequest(self.attributes.get('subscription_request'))
  


  

  

  

  

  

  
    class InstalmentScheduleRequest(object):
        """Wrapper for the response's 'instalment_schedule_request' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def app_fee(self):
            return self.attributes.get('app_fee')
    
        @property
        def currency(self):
            return self.attributes.get('currency')
    
        @property
        def instalments_with_dates(self):
            return self.attributes.get('instalments_with_dates')
    
        @property
        def instalments_with_schedule(self):
            return self.attributes.get('instalments_with_schedule')
    
        @property
        def links(self):
            return self.attributes.get('links')
    
        @property
        def metadata(self):
            return self.attributes.get('metadata')
    
        @property
        def name(self):
            return self.attributes.get('name')
    
        @property
        def payment_reference(self):
            return self.attributes.get('payment_reference')
    
        @property
        def retry_if_possible(self):
            return self.attributes.get('retry_if_possible')
    
        @property
        def total_amount(self):
            return self.attributes.get('total_amount')
    
  

  
    class Links(object):
        """Wrapper for the response's 'links' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def bank_authorisation(self):
            return self.attributes.get('bank_authorisation')
    
        @property
        def creditor(self):
            return self.attributes.get('creditor')
    
        @property
        def customer(self):
            return self.attributes.get('customer')
    
        @property
        def customer_bank_account(self):
            return self.attributes.get('customer_bank_account')
    
        @property
        def customer_billing_detail(self):
            return self.attributes.get('customer_billing_detail')
    
        @property
        def instalment_schedule_request(self):
            return self.attributes.get('instalment_schedule_request')
    
        @property
        def instalment_schedule_request_instalment_schedule(self):
            return self.attributes.get('instalment_schedule_request_instalment_schedule')
    
        @property
        def mandate_request(self):
            return self.attributes.get('mandate_request')
    
        @property
        def mandate_request_mandate(self):
            return self.attributes.get('mandate_request_mandate')
    
        @property
        def organisation(self):
            return self.attributes.get('organisation')
    
        @property
        def payment_provider(self):
            return self.attributes.get('payment_provider')
    
        @property
        def payment_request(self):
            return self.attributes.get('payment_request')
    
        @property
        def payment_request_payment(self):
            return self.attributes.get('payment_request_payment')
    
        @property
        def subscription_request(self):
            return self.attributes.get('subscription_request')
    
        @property
        def subscription_request_subscription(self):
            return self.attributes.get('subscription_request_subscription')
    
  

  
    class MandateRequest(object):
        """Wrapper for the response's 'mandate_request' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def authorisation_source(self):
            return self.attributes.get('authorisation_source')
    
        @property
        def consent_type(self):
            return self.attributes.get('consent_type')
    
        @property
        def constraints(self):
            return self.attributes.get('constraints')
    
        @property
        def currency(self):
            return self.attributes.get('currency')
    
        @property
        def description(self):
            return self.attributes.get('description')
    
        @property
        def links(self):
            return self.attributes.get('links')
    
        @property
        def metadata(self):
            return self.attributes.get('metadata')
    
        @property
        def payer_requested_dual_signature(self):
            return self.attributes.get('payer_requested_dual_signature')
    
        @property
        def scheme(self):
            return self.attributes.get('scheme')
    
        @property
        def sweeping(self):
            return self.attributes.get('sweeping')
    
        @property
        def verify(self):
            return self.attributes.get('verify')
    
  

  

  
    class PaymentRequest(object):
        """Wrapper for the response's 'payment_request' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def amount(self):
            return self.attributes.get('amount')
    
        @property
        def app_fee(self):
            return self.attributes.get('app_fee')
    
        @property
        def currency(self):
            return self.attributes.get('currency')
    
        @property
        def description(self):
            return self.attributes.get('description')
    
        @property
        def funds_settlement(self):
            return self.attributes.get('funds_settlement')
    
        @property
        def links(self):
            return self.attributes.get('links')
    
        @property
        def metadata(self):
            return self.attributes.get('metadata')
    
        @property
        def reference(self):
            return self.attributes.get('reference')
    
        @property
        def scheme(self):
            return self.attributes.get('scheme')
    
  

  

  
    class Resources(object):
        """Wrapper for the response's 'resources' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def customer(self):
            return self.attributes.get('customer')
    
        @property
        def customer_bank_account(self):
            return self.attributes.get('customer_bank_account')
    
        @property
        def customer_billing_detail(self):
            return self.attributes.get('customer_billing_detail')
    
  

  

  
    class SubscriptionRequest(object):
        """Wrapper for the response's 'subscription_request' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def amount(self):
            return self.attributes.get('amount')
    
        @property
        def app_fee(self):
            return self.attributes.get('app_fee')
    
        @property
        def count(self):
            return self.attributes.get('count')
    
        @property
        def currency(self):
            return self.attributes.get('currency')
    
        @property
        def day_of_month(self):
            return self.attributes.get('day_of_month')
    
        @property
        def interval(self):
            return self.attributes.get('interval')
    
        @property
        def interval_unit(self):
            return self.attributes.get('interval_unit')
    
        @property
        def links(self):
            return self.attributes.get('links')
    
        @property
        def metadata(self):
            return self.attributes.get('metadata')
    
        @property
        def month(self):
            return self.attributes.get('month')
    
        @property
        def name(self):
            return self.attributes.get('name')
    
        @property
        def payment_reference(self):
            return self.attributes.get('payment_reference')
    
        @property
        def retry_if_possible(self):
            return self.attributes.get('retry_if_possible')
    
        @property
        def start_date(self):
            return self.attributes.get('start_date')
    
  

