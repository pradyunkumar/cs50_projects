"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None

class Node:
    def __init__(self, move, value):
        self.move = move
        self.value = value


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount = 0
    ocount = 0
    for row in board:
        for square in row:
            if square == X:
                xcount += 1
            elif square == O:
                ocount += 1
    
    if xcount > ocount:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of actions.
    """
    moves = set()
   
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not a Valid Move")
    else:
        theoretical = copy.deepcopy(board)
        theoretical[action[0]][action[1]] = player(board)
        return theoretical 


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return row[i][0]
    
    if (board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2]) and board[1][1] is not EMPTY:
        return board[1][1]
    else:
        return None
        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    thewinner = winner(board)
    if thewinner is X:
        return 1
    elif thewinner is O:
        return -1
    else:
        return 0

def minimax(board):

    if terminal(board):
        return None

    if player(board) is X:
        bestscore = float("-inf")
    else:
        bestscore = float("inf")

    bestmove = None

    for action in actions(board):
        thescore = score(result(board, action))
        if (player(board) is X and thescore > bestscore) or (player(board) is O and thescore < bestscore):
            bestscore = thescore
            bestmove = action

    return bestmove

def score(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board)

    if player(board) is X:
        theMax = float("-inf")

        for action in actions(board):
            theMax = max(theMax, score(result(board, action)))
        return theMax

    else:
        theMin = float("inf")

        for action in actions(board):
            theMin = min(theMin, score(result(board, action)))
        return theMin
