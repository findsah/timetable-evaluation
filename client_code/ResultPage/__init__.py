from ._anvil_designer import ResultPageTemplate
from anvil import *

class ResultPage(ResultPageTemplate):
    def __init__(self, result, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Display the result in a label or handle it as needed
        self.label_result.text = result

    def link_1_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form("WelcomePage")

    def link_2_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('ContactUsPage')
