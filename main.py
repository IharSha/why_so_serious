class Board:
    board = []

    def __init__(self, column, row):
        for i in range(row):
            self.board.append(['-']*column)

    def __repr__(self):
        raw_board = ''
        for row in self.board:
            for element in row:
                raw_board += str(element)
            raw_board += '\n'
        return "This is your board:\n{}".format(raw_board)


COLUMN = 10
ROW = 5

board = Board(COLUMN, ROW)
print board
