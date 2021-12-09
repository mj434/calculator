"""multiplication class"""
from calculator.calculations.calculation import Calculation

class Multiplication(Calculation):
    """calculation multiplication class"""
    def get_result(self):
        """get the multiplication results"""
        result = 1.0
        for value in self.values:
            result = result * value
        return result
