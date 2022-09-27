board1 = {1:[1],2:[2],3:[3]}
board2 = {4:[4],5:[5],6:[6]}
board3 = {7:[7],8:[8],9:[9]}

possibleChoices = [1,2,3,4,5,6,7,8,9]

player = "zero"

playerX = "X"
playerO = "O"

statusGame = True

def turns_alternator():

    global player
    while player == "zero":
        player = input("Escolhar X ou O para começar: ")
        if player in ("x","X"):
            player = playerX
            return player
        elif player in ("o", "O"):
            player = playerO
            return player
        else:
            print("Opcao invalida, escolha novamente.")
            player = "zero"        

    if player == playerX:
        player = playerO
        return player

    if player == playerO:
        player = playerX
        return player

def display_board(board1, board2, board3):
    print(list(board1.values()))
    print(list(board2.values()))
    print(list(board3.values()))

def position_choice():

    choice = 'wrong'

    while choice not in possibleChoices :

        display_board(board1, board2, board3)
        
        choice = int(input("Pick a position: "))        

        if choice not in possibleChoices:
            print("Posição invalida!")
        else:
            possibleChoices.remove(choice)
            return int(choice)

def replace_choice(choice, player):
    if choice in [1,2,3]:
        board1.update({choice:player})
    if choice in [4,5,6]:
        board2.update({choice:player})
    if choice in [7,8,9]:
        board3.update({choice:player})

def check_game_finish():

    global statusGame
    if statusGame:
        
        for linha in (board1, board2, board3):
            if list(linha.values()) == ['X', 'X', 'X']:
                statusGame = False
                return print("Player X WINS!!!"), statusGame

            if list(linha.values()) == ['O', 'O', 'O']:
                statusGame = False
                return print("Player O WINS!!!"), statusGame

        for coluna in range(1,4):
            if list(board1[coluna]) + list(board2[coluna + 3]) + list(board3[coluna + 6]) == ['X', 'X', 'X']:
                statusGame = False
                return print("Player X WINS!!!"), statusGame
            
            if list(board1[coluna]) + list(board2[coluna+3]) + list(board3[coluna+6]) == ['O', 'O', 'O']:
                statusGame = False
                return print("Player O WINS!!!"), statusGame

        if list(board1[1]) + list(board2[5]) + list(board3[9]) == ['X', 'X', 'X']:
            statusGame = False
            return print("Player X WINS!!!"), statusGame

        if list(board1[3]) + list(board2[5]) + list(board3[7]) == ['X', 'X', 'X']:
            statusGame = False
            return print("Player X WINS!!!"), statusGame

        if list(board1[1]) + list(board2[5]) + list(board3[9]) == ['O', 'O', 'O']:
            statusGame = False
            return print("Player O WINS!!!"), statusGame

        if list(board1[3]) + list(board2[5]) + list(board3[7]) == ['O', 'O', 'O']:
            statusGame = False
            return print("Player O WINS!!!"), statusGame

        if len(possibleChoices) == 0:
            statusGame = False
            display_board(board1, board2, board3)
            return print("EMPATE!!!"), statusGame

def game_run():

    while statusGame:
        run()

def run():
    turns_alternator()
    replace_choice(position_choice(), player)
    check_game_finish()


game_run()