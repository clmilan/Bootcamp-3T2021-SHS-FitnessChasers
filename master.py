import pygame, sys 
from tkinter import *
from random import *
  
# initializing the constructor 
from pygame.locals import *
pygame.init() 
pygame.display.set_caption('FITNESS CHASERS')

# screen resolution 
res = (480,783) 
font = pygame.font.SysFont("League Spartan", 60)
  
# opens up a window 
screen = pygame.display.set_mode(res) 

# commented codes are for follow-up user interface improvements
# aesthetics 
# white color 
# color = (255,255,255) 
  
# light shade of the button 
# color_light = (170,170,170) 
  
# dark shade of the button 
# color_dark = (100,100,100) 
  
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
      draw_text('FITNESS CHASERS', font, (0,0,0), screen, 50, 150)
      # GameLogo = tkinter.PhotoImage(file ="images/{}" .format( "Fitness Chasers logo.gif"))
      # position of mouse
      mx, my = pygame.mouse.get_pos()

      button_1 = pygame.Rect(140, 300, 200, 50)
      button_2 = pygame.Rect(125, 400, 230, 50)

      if button_1.collidepoint((mx, my)):
         if click:
              game()

      if button_2.collidepoint((mx, my)):
         if click:
             options()

      pygame.draw.rect(screen, (14, 0, 68), button_1)
      draw_text('START', font, (255,255,255), screen, 175, 305)
      pygame.draw.rect(screen, (14, 0, 68), button_2)
      draw_text('OPTIONS', font, (255,255,255), screen, 145, 405)
      
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
        
        # screen.fill((60,25,60)) 
      # stores the (x,y) coordinates into 
      # the variable as a tuple 
     #  mouse = pygame.mouse.get_pos() 
      
      # if mouse is hovered on a button it 
      # changes to lighter shade 
     # if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
      #  pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
          
      #else: 
       # pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 
      
       # superimposing the text onto our button 
      # screen.blit(text , (width/2+50,height/2)) 
      
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

