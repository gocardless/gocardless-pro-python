# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class RedirectFlowsService(base_service.BaseService):
    """Service class that provides access to the redirect_flows
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.RedirectFlow
    RESOURCE_NAME = 'redirect_flows'


    def create(self,params=None, headers=None):
        """Create a redirect flow.

        Creates a redirect flow object which can then be used to redirect your
        customer to the GoCardless hosted payment pages.

        Args:
              params (dict, optional): Request body.

        Returns:
              RedirectFlow
        """
        path = '/redirect_flows'
        
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
        """Get a single redirect flow.

        Returns all details about a single redirect flow

        Args:
              identity (string): Unique identifier, beginning with "RE".
              params (dict, optional): Query string parameters.

        Returns:
              RedirectFlow
        """
        path = self._sub_url_params('/redirect_flows/:identity', {
          
            'identity': identity,
          })
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def complete(self,identity,params=None, headers=None):
        """Complete a redirect flow.

        This creates a [customer](#core-endpoints-customers), [customer bank
        account](#core-endpoints-customer-bank-accounts), and
        [mandate](#core-endpoints-mandates) using the details supplied by your
        customer and returns the ID of the created mandate.
        
        This will return a `redirect_flow_incomplete` error if your customer
        has not yet been redirected back to your site, and a
        `redirect_flow_already_completed` error if your integration has already
        completed this flow. It will return a `bad_request` error if the
        `session_token` differs to the one supplied when the redirect flow was
        created.

        Args:
              identity (string): Unique identifier, beginning with "RE".
              params (dict, optional): Request body.

        Returns:
              RedirectFlow
        """
        path = self._sub_url_params('/redirect_flows/:identity/actions/complete', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  
