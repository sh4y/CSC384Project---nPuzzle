from search import *
from nPuzzle import *
from eightPuzzle import *
from fifteenPuzzle import *
from search import *
import sys
import math

def heur_x_minus_y(state):
    """
        https://heuristicswiki.wikispaces.com/X-Y
    """
    steps = 0
    print(state.state_string())
    size = state.size
    p_of_n = heur_manhattan_distance(state)
    goal = state.get_goal_state()
    curr_state = list(state.hashable_state())

    curr_state = [curr_state[i:i + size] for i in range(0, len(curr_state), size)]
    goal_state = [goal[i:i + size] for i in range(0, len(goal), size)]


    for row in curr_state:
        row.sort()
    for row in goal_state:
        row.sort()

    print(goal_state)
    print(curr_state)

    # Compute steps for rows
    # row_steps = compute_steps(size, goal_state, curr_state)
    print("Transposed")
    # Transpose goal_state and theState to now compare columns
    goal_state = list(map(list, zip(*goal_state)))
    curr_state = list(map(list, zip(*curr_state)))

    print(goal_state)
    print(curr_state)
    # Compute steps for cols
    col_steps = compute_steps(size, goal_state, curr_state)
    return col_steps


def compute_steps(size, goal_state, curr_state):
    steps = 0

    i = 0
    for row in curr_state:
        j = 0
        for num in row:
            if num == -1:
                blank = i, j
                break
            j += 1
        i += 1

    i = 5
    #while not row_or_col_check(size, goal_state, curr_state):
    while i > 0:
        print("Current State is: " + str(curr_state))
        if blank[0] > 0:
            #print("Step One")
            compared = compare_lists(curr_state[blank[0]-1], goal_state[blank[0]-1])
            if not compared[0]:
                #print("Inner Step One")
                steps += 1
                #print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tChanging " + str(curr_state))
                curr_state[blank[0]-1][compared[1]], curr_state[blank[0]][blank[1]] = \
                    curr_state[blank[0]][blank[1]], curr_state[blank[0]-1][compared[1]]
                #print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tTo       " + str(curr_state))
                blank = (blank[0]-1, compared[1])
        elif blank[0] < size:
            #print("Step Two")
            compared = compare_lists(curr_state[blank[0] + 1], goal_state[blank[0] + 1])
            if not compared[0]:
                #print("Inner Step Two")
                steps += 1
                #print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tChanging " + str(curr_state))
                curr_state[blank[0] + 1][compared[1]], curr_state[blank[0]][blank[1]] = \
                    curr_state[blank[0]][blank[1]], curr_state[blank[0] + 1][compared[1]]
                #print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tTo       " + str(curr_state))
                blank = (blank[0] + 1, compared[1])
        i -= 1
    return steps


def compare_lists(list1, list2):
    index = 0
    for ele in list1:
        if ele not in list2:
            return False, index
        index += 1
    return True, -1


def row_or_col_check(size, goal, cstate):
    i = 0
    while i < size:
        for ele in cstate[i]:
            if ele not in goal[i]:
                return False
        i += 1
    return True


def heur_sequence_score(state):
    """
        https://heuristicswiki.wikispaces.com/Nilsson%27s+Sequence+Score
    """
    print(state.state_string())
    print("Size: " + str(state.size))
    p_of_n = heur_manhattan_distance(state)
    print("p_of_n: " + str(p_of_n))
    goal = state.get_goal_state()
    print(goal)
    cstate = list(state.hashable_state())
    print(cstate)


    s_of_n = 0

    #for tile in cstate:

    return p_of_n + (3 * s_of_n)



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


def get_xy(size, idx):
    """ ~~HELPER~~
    Given size and index, will get you to the xy from a 1D list.
    Ex, [3, 4, 6, 2, -1, 8, 1, 7, 5] and we want xy of index 5 (which is 8)
     3 4 6
     2 _ 8
     1 7 5
    Will return (3,2)
    :param size:
    :param idx:
    :return:
    """
    x = idx % size + 1
    y = idx // size + 1
    return x, y


def heur_manhattan_distance(state):
    """
    https://heuristicswiki.wikispaces.com/Manhattan+Distance
    Manhattan distance of each tile from its current position to desired position in goal (not including blank)
    """
    hval = 0
    size = state.size
    goal = state.get_goal_state()
    for idx in range(0, size**2):
        if goal[idx] is not state.positions[idx] and state.positions[idx] is not -1:
            x1, y1 = get_xy(size, idx)

            goal_index = goal.index(state.positions[idx])
            x2, y2 = get_xy(size, goal_index)

            hval += (abs(x1 - x2) + abs(y1 - y2))
    return hval


#test = fifteenPuzzleState("START", 0, None, [-1, 12, 9, 13, 15, 11, 10, 14, 3, 7, 2, 5, 4, 8, 6, 1])
#test = fifteenPuzzleState("START", 0, None, [15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1, 13, 14, 12])
#test = fifteenPuzzleState("START", 0, None, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 13, 14, 12, -1])
test = eightPuzzleState("START", 0, None, [2, -1, 6, 1, 3, 4, 7, 5, 8])

#print(heur_tiles_out_of_row_and_column(test))
#print(heur_n_maxswap(test))
#print(heur_sequence_score(test))
print(heur_x_minus_y(test))