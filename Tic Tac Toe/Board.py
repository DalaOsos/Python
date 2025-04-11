class Board:
    def __init__(self):
        self.__board = [str(i) for i in range(1, 10)]

    def Display_Board(self):
        for i in range(0, 9, 3):
            print(('|'.join(self.__board[i:i + 3])))
            if i < 6:
                print('-' * 5)

    def Update_board(self,Choice,symbol):
        if self.Is_Valid_Move(Choice):
            self.__board[Choice-1] = symbol
            return True
        return False

    def Is_Valid_Move(self,Choice):
        return self.__board[Choice-1].isdigit()

    def reset_board(self):
        self.__board = [str(i) for i in range(1, 10)]

    def get_board(self):
        return self.__board
