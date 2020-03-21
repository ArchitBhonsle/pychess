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
