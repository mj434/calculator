"""Calculation history class"""
from calculator.calculations.addition import Addition
from calculator.calculations.subtraction import Subtraction
from calculator.calculations.multiplication import Multiplication
from calculator.calculations.division import Division
class Calculations:
    """manages history of calculations"""
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clears history of calculations"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """count number of items in history"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation_object():
        """get last calculation"""
        if len(Calculations.history) > 0:
            return Calculations.history[-1]
        return 0
    @staticmethod
    def get_last_calculation_result_value():
        """get last calculation"""
        calculation = Calculations.get_last_calculation_object()
        if calculation == 0:
            return 0
        return calculation.get_result()
    @staticmethod
    def get_first_calculation():
        """get first calculation"""
        return Calculations.history[0]
    @staticmethod
    def get_calculation(num):
        """get a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """get a calculation from history"""
        return Calculations.history.append(calculation)
    @staticmethod
    def add_addition_calculation(values):
        """create addition and add object to history"""
        Calculations.add_calculation(Addition.create(values))
        return True
    @staticmethod
    def add_subtraction_calculation(values):
        """create a subtraction object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return True
    @staticmethod
    def add_division_calculation(values):
        """Add a division object to history using create"""
        Calculations.add_calculation(Division.create(values))
        return True