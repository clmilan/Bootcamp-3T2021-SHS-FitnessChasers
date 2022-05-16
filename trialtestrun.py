
import pygame
import os

pygame.display.set_caption("FitnessChasers: Catch the Healthy Food")

class Game:
    def __init__(self):
        self.width = 480
        self.height = 783
        self.win = pygame.display.set_mode(self.width, self.height)
        
    
    def draw(self):
        self.bg = pygame.transform.scale(pygame.image.load(
            os.path.join('fruits', 'mainBG.jpg')), (self.width, self.height))

        self.win.blit(self.bg, (0,0)) 
        BASKET = pygame.transform.scale(pygame.image.load(
            os.path.join('fruits', 'wicker-basket.png')), (66,66))
        
        self.win.blit(BASKET, (200, 670))

        pygame.display.update()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.START:
                     self.draw()

        pygame.quit()

game = Game()
game.run()