from reader          import Reader
from math_operations import *
from tokenizer       import Tokenizer
from exceptions      import OperationException, NumberFormatException


class Calculator:

    def __init__(self, tokenizer_object):
        """
        Erzeugen des Reader-Objekts und zuweisen des Tokenizers.
        Zudem wird die Referenz für das MathOp-Objekt mit None initialisiert.
        """
        self._math_op = None
        self._my_reader = Reader()
        self._tokenizer = tokenizer_object

    @property
    def math_op(self):
        """
        Liefert die Referenz des aktuell erstellten MathOp-Objekts
        """
        return self._math_op

    def read_input(self):
        """
        Wert von der Tastatur einlesen und den String dem Splitter zur
        Auftrennung übergeben.
        Die anfallenden Exceptions werden erst im Hauptprogramm verarbeitet!
        """
        # Eingabe für eine Rechnung realisieren....
        self._my_reader.screen_info()
        value = self._my_reader.read()
        # ...und splitten. Hier die möglichen Fehlerfälle, die beim Tokenizer anfallen können, abfangen.
        self._tokenizer.split(value)



    def create_concrete_op(self):
        """
        Anhand des Operationszeichens wird zur Laufzeit die konkrete
        Operation festgelegt und das entsprechende Objekt erzeugt.
        Sollte das Operationszeichen nicht erkannt werden, wird die
        Referenz auf None gesetzt.
        Anmerkung: Dieser Fall sollte nie auftreten, da der Tokenizer
        sonst eine Exception wirft. Aber zur Sicherheit soll das so
        realisiert werden.
        """
        if self._tokenizer.operation == '+':
            self._math_op = Adder()
        elif self._tokenizer.operation == '-':
            self._math_op = Subtractor()
        elif self._tokenizer.operation == '*':
            self._math_op = Multiplier()
        elif self._tokenizer.operation == '/':
            self._math_op = Divider()
        elif self._tokenizer.operation == '^':
            self._math_op = Exposer()
        else:
            self._math_op = None

    def calculate(self):
        """
        Ausführen der in create_concrete_op erzeugten Operation.
        Hinweis: Es werden keine Exceptions bearbeitet.
        """
        if self._math_op != None:
            self._math_op.execute_op(self._tokenizer.value1, self._tokenizer.value2)
            print(f'Ergebnis: {self._math_op.result}')

