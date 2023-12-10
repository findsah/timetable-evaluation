from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

from ..WelcomePage import WelcomePage
from ..ResultPage import ResultPage
from ..ContactUsPage import ContactUsPage

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('WelcomePage')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('ContactUsPage')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
