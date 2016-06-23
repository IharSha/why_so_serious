import random


class Board:
    board = []

    def __init__(self, rows, columns):
        self.columns = columns
        self.rows = rows
        for row in range(self.rows):
            self.board.append(['-'] * self.columns)

    def __repr__(self):
        return "Board object: {}x{}".format(self.rows, self.columns)

    def show(self):
        print '~' * self.columns * 2
        for row in self.board:
            print " ".join(row)
        print '~' * self.columns * 2

    def shuffle_stars(self):

        for row in range(self.rows):
            for column in range(self.columns):
                if random.random() < 0.5:
                    self.board[row][column] = '*'


board = Board(7, 7)
print(board)
board.shuffle_stars()
board.show()
