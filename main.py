import random
import time


def check_if_number(user_input):
    """Check that user's input is a number"""
    while type(user_input) != int:
        try:
            user_input = int(user_input)
        except ValueError:
            user_input = input("Hm... I guess you have problems with numbers.\n"
                               "Try one more time, remember! This are numbers -> 123456789,"
                               " in case you forgot.\n"
                               "Now, type the number: ")
    return user_input


class Dungeon:
    """Create Dungeon object."""

    def __init__(self, rows, columns):
        self.board = []
        self.columns = columns
        self.rows = rows
        for row in range(self.rows):
            self.board.append(['-'] * self.columns)
        for row in self.board:
            print(" ".join(row))
        print("Here is your dungeon! Look, how good it is!\n")

    def __repr__(self):
        return "Board size {}x{}\n".format(self.rows, self.columns)

    def reveal(self):
        """reveal the dungeon with spikes and treasure."""
        print('~' * self.columns * 2)
        for row in self.board:
            print(" ".join(row))
        print('~' * self.columns * 2)
        print("The dungeon revealed!\n")

    def player_map(self):
        """shows current map"""
        print("Dungeon map:")
        print('~' * self.columns * 2)
        for row in self.board:
            hidden_row = []
            for cell in row:
                if cell == '*' or cell == 'T':
                    hidden_row.append('-')
                else:
                    hidden_row.append(cell)
            print(" ".join(hidden_row))
        print('~' * self.columns * 2)
        print()

    def add_spikes(self):
        """Randomly add spikes."""
        print("Adding spikes in random places... You know, for safety...")
        for row in range(self.rows):
            for column in range(self.columns):
                if random.random() < 0.3:
                    self.board[row][column] = '*'
        time.sleep(0.5)

        print("...Done, now you can hurt yourself here. Much fun!\n")

    def create_treasure(self):
        """Randomly add treasure."""
        print("Hiding treasure... Because without treasure there is no fun at all.")
        self.board[random.randrange(self.rows)][random.randrange(self.columns)] = 'T'
        time.sleep(0.5)

        print("...Now, try to find it!\n")


game_on = True
while game_on:
    dungeon_size = check_if_number(
        input("Please create your dungeon, what size should it be? Type one number: ")
    )
    print()
    if dungeon_size <= 2:
        print("This is not cool size, let`s pretend you typed 5.\n")
        dungeon_size = 5

    dungeon = Dungeon(dungeon_size, dungeon_size)

    dungeon.add_spikes()
    dungeon.create_treasure()

    while True:
        # choose square
        user_row = check_if_number(
            input(f"Please type row number from 1 to {dungeon.rows}: ")
        )
        user_column = check_if_number(
            input(f"Please type column number from 1 to {dungeon.columns}: ")
        )
        print()

        # check that selected square in the dungeon otherwise choose square again
        if user_row > dungeon.rows or user_row < 0 \
                or user_column > dungeon.columns or user_column < 0:
            print("Please try to stay in dungeon. You need this treasure really much!\n")
            continue

        if dungeon.board[user_row - 1][user_column - 1] == "*":
            time.sleep(0.3)
            print("SPIKES!!!\nYou are dead buddy :(\n")
            dungeon.reveal()
            break
        elif dungeon.board[user_row - 1][user_column - 1] == "T":
            time.sleep(0.3)
            print("You found a T letter. T is for Treasure.")
            print("You won by the way. That's all I have.\nBye.")
            dungeon.reveal()
            break
        elif dungeon.board[user_row - 1][user_column - 1] == "0":
            time.sleep(0.3)
            print("Didn't you check this place already? Still nothing.\n")
            dungeon.player_map()
        else:
            time.sleep(0.3)
            print("Ok there is no spikes here and no treasures, keep going bro!\n")
            dungeon.board[user_row - 1][user_column - 1] = "0"
            dungeon.player_map()

    restart = input("To start new game type any kind word or press enter to quit this EPIC GAME: ")
    print()
    if restart and restart.lower() not in ("no", "no!", "n", "stop", "bye"):
        game_on = True
    else:
        game_on = False
        print("See you soon young adventurer! Or not! Bye!")
