import ast

from exceptions import OperationException
from exceptions import NumberFormatException


class Tokenizer:
    """
    Die Klasse zerlegt eine Eingabe (mathematischen Ausdruck) in die 3 Token
    - Zahl_1
    - Operation
    - Zahl_2

    Die zerlegten Token können über die Methoden
    - value1()
    - operation()
    - value2()
    ausgelesen werden.

    Die zulässigen Operationszeichen werden in einer Liste geführt. Über die Methode
    add_operation können weitere Operationszeichen zugefügt werden.
    Die entsprechenden Anpassungen sind dann aber auch in der Klasse Calculator sowie
    bei den abgeleiteten Klassen zu tätigen.
    """

    def __init__(self):
        self._value1 = None
        self._operation = None
        self._value2 = None
        #
        self._operations = ['+', '-', '*', '/']

    @property
    def value1(self):
        """
        Liefert die erste Zahl aus der Eingabe als float-Wert
        :return: 1. Zahl
        """
        return self._value1

    @property
    def value2(self):
        """
        Liefert die zweite Zahl aus der Eingabe als float-Wert
        :return: 2. Zahl
        """
        return self._value2

    @property
    def operation(self):
        """
        Liefert das Operationszeichen der Eingabe als String
        :return: Operationszeichen
        """
        return self._operation

    def add_operation(self, operation):
        """
        fügt der Liste der Operationen ein weiteres Zeichen zu.
        Die Methode prüft, ob das Zeichen bereits Teil der Liste ist. Wenn das Zeichen schon existiert,
        wird es nicht zugefügt.
        :param operation: Das Zeichen der Operation
        """
        if operation not in self._operations:
            self._operations.append(operation)
        else:
            print(f'Zeichen {operation} ist schon Teil der Liste')

    def get_all_operations(self):
        """
        liefert die Liste aller Operationen.
        Diese Methode dient Testzwecken.
        """
        return self._operations

    def split(self, command_line):
        """
        Zerlegt den String aufgrund des Vorkommens von Operationszeichen aus der Liste.
        Fehlt das Operationszeichen, weird eine OperationException geworfen.
        Ist ein Zahlenwert ungültig, wird eine NumberFormatException geworfen.
        :param command_line: Eingabe des Benutzers
        """
        # prüfen, ob ein gültiges Operationszeichen im String erkannt wird. Dazu die Liste aller Zeichen
        # abarbeiten. Wenn das Zeichen nicht erkannt wird, wird eine Exception erzeugt.
        for sign in self._operations:
            if sign in command_line:
                # die Zeichenkette entlang der Operationszeichen auftrennen
                elements = command_line.partition(sign)
                self._operation = sign
                # sicherstellen, dass es sich um gültige Zahlenwerte handelt
                try:
                    self._value1 = ast.literal_eval(elements[0].strip())
                except Exception:
                    raise NumberFormatException(elements[0])
                try:
                    self._value2 = ast.literal_eval(elements[2].strip())
                except Exception:
                    raise NumberFormatException(elements[2])
                return
        # es wurde kein Operationszeichen gefunden
        raise OperationException()


# TEST
if __name__ == '__main__':
    t = Tokenizer()
    print(t.get_all_operations())
    t.add_operation('+')
    t.add_operation('^')
    print(t.get_all_operations())
    try:
        t.split('3.25/7.568')
        #
        print(t.value1)
        print(t.operation)
        print(t.value2)
    except OperationException as exception:
        print(exception)
    except NumberFormatException as exception:
        print(exception)
