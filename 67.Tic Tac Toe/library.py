import os

scores = {
    'px_score': 0,
    'po_score': 0,
    'nul': 0
}

welcome = '''
  _______ _        _______           _______         
 |__   __(_)      |__   __|         |__   __|        
    | |   _  ___     | | __ _  ___     | | ___   ___ 
    | |  | |/ __|    | |/ _` |/ __|    | |/ _ \ / _ 
    | |  | | (__     | | (_| | (__     | | (_) |  __/
    |_|  |_|\___|    |_|\__,_|\___|    |_|\___/ \___|
'''

game = [["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]]


def show_game():
    print(f"\n X: {scores['px_score']}   Draws: {scores['nul']}    O: {scores['po_score']} \n")
    print('       |       |       ')
    print(f'   {game[0][0]}   |   {game[0][1]}   |   {game[0][2]}   ')
    print('_______|_______|_______')
    print('       |       |       ')
    print(f'   {game[1][0]}   |   {game[1][1]}   |   {game[1][2]}   ')
    print('_______|_______|_______')
    print('       |       |       ')
    print(f'   {game[2][0]}   |    {game[2][1]}  |   {game[2][2]}   ')
    print('       |       |       ')


def update_game(index, symbol):
    for row in range(len(game)):
        for element in range(len(game[row])):
            if index == game[row][element]:
                game[row][element] = symbol


def test_draw():
    draw = True
    for row in range(len(game)):
        for element in range(len(game[row])):
            if game[row][element] != 'X' and game[row][element] != 'O':
                draw = False
                break
    return draw


def test_win(player):
    # Check diagonal lines
    diago1 = True
    diago2 = True
    for i in range(len(game)):
        if game[i][i] not in player:
            diago1 = False
        if game[i][len(game) - i - 1] not in player:
            diago2 = False
    if diago1 or diago2:
        return True

    # Check rows and columns
    for i in range(len(game)):
        row = True
        col = True
        for j in range(len(game)):
            if game[i][j] not in player:
                row = False
            if game[j][i] not in player:
                col = False
        if row or col:
            return True

    return False


def is_valid_input(the_input):
    try:
        position = int(the_input)
    except ValueError:
        return False
    # Check if position is within the range of the game board
    if position < 1 or position > 9:
        return False
    # Check if the position is already occupied by a symbol
    row, col = from_pos_to_row_col(position)
    if game[row][col] == 'X' or game[row][col] == 'O':
        return False
    return True


def from_pos_to_row_col(position):
    row = (position - 1) // 3
    col = (position - 1) % 3
    return row, col


def victory(player):
    global scores
    if player == 'X':
        scores['px_score'] += 1
        print(f"Player {player} wins ! ")
    elif player == 'O':
        scores['po_score'] += 1
        print(f"Player {player} wins ! ")
    else:
        scores['nul'] += 1
        print(f"Draw..😒")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
