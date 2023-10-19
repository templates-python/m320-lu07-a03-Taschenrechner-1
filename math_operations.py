from abc import ABC, abstractmethod


from abc import ABC, abstractmethod


class MathOp(ABC):
    """
    Eine abstrakte Klasse, die eine beliebige (binäre) mathematische Operation repräsentiert.
    Die Methode execute_op wird abstrakt implementiert und muss durch konkrete Klassen überschrieben werden.
    Die Methode result liefert das Ergebnis der ausgeführten Operation.
    Hinweis: unäre Operationen wie z.B. die Fakultät (!) können nicht berechnet werden.
    """

    def __init__(self):
        """
        Initialisiert den Ergebniswert.
        """
        self._result = 0.0

    @abstractmethod
    def execute_op(self, val1, val2):
        """
        Definiert die Schnittstelle für die Berechnung einer binären Operation (Operation mit 2 Werten).
        Die Methode erhält als Parameter zwei Werte und führt dann die passende Operation aus. Die konkrete
        Operation wird in der abgeleiteten Klasse festgelegt.
        :param val1: erster Zahlenwert
        :param val2: zweiter Zahlenwert
        """
        pass

    @property
    def result(self):
        """
        Liefert das Ergebnis der mathematischen Operation.
        :return:
        """
        return self._result


class Adder(MathOp):
    """
    Addiert zwei Zahlen.
    """
    def execute_op(self, val1, val2):
        """
        Führt die Operation val1 + val2 aus.
        Das Ergebnis kann über die getter-Methode von result gelesen werden.
        :param val1: erster Zahlenwert
        :param val2: zweiter Zahlenwert
        """
        self._result = val1 + val2


class Subtractor(MathOp):
    """
    Subtrahiert zwei Zahlen.
    """
    def execute_op(self, val1, val2):
        """
        Führt die Operation val1 - val2 aus.
        Das Ergebnis kann über die getter-Methode von result gelesen werden.
        :param val1: erster Zahlenwert
        :param val2: zweiter Zahlenwert
        """
        self._result = val1 - val2


class Multiplier(MathOp):
    """
    Multipliziert zwei Zahlen.
    """

    def execute_op(self, val1, val2):
        """
        Führt die Operation val1 * val2 aus.
        Das Ergebnis kann über die getter-Methode von result gelesen werden.
        :param val1: erster Zahlenwert
        :param val2: zweiter Zahlenwert
        """
        self._result = val1 * val2


class Divider(MathOp):
    """
    Dividiert zwei Zahlen.
    Es muss sichergestellt sein, dass der Dividend nicht 0 ist!
    """

    def execute_op(self, val1, val2):
        """
        Führt die Operation val1 / val2 aus.
        Das Ergebnis kann über die getter-Methode von result gelesen werden.
        Wird als Divisor der Wert 0 geliefert, wird ein ZeroDivisionError ausgelöst.
        :param val1: erster Zahlenwert
        :param val2: zweiter Zahlenwert
        """
        if val2 != 0:
            self._result = val1 / val2
        else:
            raise ZeroDivisionError()