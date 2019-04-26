import sys
from AlphaZeroAI import AlphaZeroAI as AI
sys.path.append('../gym-connect4/gym_connect4/envs/lib/')
import board
import move
import human
sys.path.append('../alpha-zero-general/')
from MCTS import MCTS
from utils import dotdict
from connect4.tensorflow.NNet import NNetWrapper as NNet

class Connect4():

    def __init__(self):
        self.game_board = board.Board()
        self.moves = self.game_board.moves
        self.player1 = AlphaZeroAI(self.game_board, 1)
        self.player2 = AlphaZeroAI(self.game_board, 2)

    def test(self, input_values):
        def mock_input(s):
            print(s)
            return input_values.pop(0)
        human.input = mock_input

    def start(self):
        self.players()
        player = 2
        not_over = True
        turn = 1
        while not_over and turn <= 42 :
            if player == 1 :
                player = 2
                self.game_board.make_move(2, self.player2.move())
            else:
                player = 1
                self.game_board.make_move(1, self.player1.move())
            self.show_board()
            not_over = not self.gameover()
            turn += 1

        if not_over == True:
            print("It's a Draw!")
        else:
            self.show_board()
            #print(f'Player {player} wins')

    def show_board(self):
        string = ""
        i = len(self.game_board.game_board)-1
        while i > -1:
            row = self.game_board.game_board[i]
            #for token in row:
                #string +=  f'|{token}|'
            string += "\n"
            i -= 1
        print(string)

    def gameover(self):
        return self.game_board.moves.check_win()

    def players(self):
        if input("Player 1 is a Human or AI?") == "Human" : self.player1 = human.Human(self.moves)
        if input("Player 2 is a Human or AI?") == "Human" : self.player2 = human.Human(self.moves)
        return

if __name__ == "__main__":
    c4 = Connect4()
    c4.start()        