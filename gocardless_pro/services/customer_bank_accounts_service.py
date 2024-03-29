# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class CustomerBankAccountsService(base_service.BaseService):
    """Service class that provides access to the customer_bank_accounts
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.CustomerBankAccount
    RESOURCE_NAME = 'customer_bank_accounts'


    def create(self,params=None, headers=None):
        """Create a customer bank account.

        Creates a new customer bank account object.
        
        There are three different ways to supply bank account details:
        
        - [Local details](#appendix-local-bank-details)
        
        - IBAN
        
        - [Customer Bank Account
        Tokens](#javascript-flow-create-a-customer-bank-account-token)
        
        For more information on the different fields required in each country,
        see [local bank details](#appendix-local-bank-details).

        Args:
              params (dict, optional): Request body.

        Returns:
              CustomerBankAccount
        """
        path = '/customer_bank_accounts'
        
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
  

    def list(self,params=None, headers=None):
        """List customer bank accounts.

        Returns a [cursor-paginated](#api-usage-cursor-pagination) list of your
        bank accounts.

        Args:
              params (dict, optional): Query string parameters.

        Returns:
              ListResponse of CustomerBankAccount instances
        """
        path = '/customer_bank_accounts'
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)
    
  

    def get(self,identity,params=None, headers=None):
        """Get a single customer bank account.

        Retrieves the details of an existing bank account.

        Args:
              identity (string): Unique identifier, beginning with "BA".
              params (dict, optional): Query string parameters.

        Returns:
              CustomerBankAccount
        """
        path = self._sub_url_params('/customer_bank_accounts/:identity', {
          
            'identity': identity,
          })
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def update(self,identity,params=None, headers=None):
        """Update a customer bank account.

        Updates a customer bank account object. Only the metadata parameter is
        allowed.

        Args:
              identity (string): Unique identifier, beginning with "BA".
              params (dict, optional): Request body.

        Returns:
              CustomerBankAccount
        """
        path = self._sub_url_params('/customer_bank_accounts/:identity', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {self._envelope_key(): params}

        response = self._perform_request('PUT', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def disable(self,identity,params=None, headers=None):
        """Disable a customer bank account.

        Immediately cancels all associated mandates and cancellable payments.
        
        This will return a `disable_failed` error if the bank account has
        already been disabled.
        
        A disabled bank account can be re-enabled by creating a new bank
        account resource with the same details.

        Args:
              identity (string): Unique identifier, beginning with "BA".
              params (dict, optional): Request body.

        Returns:
              CustomerBankAccount
        """
        path = self._sub_url_params('/customer_bank_accounts/:identity/actions/disable', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  
