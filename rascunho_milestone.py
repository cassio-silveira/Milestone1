# Projeto KZIO

from math import sqrt
import string

def clean_board(n):

    collums = list(string.ascii_uppercase)
    rows = range(1,n+1)

    board = {cx + str(cy): ' '
                for cx in collums[:n]
                for cy in rows}
    return board

def turns_alternator(player, playerX, playerO):

    # while player == "zero":
    #     player = input("Escolhar X ou O para começar: ")
    #     if player in ("x","X"):
    #         player = playerX
    #         return player
    #     elif player in ("o", "O"):
    #         player = playerO
    #         return player
    #     else:
    #         print("Opcao invalida, escolha novamente.")
    #         player = "zero"

    if player == playerX:
        player = playerO
        return player

    if player == playerO:
        player = playerX
        return player

def display_board(board):

    board_size = int(sqrt(len(board)))
    li_keys = list(board.keys())
    li_values = list(board.values())
    li_range = list(range(1, board_size+1))

    id = list(range(board_size-1, len(li_keys), board_size))

    for inverted_lines in range(board_size-1,-1,-1):
        output = [li_keys[a] for a in id]
        id = [x-1 for x in id]
        print(f'{li_range[inverted_lines]}', output)

    print(' ', list(string.ascii_uppercase)[:board_size])


def possible_choices(board):

    # options = []

    # for _ in board:
    #     if board[_] == ' ':
    #         options.append(_)

    return [key for key,value in board.items() if value == ' ']


def get_valid_input(request_str: str, error_str:str, li_valid_input: list):

    while True:
        input_str = input(request_str)
        if input_str in li_valid_input:
            return input_str
        else:
            print(error_str)

    # if option == 'player':
    #     while option == 'player':
    #         option = input('Escolha X ou O para começar: ')
    #         if option in ('x','X','o','O'):
    #             return option
    #         else:
    #             print('Opcao invalida, escolha novamente.')
    #             option = 'player'

    # if option == 'position':
    #     while option == 'position':
    #         option = input('Pick a position: ')
    #         if option not in possible_choices(board):
    #             print('Invalid Position. Escolha outra.')
    #             option = 'position'
    #         else:
    #             return option



def position_choice(board):

    option = 'position'

    display_board(board)

    get_valid_input('Pick a position: ', 'Invalid Position. Escolha outra.', possible_choices(board))
    return int(option)

def replace_choice(index, player, board):
    # if choice in [1,2,3]:
    #     board1.update({choice:player})
    # if choice in [4,5,6]:
    #     board2.update({choice:player})
    # if choice in [7,8,9]:
    #     board3.update({choice:player})

    board[index] = player

def check_game_finish(playerlist, board):

    if possible_choices(board):
        pass
    else:
        print()


    # if statusGame:

    #     for linha in (board1, board2, board3):
    #         if list(linha.values()) == ['X', 'X', 'X']:
    #             statusGame = False
    #             return print("Player X WINS!!!"), statusGame

    #         if list(linha.values()) == ['O', 'O', 'O']:
    #             statusGame = False
    #             return print("Player O WINS!!!"), statusGame

    #     for coluna in range(1,4):
    #         if list(board1[coluna]) + list(board2[coluna + 3]) + list(board3[coluna + 6]) == ['X', 'X', 'X']:
    #             statusGame = False
    #             return print("Player X WINS!!!"), statusGame

    #         if list(board1[coluna]) + list(board2[coluna+3]) + list(board3[coluna+6]) == ['O', 'O', 'O']:
    #             statusGame = False
    #             return print("Player O WINS!!!"), statusGame

    #     if list(board1[1]) + list(board2[5]) + list(board3[9]) == ['X', 'X', 'X']:
    #         statusGame = False
    #         return print("Player X WINS!!!"), statusGame

    #     if list(board1[3]) + list(board2[5]) + list(board3[7]) == ['X', 'X', 'X']:
    #         statusGame = False
    #         return print("Player X WINS!!!"), statusGame

    #     if list(board1[1]) + list(board2[5]) + list(board3[9]) == ['O', 'O', 'O']:
    #         statusGame = False
    #         return print("Player O WINS!!!"), statusGame

    #     if list(board1[3]) + list(board2[5]) + list(board3[7]) == ['O', 'O', 'O']:
    #         statusGame = False
    #         return print("Player O WINS!!!"), statusGame

    #     if len(possibleChoices) == 0:
    #         statusGame = False
    #         display_board(board1, board2, board3)
    #         return print("EMPATE!!!"), statusGame

    pass

def game_run():

    board1 = {1:[1],2:[2],3:[3]}
    board2 = {4:[4],5:[5],6:[6]}
    board3 = {7:[7],8:[8],9:[9]}

    possibleChoices = [1,2,3,4,5,6,7,8,9]

    player = "zero"

    playerX = "X"
    playerO = "O"

    statusGame = True

    n = 3

    board = clean_board(n)

    while statusGame:
        turns_alternator(get_valid_input("Escolhar X ou O para começar: ", "Opcao invalida, escolha novamente.", ['x','X','o','O']), playerX, playerO)
        replace_choice(position_choice(board), player)
        check_game_finish()


if __name__ == "__main__":


    game_run()
    # print(clean_board(3))
    # display_board(clean_board(3))