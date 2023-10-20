import pytest

from exceptions import OperationException, NumberFormatException
from tokenizer import Tokenizer  # Annahme: Deine Tokenizer-Klasse ist in einer Datei namens tokenizer.py


class TestTokenizer:

    @pytest.fixture
    def tokenizer(self):
        return Tokenizer()

    def test_initial_values(self, tokenizer):
        assert tokenizer.value1 is None
        assert tokenizer.value2 is None
        assert tokenizer.operation is None

    def test_get_all_operations(self, tokenizer):
        assert tokenizer.get_all_operations() == ['+', '-', '*', '/']

    def test_add_operation(self, tokenizer):
        tokenizer.add_operation('%')
        assert tokenizer.get_all_operations() == ['+', '-', '*', '/', '%']

    def test_add_duplicate_operation(self, tokenizer, capsys):
        tokenizer.add_operation('+')  # Trying to add a duplicate operation
        captured = capsys.readouterr()
        assert 'Zeichen + ist schon Teil der Liste\n' in captured.out

    def test_split_valid_input(self):
        tokenizer = Tokenizer()
        tokenizer.split('5 + 7')
        assert tokenizer.value1 == 5
        assert tokenizer.operation == '+'
        assert tokenizer.value2 == 7

    def test_split_invalid_operation(self):
        tokenizer = Tokenizer()
        with pytest.raises(OperationException):
            tokenizer.split('5 ? 7')  # Using an invalid operation

    def test_split_invalid_number(self):
        tokenizer = Tokenizer()
        with pytest.raises(NumberFormatException):
            tokenizer.split('5 + abc')  # Using an invalid number
