class Reader:
    """
    Die Klasse dient dem Einlesen einer Eingabe. Sie ist als Singleton ausgelegt, da die
    Eingabe (Tastatur) ein Device darstellt, das physisch einmal vorhanden ist.
    """

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Reader, cls).__new__(cls)
        return cls._instance

    def screen_info(self):
        """
        Benutzerhinweis für die Eingabe.
        """
        print(f'Geben Sie eine Rechnung in der Form 5 + 7 ein. \nFühren Sie die Berechnung mit <ENTER> aus.')

    def read(self):
        """
        Einlesen der Benutzereingabe (als String)
        """
        return input('Eingabe: ')


# TEST
if __name__ == '__main__':
    reader = Reader()
    reader.screen_info()
    value = reader.read()
    print(value)
