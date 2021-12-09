"""Testing the calculator"""
import pytest
from calculator.calculator import Calculator
from calculator.history.calculations import Calculations

@pytest.fixture
def clear_history_fixture():
    """runs each time you pass it to a test"""
    #pylint: disable=redefined-outer-name
    Calculations.clear_history()

def test_initial_result(clear_history_fixture):
    """testing initial calculator result is 0"""
    # pylint: disable=redefined-outer-name, unused-argument
    calc = Calculator()
    assert calc.get_last_result_value() == 0

def test_calculator_add_static(clear_history_fixture):
    """testing static add method"""
    # pylint: disable=unused-argument,redefined-outer-name
    calc = Calculator()
    calc.add_numbers((1.0,2.0,4.0,5.0))
    assert calc.get_last_result_value() == 12.0

def test_calculator_subtract_static(clear_history_fixture):
    """testing static subtracting method"""
    # pylint: disable=unused-argument,redefined-outer-name
    calc = Calculator()
    calc.subtract_numbers((2.0,3.0,2.0))
    assert calc.get_last_result_value() == -7.0

def test_calculator_multiply_static(clear_history_fixture):
    """testing static multiplication method"""
    # pylint: disable=unused-argument,redefined-outer-name
    calc = Calculator()
    calc.multiply_numbers((2.0,3.0,5.0))
    assert calc.get_last_result_value() == 30.0

def test_calculator_divide_static(clear_history_fixture):
    """testing static division method"""
    # pylint: disable=unused-argument,redefined-outer-name
    calc = Calculator()
    calc.divide_numbers((1.0,2.0))
    assert calc.get_last_result_value() == 0.5
