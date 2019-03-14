#! /usr/bin/env python3
# coding: utf-8
class Hero():
    def __init__(self, map):
        self.map = map
        self.position = list(self.map.start)[0]

class Position():
    def __init__(self,x,y):
        self.position = (x, y)
    def __repr__(self):
        return str(self.position)
    def up(self):
        x, y = self.position
        return Position(x, y-1)
    def down(self):
        x, y = self.position
        return Position(x, y+1)
    def left(self):
        x, y = self.position
        return Position(x-1, y)
    def right(self):
        x, y = self.position
        return Position(x+1, y)
    def __hash__(self):
        return hash(self.position)
    def __eq__(self, pos):
        return self.position == pos.position
class Maze():
    def __init__(self, filename):
        self.filename = filename
        self.floor = set()
        self.start = set()
        self.end = set()
        self.walls = set()
        self.items = set()
        self.load_file()
    def is_floor_tile(self, position):
        return position in self.floor
    def load_file(self):
        with open(self.filename) as file:
            for x, line in enumerate(file):
                for y, c in enumerate(line):
                    if c == "S":
                        self.start.add(Position(x, y))
                        self.floor.add(Position(x, y))
                    elif c == "E":
                        self.end.add(Position(x, y))
                        self.floor.add(Position(x, y))
                    elif c == ".":
                        self.floor.add(Position(x, y))
                    elif c == "X":
                        self.walls.add(Position(x, y))
                    #

def main():
    map = Maze("maps/map-01.txt")
    p = Position(1, 1).right()
    hero = Hero(map)
    print(hero.position)
if __name__ == '__main__':
    main()
