#! /usr/bin/env python3
# coding: utf-8
import random
PATH_CHAR = '.'
HERO_CHAR = 'S'
GUARD_CHAR = 'E'
WALL_CHAR = '#'

class Hero:
    def __init__(self, position):
        self.position = position
        self.items_count = 0
    def item_found(self):
        self.items_count += 1
    def move(self, position):
        self.position = position

class Position:
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
class Maze:
    def __init__(self, filename):
        self.filename = filename
        self._map = []
        self.load_file()
    def get_char(self, position):
        ''' Method that return the character from
        a certain position in the map'''
        x, y = position.position
        return self._map[x][y]
    def get_position_of(self,char):
        ''' Method that return the indexes fo the first ocurrence of the
        char in the map as a Position'''
        for i, line in enumerate(self._map):
            if char in self._map[i]:
                return Position(self._map[i].index(char), i)
    def set_char_to_indexes(self, char, position):
        '''Method that put the char at the position in the map '''
        x, y = position.position
        self._map[x][y] = char
    def load_file(self):
        ''' Method that transform the file as a two dimensional array of char'''
        with open(self.filename) as file:
            self._map = [[c for c in list(line) if c != '\n'] for line in file]
    def __repr__(self):
        """Method that create a string of the map for consol view"""
        s = str()
        for line in self._map:
            s = s + (''.join(line) + '\n')
        return s
class ControllerMacGyver:
    def __init__(self, map, hero):
        self.map = map
        self.hero = hero
        self.items_initialize()

    def items_initialize(self):
        '''Fonction that place the 4 items randomly in the map on the floor
        as a char from '1' to '4' '''
        nb_of_items = 4
        while nb_of_items > 0:
            p = Position(random.randint(0, 14), random.randint(0, 14))
            if self.map.get_char(p) == PATH_CHAR:
                self.map.set_char_to_indexes(str(nb_of_items), p)
                nb_of_items -= 1

def main():
    map = Maze("maps/map-01.txt")
    hero = Hero(map.get_position_of('S'))
    controller = ControllerMacGyver(map, hero)
    #print(map.get_position_of(']'))
    print(map)

if __name__ == '__main__':
    main()
