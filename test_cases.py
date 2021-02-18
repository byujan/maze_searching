#Continuing Education - State Space Searching
#Tests written by Peter Jang

import unittest
from statespace_searching import Maze, State, BreadthFirstSearch
import numpy as np

class TestMaze(unittest.TestCase):

    def test_create(self):
        size = (5,5)
        walls = [(1,1), (2,1), (2,2), (3,2), (0,3)]
        newMaze = Maze(size, walls)
        a = np.array([[0, 0, 0, 8, 0],[0, 8, 0, 0, 0],[0, 8, 8, 0, 0],[0, 0, 8, 0, 0],[0, 0, 0, 0, 0]])
        self.assertEqual(newMaze.maze.all(), a.all())

    def test_create1(self):
        size = (8,8)
        walls = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
        newMaze = Maze(size, walls)
        a = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 0.0], \
                    [0.0, 0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 8.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 8.0, 0.0, 0.0], \
                    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
        self.assertEqual(newMaze.maze.all(), a.all())

class TestState(unittest.TestCase):

    def test_isValid(self):
        size = (5,5)
        walls = [(1,1), (2,1), (2,2), (3,2), (0,3)]
        newMaze = Maze(size, walls)
        init_state = State(None, (0,1), None, newMaze)
        self.assertEqual(init_state.isValid((1,0)), False)

    def test_isValid1(self):
        size = (5,5)
        walls = [(1,1), (2,1), (2,2), (3,2), (0,3)]
        newMaze = Maze(size, walls)
        init_state = State(None, (0,0), None, newMaze)
        self.assertEqual(init_state.isValid((-1,0)), False)

    def test_isValid2(self):
        size = (5,5)
        walls = [(1,1), (2,1), (2,2), (3,2), (0,3)]
        newMaze = Maze(size, walls)
        init_state = State(None, (0,0), None, newMaze)
        self.assertEqual(init_state.isValid((0,-1)), False)

    def test_isValid3(self):
        size = (5,5)
        walls = [(1,1), (2,1), (2,2), (3,2), (0,3)]
        newMaze = Maze(size, walls)
        init_state = State(None, (0,0), None, newMaze)
        self.assertEqual(init_state.isValid((0, 1)), True)

    def test_children(self):
        size = (5,5)
        walls = [(1,1), (2,1), (2,2), (3,2), (0,3)]
        newMaze = Maze(size, walls)
        init_state = State(None, (0,0), None, newMaze)
        a = init_state.get_children()
        b = []
        for child in a:
            b.append(child.pos)
        self.assertEqual(b, [(0, 1), (1, 0)])

    def test_children1(self):
        size = (5,5)
        walls = [(1,1), (2,1), (2,2), (3,2), (0,3)]
        newMaze = Maze(size, walls)
        init_state = State(None, (1,2), None, newMaze)
        a = init_state.get_children()
        b = []
        for child in a:
            b.append(child.pos)
        self.assertEqual(b, [(1,3), (0,2)])

class TestSearch(unittest.TestCase):
    def test_bfs(self):
        size = (5,5)
        walls = [(1,1), (2,1), (2,2), (3,2), (0,3)]
        newMaze = Maze(size, walls)
        init_state = State(None, (0,0), None, newMaze)
        path = BreadthFirstSearch(init_state, (4,4))
        self.assertEqual(path, ['right', 'right', 'down', 'right', 'right', 'down', 'down', 'down'])

    def test_bfs1(self):
        size = (5,5)
        walls = [(1,1), (2,1), (2,2), (3,2), (0,3)]
        newMaze = Maze(size, walls)
        init_state = State(None, (0,0), None, newMaze)
        path = BreadthFirstSearch(init_state, (0,4))
        self.assertEqual(path, ['right', 'right', 'down', 'right', 'right', 'up'])
    
if __name__ == '__main__':
    unittest.main()