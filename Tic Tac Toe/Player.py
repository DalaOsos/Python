class Player:
    def __init__(self):
        self.__name = ''
        self.__symbol = ''

    def choose_name(self):
        while True:
            name = input("Please Enter your name (letters only) : ")
            if name.isalpha():
                self.__name = name
                break
            else:
                print('INVALID NAME : Please Enter Letter Only.')

    def choose_symbol(self):
        while True:
            symbol = input(f"Please {self.__name} Enter Your Choice from (O / X) : ")
            if symbol.upper() == 'X' or symbol.upper() == 'O':
                self.__symbol = symbol.upper()
                break
            else:
                print("INVALID INPUT : Choose One of (O / X) Symbol...")

    def get_name(self):
        return self.__name

    def get_symbol(self):
        return self.__symbol
