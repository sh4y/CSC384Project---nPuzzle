import random

class Problem:
     def __init__(self, initial, goal = None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

class Board:
    def __init__(self, empty_block_position, positions):
        self.block = empty_block_position
        self.positions = positions
    
    #board is a dictionary of node positions
    #a,b are (x,y) tuples
    #assumes that a,b are definitely in board
    def swap_positions(self, a, b, board):
        a_node = board[a]        
        b_node = board[b]
        #a_node must be in pos b
        #b_node must be in pos a
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
                    print("swapped positions: ", temp)
                    succ.append("Possible successor:")
                    succ.append(temp)            
                
            elif self.block == (4,0):
                possible_empty_squares = [(4,1), (3,0)]
                #top right
                for pos in possible_empty_squares:
                    temp = self.positions
                    self.swap_positions(self.block, pos, temp)
                    print("swapped positions: ", temp)
                    succ.append("Possible successor:")

                    succ.append(temp)                        
            elif self.block ==(0,4):
                possible_empty_squares = [(0,3), (4,1)]
                #bottom left
                for pos in possible_empty_squares:
                    temp = self.positions
                    self.swap_positions(self.block, pos, temp)
                    print("swapped positions: ", temp)
                    succ.append("Possible successor:")
                    succ.append(temp)  
            elif self.block == (4,4):
                possible_empty_squares = [(3,3), (4,3)]
                for pos in possible_empty_squares:
                    temp = self.positions
                    self.swap_positions(self.block, pos, temp)
                    print("swapped positions: ", temp)
                    succ.append("Possible successor:")
                    succ.append(temp)  
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
                        succ.append("Possible successor:")
                        succ.append(temp)
                    except IndexError:
                        print("skipped edge case")
        return succ

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
    
a = Node(1, (0,1))
b = Node(0, (0,0)) #empty block
c = Node(2, (1,0))
d = Node(3, (1,1))
bo = Board((0,0),{(0,0):b, (0,1):a, (1,0):c, (1,1):d})
#bo.successors()
while True:
    b1 = create_random_board()
    print(b1.successors())
