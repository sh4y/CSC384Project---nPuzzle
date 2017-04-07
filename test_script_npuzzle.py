from nPuzzle import *
from eightPuzzle import *
from fifteenPuzzle import *
from solution import *
from umarSolution import *

#just some sample problems, ordered in (perceived) difficulty
eight_puzzle_problems = (
    eightPuzzleState("START", 0, None, [5, 2, 1, 4, 8, 3, 7, 6, -1]), #16
    eightPuzzleState("START", 0, None, [1, 4, 3, 7, -1, 8, 6, 5, 2]), #18
    eightPuzzleState("START", 0, None, [6, -1, 8, 4, 3, 5, 1, 2, 7]), #23
    eightPuzzleState("START", 0, None, [1, 6, 4, -1, 3, 5, 8, 2, 7]), #27
    eightPuzzleState("START", 0, None, [6, 3, 8, 5, 4, 1, 7, 2, -1]), #28
    eightPuzzleState("START", 0, None, [1, 8, 5, -1, 2, 4, 3, 6, 7]), #29
    eightPuzzleState("START", 0, None, [8, 6, 7, 2, -1, 4, 3, 5, 1]), #30
    eightPuzzleState("START", 0, None, [8, 6, 7, 2, 5, 4, 3, -1, 1]), #31

)

#these take 31 moves!
hardest_8_puzzle = (
    eightPuzzleState("START", 0, None, [8, 6, 7, 2, 5, 4, 3, -1, 1]),
    eightPuzzleState("START", 0, None, [6, 4, 7, 8, 5, -1, 3, 2, 1]),
)

#started from a solved, did a few steps to get to these
fifteen_puzzle_problems = (
    fifteenPuzzleState("START", 0, None, [2, 5, 3, 4, 1, 7, 11, 8, 9, 6, -1, 12, 13, 14, 15, 10]), #18
    fifteenPuzzleState("START", 0, None, [1, 2, 3, 4, 5, 6, 14, 8, 13, -1, 9, 11, 10, 12, 15, 7]), #23
    fifteenPuzzleState("START", 0, None, [1, 10, 6, 4, 5, 9, 2, 8, 13, 12, -1, 7, 14, 11, 3, 15]), #26
    fifteenPuzzleState("START", 0, None, [5, 1, 3, 2, 10, 6, 15, 7, 9, 8, 11, 4, -1, 13, 14, 12]), #31
    fifteenPuzzleState("START", 0, None, [9, 5, 8, 3, 6, -1, 10, 11, 2, 1, 14, 7, 13, 15, 12, 4]), #34
    fifteenPuzzleState("START", 0, None, [5, 9, 1, 3, -1, 11, 2, 7, 10, 13, 12, 4, 6, 15, 8, 14]), #37
    fifteenPuzzleState("START", 0, None, [13, 11, 9, 3, 14, 7, 1, 4, -1, 5, 10, 12, 15, 2, 6, 8]), #46
    fifteenPuzzleState("START", 0, None, [7, 8, 1, 10, 2, 4, 5, 13, -1, 9, 3, 6, 11, 14, 15, 12]), #48

)

#these will take 80 moves!
#source: http://kociemba.org/fifteen/fifteensolver.html
hardest_15_puzzle = (
    fifteenPuzzleState("START", 0, None, [-1, 12, 9, 13, 15, 11, 10, 14, 3, 7, 2, 5, 4, 8, 6, 1]),
    fifteenPuzzleState("START", 0, None, [-1, 12, 10, 13, 15, 11, 14, 9, 3, 7, 2, 5, 4, 8, 6, 1]),
    fifteenPuzzleState("START", 0, None, [-1, 12, 14, 13, 15, 11, 9, 10, 8, 3, 6, 2, 4, 7, 5, 1]),
)

sample_24_puzzle = (
    nPuzzleState("START", 0, None, 5, [1,2,3,4,5,6,17,23,24,13,11,8,15,18,10,16,22,9,12,20,21,14,7,19,-1]),
    nPuzzleState("START", 0, None, 5, [1,2,3,4,5,6,7,-1,9,10,11,13,8,14,15,16,12,17,18,19,21,22,23,24,20]),
)
"""
TESTING:
Change this to fit whatever tests you want.
"""
#Select what to test
print_problems = False
test_alternate = True
use_idastar = False


if print_problems:
    for x in eight_puzzle_problems:
        print(x.state_string())

#CHANGE TO WHATEVER LIST YOU WANNA USE
if test_alternate:
    for i in range(0, len(eight_puzzle_problems)):
        s0 = eight_puzzle_problems[i]

        if use_idastar is False:
            se = SearchEngine('astar', 'default')
            se.init_search(s0, goal_fn=npuzzle_goal_state, heur_fn=heur_manhattan_distance)
            final = se.search(timebound=1000)
        else:
            final = idastar(s0, heur_fn=heur_manhattan_distance, timebound=1000)

        if final:
            pass
            #final.print_path()
        else:
            print("didn't solve")