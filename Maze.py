#! /usr/bin/env python3
# coding: utf-8


class Hero:
    '''Class who contain the position and the item count of the hero'''
    def __init__(self, position):
        self.position = position
        self.items_count = 0
    def item_found(self):
        self.items_count += 1
    def move(self, position):
        self.position = position

class Position:
    '''class who contain a position as a tuple (x, y)'''
    def __init__(self,x,y):
        self.position = (x, y)
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
class Maze:
    '''Class who contain the map of the game as a 2d array'''
    def __init__(self, filename):
        self.filename = filename
        self._map = []
        self.load_file()
    def get_char(self, position):
        ''' Method that return the character from
        a certain position in the map'''
        x, y = position.position
        return self._map[y][x]
    def get_position_of(self,char):
        ''' Method that return the indexes of the first ocurrence of the
        char in the map as a Position'''
        for i, line in enumerate(self._map):
            if char in self._map[i]:
                return Position(self._map[i].index(char), i)
        return None
    def set_char_to_indexes(self, char, position):
        '''Method that put the char at the position in the map '''
        x, y = position.position
        self._map[y][x] = char
    def load_file(self):
        ''' Method that transform the file into a two dimensional array of char'''
        with open(self.filename) as file:
            self._map = [[c for c in list(line) if c != '\n'] for line in file]
    @property
    def copy(self):
        '''Method that return a copy of the maze'''
        return self._map.copy()

def main():

    pass

if __name__ == '__main__':
    main()
