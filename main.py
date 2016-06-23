import random
import time


class Dungeon:
    """Create Dungeon object."""
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
        return "Board size {}x{}\n".format(self.rows, self.columns)

    def show(self):
        """reveal the dungeon with spikes and treasure."""
        print '~' * self.columns * 2
        for row in self.board:
            print " ".join(row)
        print '~' * self.columns * 2
        print("The dungeon revealed!\n")

    def add_spikes(self):
        """Randomly add spikes."""
        print("Adding spikes in random places... You know, for safety...")
        for row in range(self.rows):
            for column in range(self.columns):
                if random.random() < 0.5:
                    self.board[row][column] = '*'
        time.sleep(1)

        print("Done, now you can hurt yourself here.\n")

    def create_treasure(self):
        """Randomly add treasure."""
        print("Hiding treasure... Because without treasure there is no fun at all.")
        self.board[random.randrange(self.rows)][random.randrange(self.columns)] = 'T'
        time.sleep(0.7)

        print("Try to find it.\n")


def check_if_number(user_input):
    """Check that user's input is a number"""
    while type(user_input) != int:
        try:
            user_input = int(user_input)
        except ValueError:
            user_input = raw_input("Hm... I guess you have problems with numbers.\n"
                                   "Try one more time, remember! This are numbers -> 123456789, in case you forgot.\n"
                                   "Now, type the number: ")
    return user_input


dungeon_size = check_if_number(raw_input('Please create your dungeon, what size should it be? Type one number: '))
if dungeon_size <= 1:
    print('This is not cool size, let`s pretend you typed 5.\n')
    dungeon_size = 5

dungeon = Dungeon(dungeon_size, dungeon_size)

dungeon.add_spikes()
dungeon.create_treasure()

while True:
    # choose square
    user_row = check_if_number(raw_input("Please type row number from 1 to {}: ".format(dungeon.rows)))
    user_column = check_if_number(raw_input("Please type column number from 1 to {}: ".format(dungeon.columns)))

    # check that selected square in the dungeon otherwise choose square again
    if user_row > dungeon.rows or user_row < 0 or user_column > dungeon.columns or user_column < 0:
        print("Please try to stay in dungeon. You need this treasure really much!\n")
        continue

    if dungeon.board[user_row - 1][user_column - 1] == "*":
        print("You are dead buddy :(\n")
        dungeon.show()
        break
    elif dungeon.board[user_row - 1][user_column - 1] == "T":
        print("You found a T letter. You won by the way.\nBye.")
        dungeon.show()
        break
    else:
        print("Ok there is no spikes here and no treasures, keep going bro!\n")
