"""division class"""
from calculator.calculations.calculation import Calculation

class Division(Calculation):
    """division calculation class"""
    def get_result(self):
        """getting division results"""
        divided_values = 1.0

        for value in self.values:
            if value == 0.0:
                return "Error, can't divide by 0"
            divided_values = divided_values / value
        return divided_values
