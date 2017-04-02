from nPuzzle import *

#just some sample problems, ordered in (perceived) difficulty
eight_puzzle_problems = (
    nPuzzleState("START", 0, None, 3, [1,2,3,4,5,6,7,-1,8]),

    nPuzzleState("START", 0, None, 3, [3,8,1,6,5,7,4,2,-1]),

    nPuzzleState("START", 0, None, 3, [5,6,1,3,8,-1,4,7,2])

)

#started from a solved, did a few steps to get to these
easy_problems = (
    nPuzzleState("START", 0, None, 5, [-1,2,3,4,1,6,7,8,5,10,11,12,9,13,14,15]),

    nPuzzleState("START", 0, None, 5, [1,2,7,3,5,6,11,4,9,-1,10,8,13,14,15,12]),

    nPuzzleState("START", 0, None, 5, [1,3,6,4,10,9,2,8,5,7,-1,12,13,14,11,15])
)

#these will take 80 moves!
#source: http://kociemba.org/fifteen/fifteensolver.html
hard_problems = (

    nPuzzleState("START", 0, None, 5, [-1,12,9,13,15,11,10,14,3,7,2,5,4,8,6,1]),

    nPuzzleState("START", 0, None, 5, [-1,12,10,13,15,11,14,9,3,7,2,5,4,8,6,1]),

    nPuzzleState("START", 0, None, 5, [-1,12,14,13,15,11,9,10,8,3,6,2,4,7,5,1])
)

#Select what to test
print_problems = True
test_alternate = False


test = nPuzzleState("START", 0, None, 3, [1,2,3,4,5,6,7,-1,8])

if print_problems:
    print(test.state_string())

if test_alternate:
    se = SearchEngine('best_first', 'full')
    se.init_search(test, goal_fn=npuzzle_goal_state)
    final = se.search()

    if final:
        final.print_path()
    else:
        print("didn't solve")