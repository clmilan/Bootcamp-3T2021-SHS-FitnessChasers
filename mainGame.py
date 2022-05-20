# from sre_parse import HEXDIGITS
import pygame
import os


class Game:

    def __init__(self):
        self.state = 'main_game'
        self.width = 480
        self.height = 713
        self.win = pygame.display.set_mode((self.width, self.height))
        self.init = False
        # self.game = MainGame()

    def run(self):

        running = True
        while running:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    running = False
                if self.state == 'main_game':
                    game = MainGame()
                    game.mainGame()

        pygame.quit()


class Button(Game):
    def __init__(self, pos_x, pos_y, name, image):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.name = name
        self.image = image
        self.display()

    def display(self):
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))


class MainGame(Game):
    def __init__(self):
        super().__init__()

    def mainGame(self):

        # BUTTONS FOR THE GAME / ITEMS

        # BACGROUND FOR THE GAME
        self.bg = pygame.transform.scale(pygame.image.load(
            os.path.join('mainsprites', 'green_background.jpg')), (480, 713))
        self.win.blit(self.bg, (0, 0))

        # WILL UPDATE THE SCREEN
        pygame.display.update()


game = Game()
game.run()
