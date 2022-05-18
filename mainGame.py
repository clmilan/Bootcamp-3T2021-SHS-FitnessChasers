from sre_parse import HEXDIGITS
import pygame, os


class Game:
    
    def __init__(self):
        self.state = 'main_menu'
        self.width = 480
        self.height = 713
        self.win = pygame.display.set_mode((self.width, self.height))
    

    def run(self):
        
        running = True
        while running:
            
            events = pygame.event.get()
                
            if self.state == 'main_game':
                game = MainGame()
                game.mainGame(events)
            if self.state == 'main_menu':
                menu = Menu()
                menu.mainmenu(events)

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
    
class MainGame(Game):
    def __init__(self):
        super().__init__()

    def mainGame(self):
       return 
        

class Menu(Game):
    def __init__(self):
        super().__init__()

    def mainmenu(self, events):
        self.bg = pygame.image.load(os.path.join('mainsprites', 'background.png'))
        self.win.blit(self.bg, (0, 0))


        for event in events:
            if event.type == pygame.KEYDOWN:
                print('Clicked?')
                if event.key == pygame.K_g:
                    print('G CLicked')
                    self.state = 'main_game'
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                    
        pygame.display.update()

game = Game()
game.run()