# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class MandateImport(object):
    """A thin wrapper around a mandate_import, providing easy access to its
    attributes.

    Example:
      mandate_import = client.mandate_imports.get()
      mandate_import.id
    """

    def __init__(self, attributes, api_response):
        self.attributes = attributes
        self.api_response = api_response

    @property
    def created_at(self):
        return self.attributes.get('created_at')
  

    @property
    def id(self):
        return self.attributes.get('id')
  

    @property
    def links(self):
        return self.Links(self.attributes.get('links'))
  

    @property
    def scheme(self):
        return self.attributes.get('scheme')
  

    @property
    def status(self):
        return self.attributes.get('status')
  


  

  

  
    class Links(object):
        """Wrapper for the response's 'links' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def creditor(self):
            return self.attributes.get('creditor')
    
  

  

  

