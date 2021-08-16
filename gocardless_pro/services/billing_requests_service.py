# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class BillingRequestsService(base_service.BaseService):
    """Service class that provides access to the billing_requests
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.BillingRequest
    RESOURCE_NAME = 'billing_requests'


    def list(self,params=None, headers=None):
        """List Billing Requests.

        Returns a [cursor-paginated](#api-usage-cursor-pagination) list of your
        billing_requests.

        Args:
              params (dict, optional): Query string parameters.

        Returns:
              BillingRequest
        """
        path = '/billing_requests'
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)
    
  

    def create(self,params=None, headers=None):
        """Create a billing_request.

        

        Args:
              params (dict, optional): Request body.

        Returns:
              ListResponse of BillingRequest instances
        """
        path = '/billing_requests'
        
        if params is not None:
            params = {self._envelope_key(): params}

        try:
          response = self._perform_request('POST', path, params, headers,
                                            retry_failures=True)
        except errors.IdempotentCreationConflictError as err:
          if self.raise_on_idempotency_conflict:
            raise err
          return self.get(identity=err.conflicting_resource_id,
                          params=params,
                          headers=headers)
        return self._resource_for(response)
  

    def get(self,identity,params=None, headers=None):
        """Get a single billing request.

        Fetches a billing request

        Args:
              identity (string): Unique identifier, beginning with "BRQ".
              params (dict, optional): Query string parameters.

        Returns:
              ListResponse of BillingRequest instances
        """
        path = self._sub_url_params('/billing_requests/:identity', {
          
            'identity': identity,
          })
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def collect_customer_details(self,identity,params=None, headers=None):
        """Collect customer details for the billing request.

        If the billing request has a pending
        <code>collect_customer_details</code>
        action, this endpoint can be used to collect the details in order to
        complete it.
        
        The endpoint takes the same payload as Customers, but checks that the
        customer fields are populated correctly for the billing request scheme.
        
        Whatever is provided to this endpoint is used to update the referenced
        customer, and will take effect immediately after the request is
        successful.

        Args:
              identity (string): Unique identifier, beginning with "BRQ".
              params (dict, optional): Request body.

        Returns:
              ListResponse of BillingRequest instances
        """
        path = self._sub_url_params('/billing_requests/:identity/actions/collect_customer_details', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  

    def collect_bank_account(self,identity,params=None, headers=None):
        """Collect bank account details for the billing request.

        If the billing request has a pending
        <code>collect_bank_account</code> action, this endpoint can be
        used to collect the details in order to complete it.
        
        The endpoint takes the same payload as Customer Bank Accounts, but
        check
        the bank account is valid for the billing request scheme before
        creating
        and attaching it.

        Args:
              identity (string): Unique identifier, beginning with "BRQ".
              params (dict, optional): Request body.

        Returns:
              ListResponse of BillingRequest instances
        """
        path = self._sub_url_params('/billing_requests/:identity/actions/collect_bank_account', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  

    def fulfil(self,identity,params=None, headers=None):
        """Fulfil a billing request.

        If a billing request is ready to be fulfilled, call this endpoint to
        cause
        it to fulfil, executing the payment.

        Args:
              identity (string): Unique identifier, beginning with "BRQ".
              params (dict, optional): Request body.

        Returns:
              ListResponse of BillingRequest instances
        """
        path = self._sub_url_params('/billing_requests/:identity/actions/fulfil', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  

    def confirm_payer_details(self,identity,params=None, headers=None):
        """Confirm the customer and bank_account details.

        This is needed when you have mandate_request. As a scheme compliance
        rule we are required to
        allow the payer to crosscheck the details entered by them and confirm
        it.

        Args:
              identity (string): Unique identifier, beginning with "BRQ".
              params (dict, optional): Request body.

        Returns:
              ListResponse of BillingRequest instances
        """
        path = self._sub_url_params('/billing_requests/:identity/actions/confirm_payer_details', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  

    def cancel(self,identity,params=None, headers=None):
        """Cancel a billing request.

        Immediately cancels a billing request, causing all billing request
        flows
        to expire.

        Args:
              identity (string): Unique identifier, beginning with "BRQ".
              params (dict, optional): Request body.

        Returns:
              ListResponse of BillingRequest instances
        """
        path = self._sub_url_params('/billing_requests/:identity/actions/cancel', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  

    def notify(self,identity,params=None, headers=None):
        """Notify the customer of a billing request.

        Notifies the customer linked to the billing request, asking them to
        authorise it.
        Currently, the customer can only be notified by email.

        Args:
              identity (string): Unique identifier, beginning with "BRQ".
              params (dict, optional): Request body.

        Returns:
              ListResponse of BillingRequest instances
        """
        path = self._sub_url_params('/billing_requests/:identity/actions/notify', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  
