from calculator import Calculator
from exceptions import *
from tokenizer import Tokenizer


def main():
    """
    Der Taschenrechner.
    Hier werden alle anfallenden Exceptions der Calculator-Klasse
    verarbeitet.
    """
    calc = Calculator(Tokenizer())
    try:
        calc.read_input()
        calc.create_concrete_op()
        calc.calculate()
    except OperationException as op_ex:
        print(op_ex)
    except NumberFormatException as nf_ex:
        print(nf_ex)
    except ZeroDivisionError as error:
        print('ERROR: Division mit 0!')


if __name__ == '__main__':
    main()
