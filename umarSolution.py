from search import *
from nPuzzle import *
from eightPuzzle import *
from fifteenPuzzle import *
from search import *
import sys

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


def heur_misplaced_tiles(state):
    """
    https://heuristicswiki.wikispaces.com/Misplaced+Tiles
    """
    hval = 0
    size = state.size
    goal = state.get_goal_state()
    for idx in range(0, size**2):
        if goal[idx] is not state.positions[idx] and state.positions[idx] is not -1:
            hval += 1
    return hval

def linear_conflict(state):
    """
    https://heuristicswiki.wikispaces.com/Linear+Conflict
    :param state:
    :return:
    """
    return 0

def idastar(initial_state, heur_fn, timebound=10):
    """
    Need to do a DFS and cut off things based on f-value (g + h)
    At each iteration of the search, the cutoff value becomes the smallest f-value that exceeded the cutoff in last iteration
    curBound = an f-value such that any node with a larger f-value is pruned
    smallestNotExplored =
    """
    timeleft = timebound

    se = SearchEngine('depth_first', 'full')
    solution = False
    #let's just start costbound at f-val of initial_state (g-val is 0 so just h-val of initial_state)
    costbound = (sys.maxsize, sys.maxsize, heur_fn(initial_state))
    init_time = os.times()[0]

    while timeleft > 0:
        se.init_search(initial_state, goal_fn=npuzzle_goal_state, heur_fn=heur_fn)
        solution = se.search(timeleft, costbound=costbound)

        if solution:
            print("Total time elapsed for all iterations of IDA*:", timebound - timeleft)
            return solution

        # introduce a cost bound for pruning
        costbound = (sys.maxsize, sys.maxsize, se.smallestNotExplored)
        timeleft -= (os.times()[0] - init_time)
        init_time = os.times()[0]

    print("Total time elapsed for all iterations of IDA*: {}", timebound - timeleft)
    return solution

#test = fifteenPuzzleState("START", 0, None, [-1, 12, 9, 13, 15, 11, 10, 14, 3, 7, 2, 5, 4, 8, 6, 1])
#x = idastar(test, heur_fn=heur_manhattan_distance, timebound=1000)

