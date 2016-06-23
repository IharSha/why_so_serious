import random
import time


class Board:
    board = []

    def __init__(self, rows, columns):
        self.columns = columns
        self.rows = rows
        for row in range(self.rows):
            self.board.append(['-'] * self.columns)
        for row in self.board:
            print " ".join(row)
        print('Here is your dungeon! Look, how good it is!\n')

    def __repr__(self):
        return "Dungeon of size {}x{}\n".format(self.rows, self.columns)

    def show(self):
        print '~' * self.columns * 2
        for row in self.board:
            print " ".join(row)
        print '~' * self.columns * 2
        print("The dungeon revealed!\n")

    def add_spikes(self):
        print("Adding spikes in random places... You know, for safety...")
        for row in range(self.rows):
            for column in range(self.columns):
                if random.random() < 0.5:
                    self.board[row][column] = '*'
        time.sleep(1)

        print("Done, now you can hurt yourself here.\n")

    def create_treasure(self):
        print("Hiding treasure... Because without treasure there is no fun at all.")
        self.board[random.randrange(self.rows)][random.randrange(self.columns)] = 'T'
        time.sleep(0.7)

        print("Try to find it.\n")


def check_if_number(user_inp):
    while type(user_inp) != int:
        try:
            user_inp = int(user_inp)
        except ValueError:
            user_inp = raw_input('Hm...I guess you have problems with numbers. Try one more time, remember! '
                                 'This are numbers ->: 123456789, in case you forgot. Type: ')
    return user_inp

board_size = check_if_number(raw_input('Please create your dungeon, what size should it be? Type one number: '))
if board_size <= 1:
    print('This is not cool size, let`s pretend you typed 10.\n')
    board_size = 10

board = Board(board_size, board_size)

board.add_spikes()
board.create_treasure()

while True:
    user_row = check_if_number(raw_input("Please type row number from 1 to {}: ".format(board.rows)))
    user_column = check_if_number(raw_input("Please type column number from 1 to {}: ".format(board.columns)))
    if user_row > board.rows or user_row < 0 or user_column > board.columns or user_column < 0:
        print("Please try to stay in dungeon. You need this treasure really much!\n")
        continue

    if board.board[user_row - 1][user_column - 1] == "*":
        print("You are dead buddy :(\n")
        board.show()
        break
    elif board.board[user_row - 1][user_column - 1] == "T":
        print("You found a T letter. You won by the way.\nBye.")
        board.show()
        break
    else:
        print("Ok there is no spikes here and no treasures, keep going bro!\n")
