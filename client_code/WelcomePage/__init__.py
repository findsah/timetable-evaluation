from ._anvil_designer import WelcomePageTemplate
from anvil import *

class WelcomePage(WelcomePageTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Open the QuestionPage when the WelcomePage is initialized
        open_form('QuestionPage')

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form("QuestionPage")

    def link_1_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('ContactUsPage')

    def link_2_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('QuestionPage')
