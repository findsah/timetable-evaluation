# _anvil_designer.py
import random
from ._anvil_designer import ResultPageTemplate
from anvil import *

class ResultPage(ResultPageTemplate):
    def __init__(self, result, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Evaluate the result and display it
        evaluated_result = self.evaluate_result(result)
        self.label_result.text = evaluated_result

    def link_1_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form("WelcomePage")

    def link_2_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('ContactUsPage')

    def evaluate_result(self, result):
        # Evaluate the result and return the corresponding label
        # You can modify this logic based on your evaluation criteria

        # For demonstration purposes, let's consider a random evaluation
        labels = ["Very Easy", "Moderate", "Hard"]
        evaluated_label = random.choice(labels)

        return f"The result is {evaluated_label}"
