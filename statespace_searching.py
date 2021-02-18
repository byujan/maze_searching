#Continuing Education - State Space Searching
#Exercises written by Peter Jang

import numpy as np

class Maze:
    def __init__(self, size, walls):
        self.size = size
        self.walls = walls
        self.maze = self.__createMaze()

    def __createMaze(self):
        """
        Purpose:
        Using size and walls input from the class instantiation
        return a matrix that represents the maze
        """
        #TODO
        pass

    def __repr__(self):
        return str(self.maze)

class State:
    def __init__(self, parent, pos, move, maze):
        self.parent = parent
        self.pos = pos
        self.maze = maze
        self.move = move

    def isValid(self, move):
        """
        Purpose:
        Given a move (tuple), check to see if that move is valid
        within the constraints of the maze
        """
        #TODO
        pass

    def get_children(self):
        """
        Purpose:
        Given the current state (self), return a list of new states that are possible
        within the constraints of the maze
        Hint - when you generate new states, use your isValid() function to see if it
        is possible
        """
        #TODO
        children = []
        moves = [(0,1), (1,0), (-1,0), (0,-1)]
        return children

    def get_direction(self, move):
        if move == (0,1):
            return 'right'
        elif move == (1,0):
            return 'down'
        elif move == (-1,0):
            return 'up'
        elif move == (0,-1):
            return 'left'
        else:
            return 'n/a'

    def get_moves(self):
        move_list = []
        state = self
        while state.parent:
            move_list.append(self.get_direction(state.move))
            state = state.parent
        move_list.reverse()
        return move_list

    def __repr__(self):
        return str(self.pos)

    def __hash__(self):
        return hash((self.pos))

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and
                getattr(other, 'pos', None) == self.pos
                )

def BreadthFirstSearch(initial_state, goal):
    """
    Purpose:
    Use your BFS search algorithm to search through the state space of the maze
    initial_state - the first state
    goal (tuple) - position of the goal state i.e. (0,4)
    return - a list of the moves you need to take from the start to the goal
    If there is no way to get to the goal, return an empty list
    """
    #TODO
    return []