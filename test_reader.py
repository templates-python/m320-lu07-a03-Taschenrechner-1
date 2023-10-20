from unittest.mock import patch

from reader import Reader  # Annahme: Deine Reader-Klasse ist in einer Datei namens reader.py


class TestReader:
    # Testet, ob die Singleton-Implementierung funktioniert
    def test_singleton_instance(self):
        reader1 = Reader()
        reader2 = Reader()
        assert reader1 is reader2

    #    Testet die Ausgabe der screen_info-Methode
    def test_screen_info(self, capsys):
        reader = Reader()
        reader.screen_info()
        captured = capsys.readouterr()
        assert 'Geben Sie eine Rechnung in der Form 5 + 7 ein.' in captured.out

    # Testet die Eingabe mit einer Mock-Implementierung
    @patch('builtins.input', return_value='5 + 7')
    def test_read(self, mock_input):
        reader = Reader()
        user_input = reader.read()
        assert user_input == '5 + 7'

    # Testet die Eingabe von Leerzeichen und Zeilenumbrüchen
    @patch('builtins.input', return_value='  \n')
    def test_read_empty_input(self, mock_input):
        reader = Reader()
        user_input = reader.read()
        assert user_input == '  \n'

    # Testet die Eingabe von Zeichenketten mit Leerzeichen
    @patch('builtins.input', return_value='   Hello   ')
    def test_read_string_input(self, mock_input):
        reader = Reader()
        user_input = reader.read()
        assert user_input == '   Hello   '
