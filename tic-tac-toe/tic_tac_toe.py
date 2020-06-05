game_board = {
    'p1': '1', 'p2': '2', 'p3': '3',
    'p4': '4', 'p5': '5', 'p6': '6',
    'p7': '7', 'p8': '8', 'p9': '9'
}

winner_combinations = [
    {'p1', 'p2', 'p3'},
    {'p4', 'p5', 'p6'},
    {'p7', 'p8', 'p9'},
    {'p1', 'p4', 'p7'},
    {'p2', 'p5', 'p8'},
    {'p3', 'p6', 'p9'},
    {'p1', 'p5', 'p9'},
    {'p3', 'p5', 'p7'}
]

cross = 'X'
nought = 'O'


def clear(board):
    for position in board.keys():
        board[position] = ' '


def display(board):
    print("\n")
    print(" {} | {} | {} ".format(board['p1'], board['p2'], board['p3']))
    print("-----------")
    print(" {} | {} | {} ".format(board['p4'], board['p5'], board['p6']))
    print("-----------")
    print(" {} | {} | {} ".format(board['p7'], board['p8'], board['p9']))
    print("\n")


def create_players():
    player_one = {'name': None, 'symbol': None, 'plays': set()}
    player_two = {'name': None, 'symbol': None, 'plays': set()}

    while not player_one['name']:
        player_one['name'] = input("Player 1: Enter your name: ")
        if not player_one['name']:
            print("Please enter a non-null name!")

    print("Hello, {}".format(player_one['name']))

    while player_one['symbol'] not in (cross, nought):
        player_one['symbol'] = input("Choose your symbol (X or O): ").upper()
        if player_one['symbol'] not in (cross, nought):
            print("Invalid symbol!")

    print("Good job, {}. You chose {}".format(player_one['name'], player_one['symbol']))

    while not player_two['name']:
        player_two['name'] = input("Player 2: Enter your name: ")
        if not player_two['name']:
            print("Please enter a non-null name!")

    player_two['symbol'] = cross if player_one['symbol'] == nought else nought
    print("Hello, {}. You will play with {}".format(player_two['name'], player_two['symbol']))

    return player_one, player_two


def has_won(player):
    for combination in winner_combinations:
        if combination.issubset(player['plays']):
            return True
    return False


def have_tied(board):
    for position in board.keys():
        if board[position] not in (cross, nought):
            return False
    return True


def play(player, board):
    position = 0
    selection_ok = False
    print(player['name'])

    while position not in range(1, 10) and not selection_ok:
        position = int(input("Select the position for your next move: "))
        if position not in range(1, 10):
            print("Invalid position!")
        elif board['p{}'.format(position)] in (cross, nought):
            print("The position {} is already busy. Select other position!".format(position))
            position = 0
        else:
            board['p{}'.format(position)] = player['symbol']
            player['plays'].add('p{}'.format(position))
            selection_ok = True

# main program


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
