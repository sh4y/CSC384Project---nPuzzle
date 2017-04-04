from search import *

class fifteenPuzzleState(StateSpace):
    def __init__(self, action, gval, parent, positions):
        """
        :param size: The puzzles X dimension
        :param height: The puzzles Y dimension
        :param empty_block_position: The index where the blank (the -1) is
        :param positions: A list of size (x*y) that shows the current order | -1 = blank
        """
        StateSpace.__init__(self, action, gval, parent)
        self.empty_block_position = positions.index(-1)
        self.positions = positions
        self.size = 4

    def successors(self):
        successors = []
        transition_cost = 1

        """
        You can move down if you're anywhere but the top row. You can move up if you're anywhere but the bottom row.
        You can move right if you're anywhere but the right column. You can move left if you're anywhere but the left column.

        INDICES:
        0 1 2 3
        4 5 6 7
        8 9 10 11
        12 13 14 15

        delta's: up = size * -1, down = size, left = -1, right = 1
        """
        #UP
        if self.empty_block_position >= 4:
            new_positions = move_and_swap(self.positions.copy(), self.empty_block_position, -4)
            new_state = fifteenPuzzleState(action="UP", gval=self.gval + transition_cost, parent=self, positions=new_positions)
            successors.append(new_state)

        #DOWN
        if self.empty_block_position <= 11:
            new_positions = move_and_swap(self.positions.copy(), self.empty_block_position, 4)
            new_state = fifteenPuzzleState(action="DOWN", gval=self.gval + transition_cost, parent=self, positions=new_positions)
            successors.append(new_state)

        #LEFT
        if self.empty_block_position not in [0,4,8,12]:
            new_positions = move_and_swap(self.positions.copy(), self.empty_block_position, -1)
            new_state = fifteenPuzzleState(action="LEFT", gval=self.gval + transition_cost, parent=self, positions=new_positions)
            successors.append(new_state)

        #RIGHT
        if self.empty_block_position not in [3,7,11,15]:
            new_positions = move_and_swap(self.positions.copy(), self.empty_block_position, 1)
            new_state = fifteenPuzzleState(action="RIGHT", gval=self.gval + transition_cost, parent=self, positions=new_positions)
            successors.append(new_state)

        return successors

    def hashable_state(self):
        return tuple(self.positions)

    def state_string(self):
        """
        Return a string representation of a state that can be printed to stdout.
        """
        s = ""
        for i in range(1, len(self.positions) + 1):
            number = "_" if self.positions[i - 1] is -1 else str(self.positions[i - 1])
            if i % self.size is 0:
                end = "\n"
            else:
                if(number is not "_") and (int(number) > 9):
                    end = ''
                else:
                    end = ' '
            s += number + " " + end

        return s

    def print_state(self):
        print("ACTION was " + self.action)
        print(self.state_string())

    def get_goal_state(self):
        return [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,-1]

def move_and_swap(pos, eb_pos, delta):
    pos[eb_pos], pos[eb_pos + delta] = pos[eb_pos + delta], pos[eb_pos]
    return pos

def eightpuzzle_goal_state(state):
    """
    Return True if we have reached a goal state.

    :param state: a nPuzzle state
    :return: True (if goal) or False (if not)
    """
    return state.positions == state.get_goal_state()

test = fifteenPuzzleState("START", 0, None, [2,9,3,4,12,-1,10,5,15,1,14,8,6,13,11,7])
print(test.state_string())
for x in test.successors():
    print(x.state_string())