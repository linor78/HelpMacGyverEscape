#! /usr/bin/env python3
# coding: utf-8
import pygame
import random
import pygame_test
PATH_CHAR = '.'
HERO_CHAR = 'S'
GUARD_CHAR = 'E'
WALL_CHAR = '#'

class ViewPyGame:
    def __init__(self):
        pygame.init()
        self.size = 750 , 750
        self.screen = pygame.display.set_mode(self.size)
        self.images = {
        PATH_CHAR : 'data/ressources/floor-tiles-20x20.png',
        HERO_CHAR: 'data/ressources/MacGyver.png',
        GUARD_CHAR: 'data/ressources/Gardien.png',
        WALL_CHAR: 'data/ressources/structures.png',
        '1': 'data/ressources/ether.png',
        '2': 'data/ressources/aiguille.png',
        '3': 'data/ressources/seringue.png',
        '4': 'data/ressources/tube_plastique.png'}
        self.load_images()
    def load_images(self):
        for key in self.images:
            self.images[key] =pygame.image.load(self.images[key])
            if key == PATH_CHAR:
                new_img = pygame.Surface((20,20))
                new_img.blit(self.images[key],(0, 0),(0, 0,20, 20))
                self.images[key] = new_img
            elif key == WALL_CHAR:
                new_img = pygame.Surface((20,20))
                new_img.blit(self.images[key],(0, 0),(20, 40,20, 20))
                self.images[key] = new_img
        self.resize_images()
    def resize_images(self):
        for key in self.images:
            self.images[key] = pygame.transform.scale(self.images[key],(50, 50))
    def show_maze(self, map):
        #self.screen.fill(BLACK)
        for y in range(0,15):
            for x in range(0,15):
                self.screen.blit(self.images[map[x][y]], (y*50, x*50))

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
    @property
    def copy(self):
        """Method that create a string of the map for consol view"""
        '''s = str()
        for line in self._map:
            s = s + (''.join(line) + '\n')'''

        return self._map.copy()
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
    #controller = ControllerMacGyver(map, hero)
    #print(map.get_position_of(']'))
    view = ViewPyGame()
    view.show_maze(map.copy)
    pygame.display.flip()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

if __name__ == '__main__':
    main()
