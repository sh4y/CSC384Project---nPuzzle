import random
from search import *
import math

class Board(StateSpace):

    def board_goal_state():
        v = 1
        positions = {}
        for y in range(0,5):
            for x in range(0,5):
                pos = (x,y)
                if pos != (4,4):        
                    n = Node(v, pos)
                    positions[pos] = n
                    v+=1
        #empty block position must be in last slot (slot 25)
        n = Node(0, (4,4))
        positions[(4,4)] = n
        return positions

    def __init__(self, empty_block_position, positions, gval=0, parent=None, action="START"):
        StateSpace.__init__(self, action, gval, parent)
        self.block = empty_block_position
        self.positions = positions
        self.hval = self.heur_distance()
        Board.final_goal_state = Board.board_goal_state()
    
    #board is a dictionary of node positions
    #a,b are (x,y) tuples
    #assumes that a,b are definitely in board
    def swap_positions(self, a, b, board):
        a_node = board[a]        
        b_node = board[b]
        board.pop(a, None)
        board.pop(b, None)
        #update node positions
        a_node.pos = b  
        b_node.pos = a
        #update nodes
        board[b] = a_node       
        board[a] = b_node        

    def successors(self):
        corners = [(0,0), (4,0), (0,4), (4,4)]
        succ = []
        #if empty block is in one of the corners, there are only two possible
        #moves
        #rather than three
        if self.block in corners:
            print("Found block in corner")
            print("Positions:",self.positions) 
            if self.block == (0,0):
                possible_empty_squares = [(0,1), (1,0)]
                #top left
                for pos in possible_empty_squares:
                    temp = self.positions
                    self.swap_positions(self.block, pos, temp)
                    self.block = pos
                    b = Board(self.block, temp,action="MOVE")
                    succ.append(b)            
                
            elif self.block == (4,0):
                possible_empty_squares = [(4,1), (3,0)]
                #top right
                for pos in possible_empty_squares:
                    temp = self.positions
                    self.swap_positions(self.block, pos, temp)
                    self.block = pos
                    b = Board(self.block, temp,action="MOVE")
                    succ.append(b)  
                                          
            elif self.block == (0,4):
                possible_empty_squares = [(0,3), (4,1)]
                #bottom left
                for pos in possible_empty_squares:
                    temp = self.positions
                    self.swap_positions(self.block, pos, temp)
                    self.block = pos
                    b = Board(self.block, temp,action="MOVE")
                    succ.append(b)  

            elif self.block == (4,4):
                possible_empty_squares = [(3,3), (4,3)]
                for pos in possible_empty_squares:
                    temp = self.positions
                    self.swap_positions(self.block, pos, temp)
                    print("swapped positions: ", temp)
                    self.block = pos
                    b = Board(self.block, temp,action="MOVE")
                    succ.append(b) 
        else:  
            #any other square
            print("Found block, not in corner")
            x,y = self.block[0], self.block[1]
            moves = [(x - 1, y),(x,y - 1),(x,y + 1),(x + 1,y)]
            for move in moves:
                if (move[0] != -1) and (move[0] != 5) and (move[1] != -1) and (move[1] != 5):
                    try:    
                        temp = self.positions
                        self.swap_positions(move, self.block, temp)
                        self.block = move
                        b = Board(self.block, temp,action="MOVE")
                        succ.append(b)
                    except IndexError:
                        print("skipped edge case")
        return succ

    def hashable_state(self):
        return hash(frozenset(self.positions.items()))

    def print_state(self):
        print(self.positions)

    def distance(a,b):
        return math.sqrt( pow(abs(b[0] - a[0]), 2) + pow(abs(b[1] - a[1]), 2) )

    def is_goal_state(self):
        return Board.final_goal_state == self.positions


    def heur_distance(self):
        goal_state = Board.board_goal_state()
        goal_val = 1
        result = 0
        #for each tile in the positions dict
        for pos in self.positions:
            #get the node value
            node_val = self.positions[pos].val
            #if the node value at the tile is not the same as the goal value
            if node_val != goal_val:
                #iterate through the goal state to find the matching tile
                for goal in goal_state:
                    g_val = goal_state[goal].val
                    #if the tile values match
                    if g_val == node_val:
                        a = goal
                        b = pos
                        #calculate the distance between the two tiles
                        result += Board.distance(a,b)
                        g_val += 1



def create_random_board():
        nums = [x for x in range(0,25)]
        positions = {}
        ebp = None
        for y in range(0,5):
            for x in range(0,5):
                pos = (x,y)
                val = random.choice(nums)
                nums.remove(val)
                n = Node(val, pos)
                positions[pos] = n
                if val == 0:
                    ebp = pos
        b = Board(ebp, positions)       
        return b
                              

class Node:
    
    def __init__(self, value, position):
    #value = int, position = tuple(x,y)
        self.val = value
        self.pos = position


    def __repr__(self):
        return ("(x: " + str(self.pos[0]) + ", y: " + str(self.pos[1]) + ", value = " + str(self.val) + ")\n")

def anytime_weighted_astar(initial_state, heur_fn, weight=1., timebound = 10):
#IMPLEMENT
    '''Provides an implementation of anytime weighted a-star, as described in the HW1 handout'''
    '''INPUT: a sokoban state that represents the start state and a timebound (number of seconds)'''
    '''OUTPUT: A goal state (if a goal is found), else False''' 
    
    currtime = time.time()
    endtime = currtime + timebound
    startstate = initial_state
    found = False
    restart = None
    
    timeleft = endtime - time.time()
    se = SearchEngine('custom', 'full')
    
    se.init_search(startstate, goal_fn=sokoban_goal_state,
                    heur_fn=heur_fn, fval_function=lambda sN: fval_function(sN, weight))
    
    final = se.search(timeleft)

    while time.time() < endtime:
  
      if final:
        found = True

      if found:
        fingval = final.gval
        finhval = heur_fn(final)

        timeleft = endtime - time.time()
        #se.init_search(startstate, goal_fn=sokoban_goal_state,
        #heur_fn=heur_fn, fval_function= (lambda sN: fval_function(sN, weight)

        restart = se.search(timeleft, (sys.maxsize, sys.maxsize, fingval + finhval))

        if restart:
          final = restart
          
    return final
   
'''a = Node(1, (0,1))
b = Node(0, (0,0)) #empty block
c = Node(2, (1,0))
d = Node(3, (1,1))
bo = Board((0,0),{(0,0):b, (0,1):a, (1,0):c, (1,1):d})
#bo.successors()
while True:
    b1 = create_random_board()
    print(b1.successors())'''

b1 = create_random_board()
se = SearchEngine('astar', 'full')
se.init_search(b1, goal_fn=Board.is_goal_state,heur_fn=Board.heur_distance)
final = se.search(1000000000)
