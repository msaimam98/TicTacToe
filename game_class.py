from typing import List, Tuple
from People import Player

class Game:
    """
    Initialize a new Game
    """
    game_array: List
    pos_game_array: List[Tuple]

    def __init__(self, player1: Player, player2: Player) -> None:

        self.player1 = player1
        self.player2 = player2
        self.game_array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.pos_game_array = [(self.game_array[0][0], 1),
                              (self.game_array[0][1], 2),
                              (self.game_array[0][2], 3),
                              (self.game_array[1][0], 4),
                              (self.game_array[1][1], 5),
                              (self.game_array[1][2], 6),
                              (self.game_array[2][0], 7),
                              (self.game_array[2][1], 8),
                              (self.game_array[2][2], 9)]

    def make_move(self, move: int, player: Player) -> None:
        """
        Have a particular player make a move
        """
        if player == self.player1:
            if move == 1:
                self.game_array[0][0] = 1
                self.pos_game_array[0] = (1, 1)
            elif move == 2:
                self.game_array[0][1] = 1
                self.pos_game_array[1] = (1, 2)
            elif move == 3:
                self.game_array[0][2] = 1
                self.pos_game_array[2] = (1, 3)
            elif move == 4:
                self.game_array[1][0] = 1
                self.pos_game_array[3] = (1, 4)
            elif move == 5:
                self.game_array[1][1] = 1
                self.pos_game_array[4] = (1, 5)
            elif move == 6:
                self.game_array[1][2] = 1
                self.pos_game_array[5] = (1, 6)
            elif move == 7:
                self.game_array[2][0] = 1
                self.pos_game_array[6] = (1, 7)
            elif move == 8:
                self.game_array[2][1] = 1
                self.pos_game_array[7] = (1, 8)
            else:
                self.game_array[2][2] = 1
                self.pos_game_array[8] = (1, 9)
        else: #player == self.player2:
            if move == 1:
                self.game_array[0][0] = 2
                self.pos_game_array[0] = (2, 1)
            elif move == 2:
                self.game_array[0][1] = 2
                self.pos_game_array[1] = (2, 2)
            elif move == 3:
                self.game_array[0][2] = 2
                self.pos_game_array[2] = (2, 3)
            elif move == 4:
                self.game_array[1][0] = 2
                self.pos_game_array[3] = (2, 4)
            elif move == 5:
                self.game_array[1][1] = 2
                self.pos_game_array[4] = (2, 5)
            elif move == 6:
                self.game_array[1][2] = 2
                self.pos_game_array[5] = (2, 6)
            elif move == 7:
                self.game_array[2][0] = 2
                self.pos_game_array[6] = (2, 7)
            elif move == 8:
                self.game_array[2][1] = 2
                self.pos_game_array[7] = (2, 8)
            else:
                self.game_array[2][2] = 2
                self.pos_game_array[8] = (2, 9)

    def someone_win(self, player: Player) -> bool:

        win = False
        # check vertical
        for i in range(len(self.game_array)):
            tracker = []
            for j in range(len(self.game_array)):
                tracker.append(self.game_array[j][i])
            if tracker == [player.tracking_num, player.tracking_num,
                           player.tracking_num]:
                win = True
                return win
        # Check horizontal
        for element in self.game_array:
            if element == [player.tracking_num, player.tracking_num,
                           player.tracking_num]:
                win = True
                return win
        # check diagonal
        # left down to right - part1
        for i in range(len(self.game_array)):
            tracker1 = []
            for j in range(len(self.game_array)):
                if i == j:
                    tracker1.append(self.game_array[j][i])
            if tracker1 == [player.tracking_num, player.tracking_num,
                           player.tracking_num]:
                win = True
                return win
        # right down to left - part2
        for i in range(len(self.game_array)):
            tracker1 = []
            counter = 2
            for j in range(len(self.game_array) - 1, 1, -1):
                if i == counter:
                    tracker1.append(self.game_array[j][i])
                    counter -= 1
            if tracker1 == [player.tracking_num, player.tracking_num,
                            player.tracking_num]:
                win = True
                return win

    def all_places_not_full(self) -> bool:
        not_full = True
        for item in self.game_array:
            for element in item:
                if element == 0:
                    return not_full
        not_full = False
        return not_full

    def check_move(self, move: int) -> bool:
        """Check if a move is already made
        """
        for i in range(len(self.pos_game_array)):
            if (i + 1) == move:
                if self.pos_game_array[i][0] == 2 or \
                        self.pos_game_array[i][0] == 1:
                    print("That move has already been utilized!")
                    return False
                else:
                    return True

    def current_state(self):
        """
        print the current state of the game
        """
        print("This is the current state of your game ")
        print('_' + str(self.game_array[0][0]) +'_|_' +
              str(self.game_array[0][1]) +'_|_' + str(self.game_array[0][2]) +'_')
        print('_' + str(self.game_array[1][0]) +'_|_' +
              str(self.game_array[1][1]) +'_|_' + str(self.game_array[1][2]) +'_')
        print('_' + str(self.game_array[2][0]) +'_|_' +
              str(self.game_array[2][1]) +'_|_' + str(self.game_array[2][2]) +'_')







