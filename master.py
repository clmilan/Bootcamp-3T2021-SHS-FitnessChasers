import pygame, sys 
from random import *
  
# initializing the constructor 
from pygame.locals import *

#initialize the game
pygame.init() 


# screen resolution 
res = (480,783) 
font = pygame.font.SysFont("League Spartan", 60)
  
# opens up a window 
screen = pygame.display.set_mode(res) 

#bg
background = pygame.image.load('background.png').convert()

#caption and icon
pygame.display.set_caption('FITNESS CHASERS')
icon = pygame.image.load('background.png')
pygame.display.set_icon(icon)


  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 



def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False
  
def main_menu ():
    while True: 
      # screen color and text * to be replaced by game logo
      screen.fill((255,255,255))
      #background image
      screen.blit(background, (0, 0))

      # position of mouse
      mx, my = pygame.mouse.get_pos()

      button_1 = pygame.Rect(140, 500, 200, 50)
      button_2 = pygame.Rect(125, 600, 230, 50)

      if button_1.collidepoint((mx, my)):
         if click:
              game()

      if button_2.collidepoint((mx, my)):
         if click:
             options()

      pygame.draw.rect(screen, (14, 0, 68), button_1)
      draw_text('START', font, (255,255,255), screen, 175, 505)
      pygame.draw.rect(screen, (14, 0, 68), button_2)
      draw_text('OPTIONS', font, (255,255,255), screen, 145, 605)
      
      click = False 

      for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit()
              
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
            #if the mouse is clicked on the 
            # button the game is terminated 
            if ev.button == 1: 
                click = True
        
      
      # updates the frames of the game 
      pygame.display.update() 
      # fills the screen with a color 

def game():
    running = True
    while running: 
        screen.fill((0,0,0))
        draw_text('game', font, (255,255,255), screen, 20,20)
        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit()
            
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update() 

def options():
    running = True
    while running: 
        screen.fill((0,0,0))
        draw_text('options', font, (255,255,255), screen, 20,20)
        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit()
            
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update() 

main_menu()
