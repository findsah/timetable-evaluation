from ._anvil_designer import QuestionPageTemplate
from anvil import *

from ..WelcomePage import WelcomePage

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
    self.content_panel.clear()
    self.content_panel.add_component(WelcomePage())

