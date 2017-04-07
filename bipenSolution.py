from search import *
from nPuzzle import *
from eightPuzzle import *
from fifteenPuzzle import *
from search import *
import sys
import math


def heur_n_maxswap(state):
    """
        https://heuristicswiki.wikispaces.com/N-MaxSwap
    """
    hval = 1
    goal = state.get_goal_state()
    P = list(state.hashable_state())

    # Replace empty tile with n+1
    largest_number = max(P)
    P[P.index(-1)] = largest_number + 1
    goal[-1] = largest_number + 1

    # Create and populate B array
    B = [-1] * (largest_number + 1)
    B = populate_b(largest_number, B, P)

    # Until we reach the goal state, swap iteratively P[B[n]] with P[B[B[n]]]
    while P != goal:
        # Increase number of steps taken
        hval += 1

        # The Swap
        P[B[largest_number]], P[B[B[largest_number]]] = P[B[B[largest_number]]], P[B[largest_number]]

        # Repopulate B with new location of values
        B = populate_b(largest_number, B, P)

    return hval


def populate_b(largest_number , B, P):
    """ ~~HELPER~~
        Populates array B with the location of index i in array P, up to the largest_number
        Ex, Given:
         largest_number = 15
         P = [15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 16, 13, 14, 12]
         B = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        Will return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 13, 14, 0, 12]
        :param largest_number:
        :param B:
        :param P:
        :return B:
    """
    i = 0

    while i <= largest_number:
        B[i] = P.index(i+1)
        i += 1

    return B


def heur_tiles_out_of_row_and_column(state):
    """
    https://heuristicswiki.wikispaces.com/Tiles+out+of+row+and+column
    """
    hval = 0
    goal = state.get_goal_state()
    cstate = state.state_string()

    current_state = []
    current_row = []

    # Turn the given state into a workable string
    for tile in cstate.split(" "):
        if not (tile == "" or tile == " " or tile == "\n"):
            if "\n" in tile:  # If the current number has newline attached, remove newline and separate into new row
                current_state.append(current_row)
                current_row = []
                tile = tile.replace("\n", "")

            if tile == "_":  # Turn blank tiles into -1
                current_row.append(-1)
            else:  # Add current tile to current row
                current_row.append(int(tile))

    current_state.append(current_row)

    # Number of tiles per row
    n = int(math.sqrt(max(goal) + 1))

    # Modify goal to be same format as the state
    goal_state = [goal[i:i + n] for i in range(0, len(goal), n)]

    # Compare goal_state and current_state rows
    i = 0

    for row in current_state:
        for tile in row:
            if tile != -1 and tile not in goal_state[i]:
                hval += 1
        i += 1
    i = 0
    # Transpose goal_state and theState to now compare columns
    goal_state = list(map(list, zip(*goal_state)))
    current_state = list(map(list, zip(*current_state)))

    # Compare goal_state and current_state cols
    for col in current_state:
        for tile in col:
            if tile != -1 and tile not in goal_state[i]:
                hval += 1
        i += 1

    return hval


#test = fifteenPuzzleState("START", 0, None, [-1, 12, 9, 13, 15, 11, 10, 14, 3, 7, 2, 5, 4, 8, 6, 1])
#test = fifteenPuzzleState("START", 0, None, [15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1, 13, 14, 12])
#test = fifteenPuzzleState("START", 0, None, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 13, 14, 12, -1])
test = eightPuzzleState("START", 0, None, [2, -1, 6, 1, 3, 4, 7, 5, 8])

#print(heur_tiles_out_of_row_and_column(test))
print(heur_n_maxswap(test))