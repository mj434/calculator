"""subtraction class"""
import pprint

from calculator.calculations.calculation import Calculation

class Subtraction(Calculation):
    """subtraction calculation"""
    def get_result(self):
        """subtraction results"""
        difference_of_values = 0.0
        for value in self.values:
            difference_of_values = difference_of_values - value
            pprint.pprint(value)
        return difference_of_values
