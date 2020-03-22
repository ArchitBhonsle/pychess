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
        (ci, ri), (cf, rf) = self.get_rowcol(
            move[0:2]), self.get_rowcol(move[2:4])

        if len(move) == 5:
            # Promotions
            self.board[ri][ci], self.board[rf][cf] = \
                " ", \
                move[4] if self.board[ri][ci].islower() else move[4].upper()
        elif (move in ('e1g1', 'e1c1', 'e8g8', 'e8c8')) and \
                (self.board[ri][ci] in ("K", "k")):
            # Castling
            self.board[ri][ci], self.board[rf][cf] = " ", self.board[ri][ci]
            if move == 'e1g1':
                self.make_move('h1f1')
            elif move == 'e1c1':
                self.make_move('a1d1')
            elif move == 'e8g8':
                self.make_move('h8f8')
            elif move == 'e8c8':
                self.make_move('a8d8')
        elif (self.board[ri][ci] in ("p", "P") and (ci != cf) and (self.board[rf][cf] == " ")):
            # En Passant
            self.board[ri][cf] = " "
            self.board[ri][ci], self.board[rf][cf] = " ", self.board[ri][ci]
        else:
            # Normal moves
            self.board[ri][ci], self.board[rf][cf] = " ", self.board[ri][ci]

        return self.move_list

    def actual_board(self) -> str:
        res = []
        for i in range(8):
            res.append(" ".join(self.board[i]))
        return "\n".join(res)

    def get_pretty_board(self) -> list:
        res = []
        for i in range(7, -1, -1):
            res.append(self.board[i])
        return res

    def __str__(self) -> str:
        res = []
        for i in range(7, -1, -1):
            res.append(" ".join(self.board[i]))
        return "\n".join(res)


if __name__ == "__main__":
    b = Board()
    print("Board: ", str(b), sep="\n")
    print("Actual Board: ", b.actual_board(), sep="\n")
    print(b.make_move('e2e4'))
    print(b.make_move('e7e5'))
    print(b.make_move('g1f3'))
    print(str(b))
