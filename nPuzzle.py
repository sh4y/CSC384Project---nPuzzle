from search import *

class nPuzzleState(StateSpace):
    def __init__(self, action, gval, parent, size, positions):
        """
        :param size: The puzzles X dimension
        :param height: The puzzles Y dimension
        :param empty_block_position: The index where the blank (the -1) is
        :param positions: A list of size (x*y) that shows the current order | -1 = blank
        """
        StateSpace.__init__(self, action, gval, parent)
        self.empty_block_position = positions.index(-1)
        self.positions = positions
        self.size = size

    def successors(self):
        successors = []
        transition_cost = 1

        # Directions
        UP = Direction("up", self.size * -1)
        RIGHT = Direction("right", 1)
        DOWN = Direction("down", self.size)
        LEFT = Direction("left", -1)

        for direction in (UP, RIGHT, DOWN, LEFT):
            new_location = direction.move(self.empty_block_position)

            if new_location < 0 or new_location >= len(self.positions):
                continue

            new_positions = direction.move_and_swap(self.positions.copy(), self.empty_block_position)

            if direction.name is "right" or direction.name is "left":
                if not self.in_same_row(self.positions, new_positions):
                    continue

            new_state = nPuzzleState(action=direction.name, gval=self.gval + transition_cost,
                                     parent=self, size=self.size,
                                     positions=new_positions)
            successors.append(new_state)

        return successors

    def in_same_row(self, old, new):
        old_matrix = [old[i:i + self.size] for i in range(0, len(old), self.size)]
        new_matrix = [new[i:i + self.size] for i in range(0, len(new), self.size)]
        xy1 = [(ix, iy) for ix, row in enumerate(old_matrix) for iy, i in enumerate(row) if i == -1]
        xy2 = [(ix, iy) for ix, row in enumerate(new_matrix) for iy, i in enumerate(row) if i == -1]
        return xy1[0][0] == xy2[0][0]

    def hashable_state(self):
        return hash(self.positions)

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
                end = ''
            s += number + " " + end

        return s

    def print_state(self):
        print("ACTION was " + self.action)
        print(self.state_string())

def npuzzle_goal_state(state):
    """
    Return True if we have reached a goal state.

    :param state: a nPuzzle state
    :return: True (if goal) or False (if not)
    """
    size = state.size ** 2
    l = list(range(1, size))
    l.append(-1)
    return state.positions == l



"""
nPuzzle Directions
"""
class Direction():
    """
    A direction of movement.
    """

    def __init__(self, name, delta):
        """
        Creates a new direction.
        @param name: The direction's name.
        @param delta: The coordinate modification needed for moving in the specified direction.
        """
        self.name = name
        self.delta = delta

    def __hash__(self):
        """
        The hash method must be implemented for actions to be inserted into sets
        and dictionaries.
        @return: The hash value of the action.
        """
        return hash(self.name)

    def __str__(self):
        """
        @return: The string representation of this object when *str* is called.
        """
        return str(self.name)

    def __repr__(self):
        return self.__str__()

    def move(self, location):
        """
        @return: Moving from the given location in this direction will result in the returned location.
        """
        return location + self.delta

    def move_and_swap(self, pos, eb_pos):
        pos[eb_pos], pos[eb_pos + self.delta] = pos[eb_pos + self.delta], pos[eb_pos]
        return pos


test = nPuzzleState("START", 0, None, 3, [1,2,3,4,5,6,7,8,-1])
print(npuzzle_goal_state(test))
test.print_state()
for t in test.successors():
    t.print_state()
