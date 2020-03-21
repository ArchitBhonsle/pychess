class Board:

    def __init__(self):
        self.board = self.initialize_pieces(
            [[" " for i in range(8)] for j in range(8)])
        self.move_list = []

    def initialize_pieces(self, board) -> list:
        board[1] = ['P' for i in range(8)]
        board[6] = ['p' for i in range(8)]
        board[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        board[7] = [i.lower() for i in board[0]]
        return board

    def get_rowcol(self, move: str) -> tuple:
        return ord(move[0])-97, int(move[1])-1

    def make_move(self, move: str) -> list:
        self.move_list.append(move)
        # ! Handle Castling, Promations and En Passants
        (ci, ri), (cf, rf) = self.get_rowcol(
            move[0:2]), self.get_rowcol(move[2:4])
        self.board[ri][ci], self.board[rf][cf] = " ", self.board[ri][ci]
        return self.move_list

    def actual_board(self) -> str:
        res = []
        for i in range(8):
            res.append(" ".join(self.board[i]))
        return "\n".join(res)

    def __str__(self) -> str:
        res = []
        for i in range(7, -1, -1):
            res.append(" ".join(self.board[i]))
        return "\n".join(res)


b = Board()
print("Board: ", str(b), sep="\n")
print("Actual Board: ", b.actual_board(), sep="\n")
print(b.make_move('e2e4'))
print(str(b))
