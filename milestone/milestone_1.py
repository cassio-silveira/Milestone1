# Projeto KZIO

from math import sqrt
import string
import os

def clean_board(n):

    collums = list(string.ascii_uppercase)
    rows = range(1,n+1)

    board = {cx + str(cy): ' '
                for cx in collums[:n]
                for cy in rows}
    return board

def turns_alternator(player, playerX, playerO):

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
        output = [li_values[a] for a in id]
        id = [x-1 for x in id]
        print(f'{li_range[inverted_lines]}', output)

    print(' ', list(string.ascii_uppercase)[:board_size])
    

def possible_choices(board):

    return [key for key,value in board.items() if value == ' ']


def get_valid_input(request_str: str, error_str:str, li_valid_input: list):

    while True:
        input_str = input(request_str)
        if input_str in li_valid_input:
            return input_str
        else:
            print(error_str)


def position_choice(board):

    display_board(board)

    return get_valid_input('Pick a position: ', 'Invalid Position. Escolha outra.', possible_choices(board))

def replace_choice(index, player, board):

    board[index] = player
    

def check_game_finish(player, board):

    
    board_size = int(sqrt(len(board)))
    letters = list(string.ascii_uppercase)[:board_size]
    numbers = [str(num) for num in range(1, board_size+1)]

    checks_li = [[letra + num for letra in letters] for num in numbers]\
    + [[letra + num for num in numbers] for letra in letters]\
    + [[letra + num for letra, num in zip(letters, numbers)]]\
    + [[letra + num for letra, num in zip(reversed(letters), numbers)]]


    if possible_choices(board):
        for check_li in checks_li:
            if all([board.get(check) == player for check in check_li]):
                print(f'PLAYER {player} WINS')
                return False



    else:
        print("EMPATE!!!")
        return False
    
    

    return True



def game_run():

    want_play = True

    while want_play:


        os.system('cls')
        initial_player = get_valid_input("Escolhar X ou O para começar: ", "Opcao invalida, escolha novamente.", ['x','X','o','O']).upper()
        os.system('cls')
        player = initial_player
        playerX = "X"
        playerO = "O"

        status_game = True

        n = 5

        board = clean_board(n)

        while status_game:
            
            # replace_choice(position_choice(board), player, board)
            board[position_choice(board)] = player
            os.system('cls')
            status_game = check_game_finish(player ,board)
            player = turns_alternator(player, playerX, playerO)

        if get_valid_input("Quer jogar novamente? (S/N)", "Opção invalida, escolha S ou N.", ['S','s','n','N']).lower() != 's':
            want_play = False

    



if __name__ == "__main__":

    game_run()
    # print(clean_board(3))
    # display_board(clean_board(3))