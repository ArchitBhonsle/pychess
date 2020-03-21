from stockfish import Stockfish
from board import Board


class Game:

    def __init__(self):
        self.engine = Stockfish(path='stockfish')
        self.board = Board()

    def sync_engine(self):
        self.engine.set_position(self.board.move_list)

    def get_best_move(self) -> str:
        return self.engine.get_best_move()

    def is_move_correct(self, move: str) -> bool:
        return self.engine.is_move_correct(move)

    def make_move(self, move):
        if self.is_move_correct(move):
            self.board.make_move(move)
            self.sync_engine()
        else:
            print("Invalid move")

    def make_best_move(self):
        self.make_move(self.get_best_move())
