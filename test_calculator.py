import pytest

from calculator import Calculator
from exceptions import *
from math_operations import *
from tokenizer import Tokenizer


class TestCalculator:

    @pytest.fixture
    def tokenizer(self):
        return Tokenizer()

    @pytest.fixture
    def calculator(self, tokenizer):
        return Calculator(tokenizer)

    def test_object_creation_adder(self, calculator, tokenizer):
        tokenizer.split('2+5')
        calculator.create_concrete_op()
        assert isinstance(calculator.math_op, Adder)

    def test_object_creation_subtractor(self, calculator, tokenizer):
        tokenizer.split('2-5')
        calculator.create_concrete_op()
        assert isinstance(calculator.math_op, Subtractor)

    def test_object_creation_multiplier(self, calculator, tokenizer):
        tokenizer.split('2*5')
        calculator.create_concrete_op()
        assert isinstance(calculator.math_op, Multiplier)

    def test_object_creation_divider(self, calculator, tokenizer):
        tokenizer.split('2/5')
        calculator.create_concrete_op()
        assert isinstance(calculator.math_op, Divider)

    def test_read_input_valid_input(self, calculator, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '10 + 5')
        calculator.read_input()
        assert calculator._tokenizer.value1 == 10
        assert calculator._tokenizer.value2 == 5
        assert calculator._tokenizer.operation == '+'

    def test_read_input_invalid_operation(self, calculator, monkeypatch):
        #with pytest.raises(OperationException):
        monkeypatch.setattr('builtins.input', lambda _: '10 % 5')
        try:
            calculator.read_input()
            assert False
        except OperationException:
            assert True


    def test_read_input_invalid_number(self, calculator, monkeypatch):
        with pytest.raises(NumberFormatException):
            monkeypatch.setattr('builtins.input', lambda _: '10 + abc')
            calculator.read_input()

    def test_calculator_valid_division(self, calculator, tokenizer):
        tokenizer.split('10/5')
        calculator.create_concrete_op()
        calculator.calculate()
        assert calculator.math_op.result == 2

    def test_calculator_invalid_division(self, calculator, tokenizer):
        with pytest.raises(ZeroDivisionError):
            tokenizer.split('10/0')
            calculator.create_concrete_op()
            calculator.calculate()
