from ._anvil_designer import ContactUsPageTemplate
from anvil import *
import anvil.server

from ..WelcomePage import WelcomePage

class ContactUsPage(ContactUsPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
