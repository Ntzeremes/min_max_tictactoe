""" This module contains all the minmax algorithms for the game."""
import copy
import time


def player(board):
    x = 0
    o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                x += 1
            elif board[i][j] == "O":
                o += 1
    if x == o:
        return "X"
    else:
        return "O"


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == "X" or board[i][0] == "O":
                return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "X" or board[0][i] == "O":
                return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == "X" or board[1][1] == "O":
            return board[1][1]

    return None


def game_over(board):
    winner = check_winner(board)
    if winner:
        return True

    for i in range(3):
        if "#" in board[i]:
            return False
    return True


def actions(board):
    action_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == "#":
                action_set.add((i, j))
    return action_set


def utility(board):
    winner = check_winner(board)
    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    else:
        return 0


def result(board, action, player):
    new = copy.deepcopy(board)
    new[action[0]][action[1]] = player
    return new


def minmax(board):
    """Minmax algorithm for the 3x3 game, it is not depth limited."""

    if game_over(board):
        return utility(board), None

    turn = player(board)

    if turn == "X":
        max_utility = -10
        action = None
        for a in actions(board):
            current_utility, _ = minmax(result(board, a, "X"))
            if current_utility > max_utility:
                max_utility = current_utility
                action = a

        return max_utility, action
    else:
        min_utility = 10
        action = None
        for a in actions(board):
            current_utility, _ = minmax(result(board, a, "O"))
            if current_utility < min_utility:
                min_utility = current_utility
                action = a

        return min_utility, action


def algo_tester():
    """this function tests all the algorithms of this module on some test boards.
    it returns the best action for each board and the time it took to calculate it."""

    tables = [[["#", "O", "#"],
               ["#", "X", "#"],
               ["#", "#", "#"]],

              [["O", "#", "X"],
               ["#", "X", "#"],
               ["#", "#", "#"]],

              [["#", "#", "#"],
               ["#", "#", "#"],
               ["#", "#", "#"]],

              [["X", "O", "#"],
               ["#", "X", "#"],
               ["#", "#", "#"]],

              [["#", "#", "#"],
               ["#", "X", "#"],
               ["#", "#", "#"]],

              [["X", "#", "O"],
               ["O", "X", "X"],
               ["#", "#", "O"]]
              ]

    for i, table in enumerate(tables):
        start = time.time()
        action = minmax(table)
        end = time.time()

        print(f"for table {i + 1} best action is {action} and total time is {end - start} sec.")


test = [["X", "O", "#"],
        ["#", "X", "#"],
        ["#", "#", "#"]]

algo_tester()


