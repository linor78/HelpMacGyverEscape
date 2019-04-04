#! /usr/bin/env python3
# coding: utf-8
import pygame
import random
import sys
import view as v
import Maze as m

PATH_CHAR = '.'
HERO_CHAR = 'S'
GUARD_CHAR = 'E'
WALL_CHAR = '#'
ITEMS_CHARS = ('1', '2', '3')
KEY_DOWN_VAlID = (pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT)

class ControllerMacGyver:
    '''Class who will contain the rules of the game
    and who will interact with the other classes'''
    def __init__(self, map, hero, view):
        self.map = map
        self.hero = hero
        self.view = view
        self.items_initialize()
        self.view.show_maze(self.map.copy)
    def items_initialize(self):
        '''Fonction that place the 3 items randomly in the map on the floor
        as a char from '1' to '3' '''
        nb_of_items = 3
        while nb_of_items > 0:
            p = m.Position(random.randint(0, 14), random.randint(0, 14))
            if self.map.get_char(p) == PATH_CHAR:
                self.map.set_char_to_indexes(str(nb_of_items), p)
                nb_of_items -= 1
    def is_within(self, pos):
        '''Method who check if the next position is within the 15 by 15 map'''
        x, y = pos.position
        if ((x >= 0 and x < 15) and (y >= 0 and y < 15)):
            return 1
        else :
            return 0
    def is_valid_case(self, pos):
        '''Method who check if the move is in the map and valid and
         then return the state of the game '''
        if self.is_within(pos) == 0:
            return 0
        char = self.map.get_char(pos)
        if char == PATH_CHAR:
            return 1
        elif char in ITEMS_CHARS:
            self.hero.item_found()
            self.view.add_items_to_inventory(char, self.hero.items_count)
            '''If the 3 items are found by the hero, we remove the 3 items
            and put the crafted one instead'''
            if self.hero.items_count == 3 :
                self.view.show_inventory()
                self.view.add_items_to_inventory('crafted',2)
            return 1
        elif char == WALL_CHAR:
            return 0
        elif char == GUARD_CHAR:
            if self.hero.items_count == 3:
                return 3
            else :
                return 4
    def check_move(self, newpos):
        '''Method who update the map and screen if the move is valid'''
        state = self.is_valid_case(newpos)
        if state:
            self.view.update_hero_position(self.hero.position, newpos)
            self.map.set_char_to_indexes(PATH_CHAR,self.hero.position)
            self.map.set_char_to_indexes(HERO_CHAR, newpos)
            self.hero.move(newpos)
        return state
    def get_event(self):
        '''Event loop who will wait for an event and move accordingly until
         either victory or gameover'''
        state = 0
        '''state being at 3 mean victory and it being at 4 mean gameover
        , any other state let the game continue'''
        while state not in (3, 4):
            event = self.view.wait_event_keydown_within(KEY_DOWN_VAlID)
            if event == "QUIT":
                self.view.end_pygame()
                exit()
            elif event == pygame.K_UP:
                state = self.check_move(self.hero.position.up())
            elif event == pygame.K_DOWN:
                state = self.check_move(self.hero.position.down())
            elif event == pygame.K_LEFT:
                state = self.check_move(self.hero.position.left())
            elif event == pygame.K_RIGHT:
                state = self.check_move(self.hero.position.right())
        if state == 3 :
            self.view.victory()
        else :
            self.view.gameover()
        self.view.end_screen_event()
def main():
    '''Replay loop of the game, it will restart the game until n is pressed
    on the end screen'''
    while 1:
        '''Initialising the four main objects of the program'''
        map = m.Maze("data/maps/map-01.txt")
        hero = m.Hero(map.get_position_of(HERO_CHAR))
        view = v.ViewPyGame()
        controller = ControllerMacGyver(map, hero, view)
        '''launching the game loop'''
        controller.get_event()
        '''Before restarting, we del every objects'''
        del map,hero,view,controller

if __name__ == '__main__':
    main()
