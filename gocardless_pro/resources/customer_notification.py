# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class CustomerNotification(object):
    """A thin wrapper around a customer_notification, providing easy access to its
    attributes.

    Example:
      customer_notification = client.customer_notifications.get()
      customer_notification.id
    """

    def __init__(self, attributes, api_response):
        self.attributes = attributes
        self.api_response = api_response

    @property
    def action_taken(self):
        return self.attributes.get('action_taken')
  

    @property
    def action_taken_at(self):
        return self.attributes.get('action_taken_at')
  

    @property
    def action_taken_by(self):
        return self.attributes.get('action_taken_by')
  

    @property
    def id(self):
        return self.attributes.get('id')
  

    @property
    def links(self):
        return self.Links(self.attributes.get('links'))
  

    @property
    def type(self):
        return self.attributes.get('type')
  


  

  

  

  

  
    class Links(object):
        """Wrapper for the response's 'links' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def customer(self):
            return self.attributes.get('customer')
    
        @property
        def event(self):
            return self.attributes.get('event')
    
        @property
        def mandate(self):
            return self.attributes.get('mandate')
    
        @property
        def payment(self):
            return self.attributes.get('payment')
    
        @property
        def refund(self):
            return self.attributes.get('refund')
    
        @property
        def subscription(self):
            return self.attributes.get('subscription')
    
  

  
