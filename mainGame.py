from sre_parse import HEXDIGITS
import pygame, os
from gameScene import *

class Game:
    
    def __init__(self):
        self.state = 'main_game'
        self.width = 480
        self.height = 713
        self.win = pygame.display.set_mode((self.width, self.height))
        self.init = False
        self.game = Game()

    def run(self):
        
        running = True
        while running:
            
            events = pygame.event.get()
                
            if self.state == 'main_game':
                self.game.mainGame()
            if self.state == 'main_menu':
                self.menu.mainmenu(events)

        pygame.quit()

class Buttons(Game):
    def __init__(self, pos_x, pos_y, name):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.name = name
        self.updateRect()
    
    def display(self):
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
    

    def __init__(self):
        super().__init__()

    def mainGame(self, events):
        print('Line 46')
        if not self.init:
            self.bg = pygame.image.load(os.path.join('mainsprites', 'green_background.png'))
            self.win.blit(self.bg, (0, 0))
            pygame.display.update()
            self.init = True
    

game = Game()
game.run()