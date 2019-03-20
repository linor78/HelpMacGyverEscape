#! /usr/bin/env python3
# coding: utf-8
import pygame
import random
import pygame_test
import sys
HEIGHT = 750
WIDTH = 750
CASE_SIZE = int(WIDTH / 15)
PATH_CHAR = '.'
HERO_CHAR = 'S'
GUARD_CHAR = 'E'
WALL_CHAR = '#'
ITEMS_CHARS = ('1', '2', '3', '4')
KEY_DOWN_VAlID = (pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT)

class ViewPyGame:
    def __init__(self):
        pygame.init()
        self.size = WIDTH , HEIGHT
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
        ''''''
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
        '''Method that resize every loaded images to 50px * 50px'''
        for key in self.images:
            self.images[key] = pygame.transform.scale(self.images[key],(CASE_SIZE, CASE_SIZE))
    def show_maze(self, map):
        '''Method that put initial map on the window Surface'''
        #self.screen.fill(BLACK)
        for y in range(0,15):
            for x in range(0,15):
                self.screen.blit(self.images[map[y][x]], (x*CASE_SIZE, y*CASE_SIZE))
        pygame.display.flip()
    def wait_event_keydown_within(self,list_of_key):
        '''Method that wait for an event to occur and return the event '''
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in list_of_key :
                        return event.key
    def update_hero_position(self, oldpos, newpos):
        '''Method that only update the 2 zones who changed'''
        ox, oy = oldpos.position
        nx, ny = newpos.position
        self.screen.blit(self.images[PATH_CHAR],( ox * CASE_SIZE, oy * CASE_SIZE))
        pygame.draw.rect(self.screen, (0,0,0),(nx * CASE_SIZE, ny * CASE_SIZE, CASE_SIZE, CASE_SIZE))
        self.screen.blit(self.images[HERO_CHAR],( nx * CASE_SIZE, ny * CASE_SIZE))
        pygame.display.update(((ox * CASE_SIZE, oy * CASE_SIZE, CASE_SIZE, CASE_SIZE),
        (nx * CASE_SIZE, ny * CASE_SIZE, CASE_SIZE, CASE_SIZE)))
    def end_screen(self):
        pygame.quit()


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
        return self._map[y][x]
    def get_position_of(self,char):
        ''' Method that return the indexes fo the first ocurrence of the
        char in the map as a Position'''
        for i, line in enumerate(self._map):
            if char in self._map[i]:
                return Position(self._map[i].index(char), i)
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
        """Method that create a string of the map for consol view"""
        '''s = str()
        for line in self._map:
            s = s + (''.join(line) + '\n')'''

        return self._map.copy()
class ControllerMacGyver:
    def __init__(self, map, hero, view):
        self.map = map
        self.hero = hero
        self.view = view
        self.items_initialize()
        self.view.show_maze(self.map.copy)
    def items_initialize(self):
        '''Fonction that place the 4 items randomly in the map on the floor
        as a char from '1' to '4' '''
        nb_of_items = 4
        while nb_of_items > 0:
            p = Position(random.randint(0, 14), random.randint(0, 14))
            if self.map.get_char(p) == PATH_CHAR:
                self.map.set_char_to_indexes(str(nb_of_items), p)
                nb_of_items -= 1
    def is_valid_case(self, pos):
        char = self.map.get_char(pos)
        if char == PATH_CHAR:
            return 1
        elif char in ITEMS_CHARS:
            self.hero.item_found()
            return 1
        elif char == WALL_CHAR:
            return 0
        elif char == GUARD_CHAR:
            if self.hero.items_count == 4:
                self.victory()
            else :
                self.game_over()

    def check_move(self, newpos):
        if self.is_valid_case(newpos):
            self.view.update_hero_position(self.hero.position, newpos)
            self.map.set_char_to_indexes(PATH_CHAR,self.hero.position)
            self.map.set_char_to_indexes(HERO_CHAR, newpos)
            self.hero.position = newpos
    def victory(self):
        self.view.end_screen()
        print("\n\n\n############################## YOU WON! ##############################\n\n\n")
        exit()
    def game_over(self):
        self.view.end_screen()
        print("\n\n\n############################## GAME OVER! ##############################\n\n\n")
        exit()
    def get_event(self):
        event = self.view.wait_event_keydown_within(KEY_DOWN_VAlID)
        if event == pygame.K_UP:
            self.check_move(self.hero.position.up())
        elif event == pygame.K_DOWN:
            self.check_move(self.hero.position.down())
        elif event == pygame.K_LEFT:
            self.check_move(self.hero.position.left())
        elif event == pygame.K_RIGHT:
            self.check_move(self.hero.position.right())
        self.get_event()
def main():
    map = Maze("maps/map-01.txt")
    hero = Hero(map.get_position_of(HERO_CHAR))
    view = ViewPyGame()
    controller = ControllerMacGyver(map, hero, view)
    controller.get_event()
    '''while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()'''

if __name__ == '__main__':
    main()
