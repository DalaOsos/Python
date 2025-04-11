class Menu:
    def Display_Main_Menu(self):
        text = """

        Welcome In Tic Tac Toe Game

        1 - Start Game
        2 - Quit Game

        Enter Your choice one of both...
        """
        choice = input(text)
        return choice

    def Display_End_Game(self):
        text = """

        .....Game Over.....

        1- Restart Game
        2- End Game

        Enter Your Choice one of both...
        """
        choice = input(text)
        return choice
