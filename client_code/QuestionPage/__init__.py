from ._anvil_designer import QuestionPageTemplate
from anvil import *
import anvil.server

from ..WelcomePage import WelcomePage
from ..ResultPage import ResultPage
from ..ContactUsPage import ContactUsPage

class QuestionPage(QuestionPageTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def radio_button_2_clicked(self, **event_args):
        """This method is called when this radio button is selected"""
        pass

    def link_1_click(self, **event_args):
        open_form('WelcomePage')

    def button_1_click(self, **event_args):
        # Get the user's responses
        response1 = self.text_box_1.text
        response2 = self.text_box_2.text
        response3 = self.text_box_2.text  # Fix the typo here

        # Call the Anvil server function to send responses to Jupyter notebook
        result = anvil.server.call('predict_result', response1, response2, response3)

        # Create an instance of the ResultPage form
        result_form = ResultPage(result=result)

        # Open the ResultPage form
        open_form(result_form)

    def link_2_click(self, **event_args):
        open_form('ContactUsPage')

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        pass
