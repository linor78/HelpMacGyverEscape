#! /usr/bin/env python3
# coding: utf-8
import pygame

HEIGHT = 750
WIDTH = 750
CASE_SIZE = int(WIDTH / 15)
INVENTORY_HEIGHT = int(CASE_SIZE * 1.2)
PATH_CHAR = '.'
HERO_CHAR = 'S'
GUARD_CHAR = 'E'
WALL_CHAR = '#'
ITEMS_CHARS = ('1', '2', '3')

class ViewPyGame:
    '''Class who will handle the creation and filling of the window using Pygame'''
    def __init__(self):
        pygame.init()
        self.size = WIDTH , (HEIGHT + INVENTORY_HEIGHT)
        self.screen = pygame.display.set_mode(self.size)
        '''Dict containing pairs of data/images representing the diferents type of tile in the maze'''
        self.images = {
        PATH_CHAR : 'data/ressources/floor-tiles-20x20.png',
        HERO_CHAR: 'data/ressources/MacGyver.png',
        GUARD_CHAR: 'data/ressources/Gardien.png',
        WALL_CHAR: 'data/ressources/structures.png',
        '1': 'data/ressources/ether.png',
        '2': 'data/ressources/aiguille.png',
        '3': 'data/ressources/tube_plastique.png',
        'inventory': 'data/ressources/inventory.png',
        'crafted': 'data/ressources/seringue.png'}
        self.load_images()
    def load_images(self):
        '''Method who load the images of the dict 'self.images' and then resize them '''
        for key in self.images:
            self.images[key] =pygame.image.load(self.images[key])
            '''Both the PATH_CHAR and WALL_CHAR images are sprites and need the
            use of the AREA argument of blit to choose the right texture'''
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
        '''Method that resize every loaded images to CASE_SIZEpx * CASE_SIZEpx'''
        for key in self.images:
            if key == 'inventory':
                self.images[key] = pygame.transform.scale(self.images[key],(CASE_SIZE * 15, INVENTORY_HEIGHT))
            else :
                self.images[key] = pygame.transform.scale(self.images[key],(CASE_SIZE, CASE_SIZE))
    def show_maze(self, map):
        '''Method that put initial map on the window Surface'''
        for y in range(0,15):
            for x in range(0,15):
                self.screen.blit(self.images[map[y][x]], (x*CASE_SIZE, y*CASE_SIZE))
        self.show_inventory()
        pygame.display.flip()
    def show_inventory(self):
        '''method who put the inventory bar on teh screen, used both a the start of the game and when the 3 items are found'''
        self.screen.blit((self.images['inventory']),(0, 15 * CASE_SIZE,15 * CASE_SIZE, INVENTORY_HEIGHT))
    def add_items_to_inventory(self, char, index_of_item):
        '''Method who add to the inventory the image of the item the hero just picked up'''
        self.screen.blit(self.images[char],((index_of_item * CASE_SIZE) + 100, 15.1 * CASE_SIZE))
        pygame.display.flip()
    def update_hero_position(self, oldpos, newpos):
        '''Method that update the 2 zones of the screen who changed'''
        ox, oy = oldpos.position
        nx, ny = newpos.position
        self.screen.blit(self.images[PATH_CHAR],( ox * CASE_SIZE, oy * CASE_SIZE))
        '''Before puting the Hero image in his new position we need to fill the zone with black'''
        pygame.draw.rect(self.screen, (0,0,0),(nx * CASE_SIZE, ny * CASE_SIZE, CASE_SIZE, CASE_SIZE))
        self.screen.blit(self.images[HERO_CHAR],( nx * CASE_SIZE, ny * CASE_SIZE))
        '''Updating only the two rectangles we changed'''
        pygame.display.update(((ox * CASE_SIZE, oy * CASE_SIZE, CASE_SIZE, CASE_SIZE),
        (nx * CASE_SIZE, ny * CASE_SIZE, CASE_SIZE, CASE_SIZE)))
    def wait_event_keydown_within(self,list_of_key):
        '''Method that wait for an event to occur and then return the event '''
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "QUIT"
                elif event.type == pygame.KEYDOWN:
                    if event.key in list_of_key :
                        return event.key
    def end_screen_event(self):
        '''Method who wait for either 'y' or 'n' key to be pressed and exit the program if 'n' is pressed'''
        event = self.wait_event_keydown_within((pygame.K_y, pygame.K_n))
        if event == pygame.K_y:
            pass
        else:
            self.end_pygame()
            exit()
    def end_pygame(self):
        """Method that shutdown all pygames modules"""
        pygame.quit()
    def victory(self):
        """Method that print the victory message on the window"""
        font = pygame.font.Font(None, CASE_SIZE)
        text = font.render('You Win!', True,(255, 255, 255), (0, 0, 0))
        self.screen.blit(text,(CASE_SIZE * 6, CASE_SIZE * 7))
        self.try_again()
        pygame.display.flip()
    def gameover(self):
        """Method that print the game over message on the window"""
        font = pygame.font.Font(None, CASE_SIZE)
        text = font.render('Game over!', True,(255, 255, 255), (0, 0, 0))
        self.screen.blit(text,(CASE_SIZE * 6, CASE_SIZE * 7))
        self.try_again()
        pygame.display.flip()
    def try_again(self):
        """Method that print the try again message on the window"""
        font = pygame.font.Font(None, CASE_SIZE)
        text = font.render('Press (y) to play again or', True,(255, 255, 255), (0, 0, 0))
        self.screen.blit(text,(CASE_SIZE * 4, CASE_SIZE * 8))
        font = pygame.font.Font(None, CASE_SIZE)
        text = font.render('press (n) to quit', True,(255, 255, 255), (0, 0, 0))
        self.screen.blit(text,(CASE_SIZE * 5, CASE_SIZE * 9))

def main():
    pass
if __name__ == '__main__':
    main()
