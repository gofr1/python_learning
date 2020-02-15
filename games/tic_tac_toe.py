# tic-tak-toe game

from math import pow

X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'Tie'
ROWS_NUMBER = 5
NUM_SQUARES = int(pow(ROWS_NUMBER,2))
SQUARES_TO_WIN = 3 if ROWS_NUMBER in range(3,10) else 5

def ask_yes_no(question):
    """Ask yes/no question"""
    responce = None
    while responce not in ('y', 'n'):
        responce = input(question).lower()
    return responce

def ask_number(question, low, high):
    """Ask to enter a number from some range"""
    responce = None
    while responce not in range(low, high):
        responce = int(input(question))
    return responce

def who_go_first():
    """Let's choose who will go first"""
    go_first = ask_yes_no("Do you want to go first? (y/n): ")
    if go_first == 'y':
        human = X
        computer = O
    else:
        human = O
        computer = X
    return computer, human

def board():
    """Creates a game board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board, help=None):
    '''Display a current game board'''
    
    print('\n')
    for i in range(0, NUM_SQUARES, ROWS_NUMBER):
        row = ' '
        line = '-----'*ROWS_NUMBER
        for n in range(ROWS_NUMBER):
            row = row + '{: ^4}'.format(board[i+n] if help == None else str(i+n)) + '|'
        print(row[:-1])
        print(line)


def legal_moves(board):
    """Creates a list of legal moves for current board"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Check who wins"""
    ways_to_win = []
    # TODO: make it works for any board
    return(ways_to_win)

new_board = board()
winner(new_board)
display_board(new_board, 0)