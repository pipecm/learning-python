cross = 'X'
nought = 'O'
game_board = ['#'] + [str(x) for x in range(1, 10)]
winner_combinations = [
    {1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7},
    {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}
]


def clear(board):
    for position in range(1, 10):
        board[position] = ' '


def display(board):
    print("\n")
    print(" {} | {} | {} ".format(board[1], board[2], board[3]))
    print("-----------")
    print(" {} | {} | {} ".format(board[4], board[5], board[6]))
    print("-----------")
    print(" {} | {} | {} ".format(board[7], board[8], board[9]))
    print("\n")


def create_players():
    player_one = {'name': None, 'mark': None, 'plays': set()}
    player_two = {'name': None, 'mark': None, 'plays': set()}

    while not player_one['name']:
        player_one['name'] = input("Player 1: Enter your name: ")
        if not player_one['name']:
            print("Please enter a non-null name!")

    print("Hello, {}".format(player_one['name']))

    while player_one['mark'] not in (cross, nought):
        player_one['mark'] = input("Choose your mark (X or O): ").upper()
        if player_one['mark'] not in (cross, nought):
            print("Invalid mark!")

    print("Good job, {}. You chose {}".format(player_one['name'], player_one['mark']))

    while not player_two['name']:
        player_two['name'] = input("Player 2: Enter your name: ")
        if not player_two['name']:
            print("Please enter a non-null name!")

    player_two['mark'] = cross if player_one['mark'] == nought else nought
    print("Hello, {}. You will play with {}".format(player_two['name'], player_two['mark']))

    return player_one, player_two


def play(player, board):
    position = 0
    selection_ok = False
    print(player['name'])

    while position not in range(1, 10) and not selection_ok:
        position = int(input("Select the position for your next move: "))
        if position not in range(1, 10):
            print("Invalid position!")
        elif board[position] in (cross, nought):
            print("The position {} is already busy. Select other position!".format(position))
            position = 0
        else:
            board[position] = player['mark']
            player['plays'].add(position)
            selection_ok = True


def has_won(player):
    for combination in winner_combinations:
        if combination.issubset(player['plays']):
            return True
    return False


def have_tied(board):
    for position in range(1, 10):
        if board[position] not in (cross, nought):
            return False
    return True


running = True

while running:
    finished = False

    print("Welcome to Tic-Tac-Toe!")
    print("-----------------------")

    display(game_board)
    players = create_players()
    clear(game_board)

    while not finished:
        for player in players:
            display(game_board)
            play(player, game_board)
            if has_won(player):
                print("{} wins!".format(player['name']))
                finished = True
                break
            elif have_tied(game_board):
                print("There is a tie!")
                finished = True
                break

    display(game_board)
    running = False
