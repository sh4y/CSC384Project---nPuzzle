import random

class Problem:
     def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

class Board:
    def __init__(self, empty_block_position, positions):
        self.block = empty_block_position
        self.positions = positions

    def successors(self):
        corners = [(0,0), (4,0), (0,4), (4,4)]
        succ = []
        if self.block in corners:
            if self.block == (0,0):
                temp = self.positions   
                                      
        


    def create_random_board(self):
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
        #print(positions)
        return b
                       
            

class Node:
    
    def __init__(self, value, position):
    #value = int, position = tuple(x,y)
        self.val = value
        self.pos = position

    def __repr__(self):
        return ("(x: " + str(self.pos[0]) + ", y: " + str(self.pos[1]) + ", value = " + str(self.val) + ")\n")
    
