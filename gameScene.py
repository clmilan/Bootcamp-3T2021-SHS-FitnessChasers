import pygame, os
from mainGame import *

class MainGame(Game):
    def __init__(self):
        super().__init__()

    def mainGame(self, events):
        print('Line 46')
        if not self.init:
            self.bg = pygame.image.load(os.path.join('mainsprites', 'green_background.png'))
            self.win.blit(self.bg, (0, 0))
            pygame.display.update()
            self.init = True