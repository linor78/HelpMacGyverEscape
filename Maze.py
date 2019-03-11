#! /usr/bin/env python3
# coding: utf-8
class Maze():
    def __init__(self):
        self.board = []

def main():
    maze=Maze()
    maze.board=['XXXXXXXXXXXXXXXXX', 'XXXXX  XXX XXX XX']
    print(maze.board)
if __name__ == '__main__':
    main()
