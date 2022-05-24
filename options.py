import pygame, sys 
from tkinter import *
import os
from master import * 
#for the music
from pygame import mixer

#initialize the game
pygame.init() 
# screen resolution 
res = (480,783) 
screen = pygame.display.set_mode(res) 
pygame.display.set_caption('FITNESS CHASERS')
#option_background = pygame.image.load('option_bg.png').convert()

#pygame.display.set_icon(option_background)
#height = screen.get_height()
#width = screen.get_width()

#background music
pygame.mixer.init()
mixer.music.load('default_music.mp3')
mixer.music.play(-1)

#def option():
    #running = True
    #while running:
        #screen.fill((255,255,255))
        #background image
        #screen.blit(option_background, (0, 0))
       # pygame.display.update() 
