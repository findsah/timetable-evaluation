from ._anvil_designer import QuestionPageTemplate
from anvil import *
import anvil.server

from ..WelcomePage import WelcomePage
from ..ResultPage import ResultPage

class QuestionPage(QuestionPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def radio_button_2_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form(WelcomePage())

  def button_1_click(self, **event_args):
    f1 = self.text_box_1.text
    result = anvil.server.call('GetCustomerInfo', 1, 2)
    self.text_box_1.text = result
    """This method is called when the button is clicked"""
    open_form(ResultPage())
