import math
import random
import time
import os

from termcolor import cprint

colors = ['white', 'yellow', 'green', 'red', 'magenta', 'blue', 'cyan']


class Game2048:
    def __init__(self):
        self.state = [0, 0, 0, 0,
                      0, 0, 0, 0,
                      0, 0, 0, 0,
                      0, 0, 0, 0]

        self.score = 0
        self.add_new_tile()

    def add_new_tile(self):
        emptySpots = []
        for tile in range(0, len(self.state)):
            if self.state[tile] == 0:
                emptySpots.append(tile)

        if not emptySpots:
            return

        newTile = random.choice(emptySpots)
        newTileValue = 2 if random.uniform(0, 1) < 0.9 else 4  # assigns value for a new random tile
        self.state[newTile] = newTileValue

    def make_move(self, move):
        if move == 0:  # left
            for i in range(0, 4):
                j = 0
                while j < 3:  # rightmost tiles can't move right
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0 and self.state[checkTile] == self.state[checkTile+1]:
                        # check if tile can merge with what is on its right
                        self.state[checkTile] = self.state[checkTile] * 2  # shift the tile left by 1 spot
                        self.state[checkTile+1] = 0  # reset the shifted tile
                        self.score += self.state[checkTile]
                        j += 2

                    else:
                        j += 1

                nonzero = []
                for j in range(0, 4):
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0:
                        nonzero.append(self.state[checkTile])

                for j in range(0, 4):
                    checkTile = i * 4 + j
                    if j >= len(nonzero):
                        self.state[checkTile] = 0
                    else:
                        self.state[checkTile] = nonzero[j]

        if move == 1:  # right
            for i in range(0, 4):
                j = 3
                while j > 0:  # rightmost tiles can't move right
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0 and self.state[checkTile] == self.state[checkTile-1]:
                        # check if tile can merge with what is on its left
                        self.state[checkTile] = self.state[checkTile] * 2  # shift the tile right by 1 spot
                        self.state[checkTile-1] = 0  # reset the shifted tile
                        self.score += self.state[checkTile]
                        j -= 2
                    else:
                        j -= 1

                nonzero = []
                for j in range(3, -1, -1):
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0:
                        nonzero.append(self.state[checkTile])

                for j in range(3, -1, -1):
                    checkTile = i * 4 + j
                    if 3 - j >= len(nonzero):
                        self.state[checkTile] = 0
                    else:
                        self.state[checkTile] = nonzero[3 - j]

        if move == 2:  # up
            for j in range(0, 4):
                i = 0
                while i < 3:  # rightmost tiles can't move right
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0 and self.state[checkTile] == self.state[checkTile+4]:
                        # check if tile can merge with what is on its left
                        self.state[checkTile] = self.state[checkTile] * 2  # shift the tile right by 1 spot
                        self.state[checkTile+4] = 0  # reset the shifted tile
                        self.score += self.state[checkTile]
                        i += 2
                    else:
                        i += 1

                nonzero = []
                for i in range(0, 4):
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0:
                        nonzero.append(self.state[checkTile])

                for i in range(0, 4):
                    checkTile = i * 4 + j
                    if i >= len(nonzero):
                        self.state[checkTile] = 0
                    else:
                        self.state[checkTile] = nonzero[i]

        if move == 3:  # down
            for j in range(0, 4):
                i = 3
                while i > 0:  # rightmost tiles can't move right
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0 and self.state[checkTile] == self.state[checkTile-4]:
                        # check if tile can merge with what is on its left
                        self.state[checkTile] = self.state[checkTile] * 2  # shift the tile right by 1 spot
                        self.state[checkTile-4] = 0  # reset the shifted tile
                        self.score += self.state[checkTile]
                        i -= 2
                    else:
                        i -= 1

                nonzero = []
                for i in range(3, -1, -1):
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0:
                        nonzero.append(self.state[checkTile])

                for i in range(3, -1, -1):
                    checkTile = i * 4 + j
                    if 3 - i >= len(nonzero):
                        self.state[checkTile] = 0
                    else:
                        self.state[checkTile] = nonzero[3 - i]

        if move == 0:  # left
            for i in range(0, 4):
                j = 0
                while j < 3:  # rightmost tiles can't move right
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0 and self.state[checkTile] == self.state[checkTile+1]:
                        # check if tile can merge with what is on its right
                        self.state[checkTile] = self.state[checkTile] * 2  # shift the tile left by 1 spot
                        self.state[checkTile+1] = 0  # reset the shifted tile
                        self.score += self.state[checkTile]
                        j += 2

                    else:
                        j += 1

                nonzero = []
                for j in range(0, 4):
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0:
                        nonzero.append(self.state[checkTile])

                for j in range(0, 4):
                    checkTile = i * 4 + j
                    if j >= len(nonzero):
                        self.state[checkTile] = 0
                    else:
                        self.state[checkTile] = nonzero[j]

        if move == 1:  # right
            for i in range(0, 4):
                j = 3
                while j > 0:  # rightmost tiles can't move right
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0 and self.state[checkTile] == self.state[checkTile-1]:
                        # check if tile can merge with what is on its left
                        self.state[checkTile] = self.state[checkTile] * 2  # shift the tile right by 1 spot
                        self.state[checkTile-1] = 0  # reset the shifted tile
                        self.score += self.state[checkTile]
                        j -= 2
                    else:
                        j -= 1

                nonzero = []
                for j in range(3, -1, -1):
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0:
                        nonzero.append(self.state[checkTile])

                for j in range(3, -1, -1):
                    checkTile = i * 4 + j
                    if 3 - j >= len(nonzero):
                        self.state[checkTile] = 0
                    else:
                        self.state[checkTile] = nonzero[3 - j]

        if move == 2:  # up
            for j in range(0, 4):
                i = 0
                while i < 3:  # rightmost tiles can't move right
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0 and self.state[checkTile] == self.state[checkTile+4]:
                        # check if tile can merge with what is on its left
                        self.state[checkTile] = self.state[checkTile] * 2  # shift the tile right by 1 spot
                        self.state[checkTile+4] = 0  # reset the shifted tile
                        self.score += self.state[checkTile]
                        i += 2
                    else:
                        i += 1

                nonzero = []
                for i in range(0, 4):
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0:
                        nonzero.append(self.state[checkTile])

                for i in range(0, 4):
                    checkTile = i * 4 + j
                    if i >= len(nonzero):
                        self.state[checkTile] = 0
                    else:
                        self.state[checkTile] = nonzero[i]

        if move == 3:  # down
            for j in range(0, 4):
                i = 3
                while i > 0:  # rightmost tiles can't move right
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0 and self.state[checkTile] == self.state[checkTile-4]:
                        # check if tile can merge with what is on its left
                        self.state[checkTile] = self.state[checkTile] * 2  # shift the tile right by 1 spot
                        self.state[checkTile-4] = 0  # reset the shifted tile
                        self.score += self.state[checkTile]
                        i -= 2
                    else:
                        i -= 1

                nonzero = []
                for i in range(3, -1, -1):
                    checkTile = i * 4 + j
                    if self.state[checkTile] != 0:
                        nonzero.append(self.state[checkTile])

                for i in range(3, -1, -1):
                    checkTile = i * 4 + j
                    if 3 - i >= len(nonzero):
                        self.state[checkTile] = 0
                    else:
                        self.state[checkTile] = nonzero[3 - i]

        self.add_new_tile()

    def display_state(self):
        print("==============================================")
        for i in range(0, 4):
            for j in range(0, 4):
                num = self.state[i * 4 + j]
                cprint(num, colors[int(math.log(num + 1, 2))] if num <= 64 else 'cyan', end="\t")
            print()
        print("==============================================")

    def return_state(self):
        returnedstate = []
        for i in self.state:
            if i == 0:
                returnedstate.append(i)
            else:
                returnedstate.append(int(math.log(i,2)))
        return returnedstate

    def return_score(self):
        return self.score

    def check_for_termination(self):
        for i in range(0,len(self.state)):
            if self.state[i] == 0:
                return False
            else:
                if i == 0:
                    if self.state[i] == self.state[i+1] or self.state[i] == self.state[i+4]:
                        return False
                elif i == 1 or i == 2:
                    if self.state[i] == self.state[i-1] or self.state[i] == self.state[i+4] or self.state[i] == self.state[i+1]:
                        return False
                elif i == 3:
                    if self.state[i] == self.state[i-1] or self.state[i] == self.state[i+4]:
                        return False
                elif i == 4 or i == 8:
                   if self.state[i] == self.state[i-4] or self.state[i] == self.state[i+4] or self.state[i] == self.state[i+1]:
                       return False
                elif i == 7 or i == 11:
                    if self.state[i] == self.state[i-4] or self.state[i] == self.state[i+4] or self.state[i] == self.state[i-1]:
                        return False
                elif i == 12:
                    if self.state[i] == self.state[i + 1] or self.state[i] == self.state[i - 4]:
                        return False
                elif i == 13 or i == 14:
                    if self.state[i] == self.state[i - 1] or self.state[i] == self.state[i - 4] or self.state[i] == self.state[i + 1]:
                        return False
                elif i == 15:
                    if self.state[i] == self.state[i - 1] or self.state[i] == self.state[i - 4]:
                        return False
                else:
                    if self.state[i] == self.state[i+1] or self.state[i] == self.state[i-1] or self.state[i] == self.state[i+4] or self.state[i] == self.state[i-4]:
                        return False
        return True

    def reset_game(self):
        self.__init__()

