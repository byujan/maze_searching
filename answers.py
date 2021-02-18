#Continuing Education - State Space Searching
#Answers written by Peter Jang

import numpy as np

class Maze:
    def __init__(self, size, walls):
        self.size = size
        self.walls = walls
        self.maze = self.__createMaze()

    def __createMaze(self):
        maze = np.zeros(self.size)
        for x, y in self.walls:
            maze[x,y] = 8
        return maze

    def put_answer(self, moves):
        for x,y in moves:
            self.maze[x,y] = 5
        

    def __repr__(self):
        return str(self.maze)

class State:
    def __init__(self, parent, pos, move, maze):
        self.parent = parent
        self.pos = pos
        self.maze = maze
        self.move = move

    def isValid(self, move):
        xpos, ypos = self.pos
        xmove, ymove = move
        if xpos + xmove < 0 or ypos + ymove < 0:
            return False
        if xpos == xpos+xmove and ypos == ypos+ymove:
            return False
        if (xpos+xmove, ypos+ymove) in self.maze.walls:
            return False
        if xpos + xmove > self.maze.size[0] or ypos + ymove > self.maze.size[1]:
            return False
        return True

    def get_children(self):
        children = []
        moves = [(0,1), (1,0), (-1,0), (0,-1)]
        for move in moves:
            xpos, ypos = self.pos
            xmove, ymove = move
            newpos = (xpos+xmove, ypos+ymove)
            if self.isValid(move):
                newState = State(self, newpos, move, self.maze)
                children.append(newState)
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
    frontier = [initial_state]
    explored_states = set()
    while frontier:
        state = frontier.pop(0)
        if state.pos not in explored_states:
            explored_states.add(state.pos)
            children = state.get_children()
            for child in children:
                frontier.append(child)
                if child.pos == goal:
                    move_list = child.get_moves()
                    return move_list
    return None

def main():
    size = (5,5)
    walls = [(1,1), (2,1), (2,2), (3,2), (0,3)]
    newMaze = Maze(size, walls)
    print(newMaze.maze)
    init_state = State(None, (0,0), None, newMaze)
    path = BreadthFirstSearch(init_state, (0,4))
    print(path)

if __name__ == "__main__":
    main()