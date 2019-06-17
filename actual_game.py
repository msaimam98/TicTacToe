from People import Player
from game_class import Game


TOP_LEFT = 1
MIDDLE_LEFT = 2
LOWER_LEFT = 3
TOP_MIDDLE = 4
MIDDLE_MIDDLE = 5
LOWER_MIDDLE = 6
TOP_RIGHT = 7
MIDDLE_RIGHT = 8
LOWER_RIGHT = 9

MOVES_ARRAY = [TOP_LEFT, TOP_MIDDLE, TOP_RIGHT, MIDDLE_LEFT, MIDDLE_MIDDLE,
               MIDDLE_RIGHT, LOWER_RIGHT, LOWER_MIDDLE, LOWER_LEFT]

game_play = True
while game_play:
    player1 = input("player1:    ")
    player2 = input("player2:    ")

    guy1 = Player(player1, 1)
    guy2 = Player(player2, 2)
    winner = None
    new_game = Game(guy1, guy2)

    print('Instructions:')
    print('Each grid location is numbered.'
          'Please use those numbers to place your tictactoe')
    print('_1_|_2_|_3_')
    print('_4_|_5_|_6_')
    print(' 7 | 8 | 9 ')

    i = 0
    next_move_man = guy1
    while not new_game.someone_win(next_move_man) and \
            new_game.all_places_not_full():
        if i % 2 == 0:
            move = input(guy1.name + " makes a move:    ")
            if move.isdigit():
                move1 = int(move)
                if 9 >= move1 >= 1:
                    for mv in MOVES_ARRAY:
                        if move1 == mv and new_game.check_move(move1):
                            new_game.make_move(move1, guy1)
                            i += 1
                            new_game.current_state()
                            next_move_man = guy1
                        # else:
                        #     print("A player has already made a move here")
                else:
                    print("Please use one of the moves outlined!")

            else:
                print("Please use one of the moves outlined!")
        else:
            move = input(guy2.name + " makes a move:    ")
            if move.isdigit():
                move1 = int(move)
                if 9 >= move1 >= 1:
                    for mv in MOVES_ARRAY:
                        if move1 == mv and new_game.check_move(move1):
                            new_game.make_move(move1, guy2)
                            i += 1
                            new_game.current_state()
                            next_move_man = guy2
                        # else:
                        #     print("A player has already made a move here")
                else:
                    print("Please use one of the moves outlined!")
            else:
                print("Please use one of the moves outlined!")

    full = new_game.all_places_not_full()
    if full is not False:
        winner = next_move_man
        print(winner.name + ' is the winner! Congrats ' + winner.name + '!')
    else:
        print("Its a draw folks!")

    play_again1 = input("Would you guys like to play again? [y/n]")
    while play_again1 != 'y' and play_again1 != 'n':
        print("Please select y or n")
        play_again1 = input("Would you guys like to play again? [y/n]")
    if play_again1 == 'n':
        game_play = False




















