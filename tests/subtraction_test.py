"""testing subtraction"""
from calculator.calculations.subtraction import Subtraction

def test_calculation_subtraction():
    """testing that our calculator has a static subtraction method"""
    mynumbers = (1.0,2.0)
    subtraction = Subtraction(mynumbers)
    assert subtraction.get_result() == -3.0
