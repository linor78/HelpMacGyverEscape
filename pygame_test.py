import sys, pygame
import Maze
BLACK = 0, 0, 0
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
        WALL_CHAR: 'data/ressources/structures.png'}
        self.load_images()
    def load_images(self):
        for key in self.images:
            self.images[key] = pygame.transform.scale((pygame.image.load((self.images[key]))),( 50, 50))
    def show_maze(self, map):
        for y in range(0,15):
            for x in range(0,15):
                self.screen.blit(self.images[map[x][y]],self.screen,(x, y))
def main():
    view = ViewPyGame()
    img = pygame.image.load("data/ressources/structures.png")
    new_img = pygame.Surface((20,20))
    new_img.blit(img,(0, 0),(20, 40,20, 20))
    view.screen.blit(new_img, (0,0))
    pygame.display.flip()
'''while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip() '''
if __name__ == '__main__':
    main()
