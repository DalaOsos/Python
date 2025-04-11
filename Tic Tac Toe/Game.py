from Player import Player
from Board import Board
from Menu import Menu

class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.cur_player_index = 0

    def Start_Game(self):
        choice = self.menu.Display_Main_Menu()
        if choice == '1':
            self.Setup_Game()
            self.Play_Game()
        else:
            self.Quit_Game()

    def Setup_Game(self):
        for index, player in enumerate(self.players, start=1):
            print(f"Player {index}, Enter Your Details : ")
            player.choose_name()
            player.choose_symbol()
            print('-'*20, '-'*20)

    def Play_Game(self):
        while True:
            self.Player_Turn()
            if self.Check_Win() or self.Check_Draw():
                choice = self.menu.Display_End_Game()
                if choice == '1':
                    self.Restart_Game()
                else:
                    self.Quit_Game()
                break

    def Quit_Game(self):
        print('Thanks for your Playing.....')

    def Player_Turn(self):
        player = self.players[self.cur_player_index]
        self.board.Display_Board()
        print(f"{player.get_name()}'s Turn and its symbol is : {player.get_symbol()}")
        while True:
            try:
                cell_choice = int(input('Choose cell [1-9] : '))
                if 1 <= cell_choice <=9 and self.board.Update_board(cell_choice,player.get_symbol()):
                    break
                else:
                    print(f"INVALID INPUT, Try Again{cell_choice}")
            except ValueError:
                print("Please Enter number between 1 and 9. ")
        self.Switch_Player()

    def Switch_Player(self):
        self.cur_player_index = 1- self.cur_player_index

    def Check_Win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        boardexchange = self.board.get_board()
        for combo in win_combinations:
            if boardexchange[combo[0]] == boardexchange[combo[1]] == boardexchange[combo[2]]:
                return True
        return False

    def Check_Draw(self):
        boardexchange = self.board.get_board()
        return all(not cell.isdigit() for cell in boardexchange)

    def Restart_Game(self):
        self.board.reset_board()
        self.cur_player_index = 0
        self.Play_Game()
