from nPuzzle import *
from eightPuzzle import *
from fifteenPuzzle import *
from solution import *

#just some sample problems, ordered in (perceived) difficulty
eight_puzzle_problems = (
    eightPuzzleState("START", 0, None, [1, 2, 3, 4, 5, -1, 7, 8, 6]),
    eightPuzzleState("START", 0, None, [1, 2, 3, -1, 4, 5, 7, 8, 6]),
    eightPuzzleState("START", 0, None, [1, -1, 2, 4, 6, 3, 7, 5, 8]),
    eightPuzzleState("START", 0, None, [1, 2, 3, -1, 4, 8, 7, 6, 5]),
    eightPuzzleState("START", 0, None, [1, 3, 6, 5, 2, 8, 4, -1, 7]),
    eightPuzzleState("START", 0, None, [3, 4, 6, 2, -1, 8, 1, 7, 5]),
    eightPuzzleState("START", 0, None, [5, 2, 1, 4, 8, 3, 7, 6, -1]),
    eightPuzzleState("START", 0, None, [1, 4, 3, 7, -1, 8, 6, 5, 2]),
)

#these take 31 moves!
hardest_8_puzzle = (
    eightPuzzleState("START", 0, None, [8, 6, 7, 2, 5, 4, 3, -1, 1]),
    eightPuzzleState("START", 0, None, [6, 4, 7, 8, 5, -1, 3, 2, 1]),
)

#started from a solved, did a few steps to get to these
fifteen_puzzle_problems = (
    fifteenPuzzleState("START", 0, None, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1, 13, 14, 15, 12]),
    fifteenPuzzleState("START", 0, None, [1, 2, 3, 4, 5, 6, -1, 8, 9, 10, 7, 12, 13, 14, 11, 15]),
    fifteenPuzzleState("START", 0, None, [1, 2, 3, 4, 5, 6, 7, 8, 10, -1, 11, 12, 9, 13, 14, 15]),
    fifteenPuzzleState("START", 0, None, [1, 2, 3, 4, 6, 10, 7, 8, 5, -1, 11, 12, 9, 13, 14, 15]),
    fifteenPuzzleState("START", 0, None, [5, 1, 2, 4, 9, 6, 3, 7, 13, 10, -1, 8, 14, 15, 11, 12]),
    fifteenPuzzleState("START", 0, None, [1, 2, 8, 3, 5, 11, 6, 4, -1, 10, 7, 12, 9, 13, 14, 15]),
    fifteenPuzzleState("START", 0, None, [5, 1, 2, 4, 6, -1, 10, 7, 13, 11, 3, 8, 14, 9, 15, 12]),
    fifteenPuzzleState("START", 0, None, [2, 5, 3, 4, 1, 7, 11, 8, 9, 6, -1, 12, 13, 14, 15, 10]),
)

#these will take 80 moves!
#source: http://kociemba.org/fifteen/fifteensolver.html
hardest_15_puzzle = (
    fifteenPuzzleState("START", 0, None, [-1, 12, 9, 13, 15, 11, 10, 14, 3, 7, 2, 5, 4, 8, 6, 1]),
    fifteenPuzzleState("START", 0, None, [-1, 12, 10, 13, 15, 11, 14, 9, 3, 7, 2, 5, 4, 8, 6, 1]),
    fifteenPuzzleState("START", 0, None, [-1, 12, 14, 13, 15, 11, 9, 10, 8, 3, 6, 2, 4, 7, 5, 1]),
)

sample_24_puzzle = (
    nPuzzleState("START", 0, None, 5, [3,22,14,20,17,2,21,23,13,15,7,16,12,8,1,10,5,9,19,24,11,4,6,18,-1]),
    nPuzzleState("START", 0, None, 5, [7,17,19,20,6,22,13,10,8,1,23,2,3,11,16,5,18,12,14,24,9,4,15,21,-1]),
)
"""
TESTING:
Change this to fit whatever tests you want.
"""
#Select what to test
print_problems = False
test_alternate = True


test = nPuzzleState("START", 0, None, 3, [2,-1,4,5,8,3,6,7,1])

if print_problems:
    for x in sample_24_puzzle:
        print(x.state_string())

if test_alternate:
    #CHANGE THIS TO DO W/E TEST YOU WANT TO DO!
    se = SearchEngine('best_first', 'full')
    se.init_search(test, goal_fn=npuzzle_goal_state, heur_fn=heur_manhattan_distance)
    final = se.search(timebound=1000)

    if final:
        final.print_path()
    else:
        print("didn't solve")