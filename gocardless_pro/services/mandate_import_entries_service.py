# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class MandateImportEntriesService(base_service.BaseService):
    """Service class that provides access to the mandate_import_entries
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.MandateImportEntry
    RESOURCE_NAME = 'mandate_import_entries'


    def create(self,params=None, headers=None):
        """Add a mandate import entry.

        For an existing [mandate import](#core-endpoints-mandate-imports), this
        endpoint can
        be used to add individual mandates to be imported into GoCardless.
        
        You can add no more than 30,000 rows to a single mandate import.
        If you attempt to go over this limit, the API will return a
        `record_limit_exceeded` error.

        Args:
              params (dict, optional): Request body.

        Returns:
              MandateImportEntry
        """
        path = '/mandate_import_entries'
        
        if params is not None:
            params = {self._envelope_key(): params}

        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def list(self,params=None, headers=None):
        """List all mandate import entries.

        For an existing mandate import, this endpoint lists all of the entries
        attached.
        
        After a mandate import has been submitted, you can use this endpoint to
        associate records
        in your system (using the `record_identifier` that you provided when
        creating the
        mandate import).
        

        Args:
              params (dict, optional): Query string parameters.

        Returns:
              ListResponse of MandateImportEntry instances
        """
        path = '/mandate_import_entries'
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)
    
  
