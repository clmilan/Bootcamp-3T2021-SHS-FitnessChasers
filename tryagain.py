# Import the pygame module
import pygame

# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
# from pygame.locals import *
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize pygame
pygame.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Open window with window size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define a player class to contain the player logic
# and avoid dumping it all in the game loop
class Player(pygame.sprite.Sprite):
    # Define position variables
    x = 0
    y = 0

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("player.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
    # Move the sprite based on keypresses
    # This update method is for game logic and controls
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.y -= 1
        if pressed_keys[K_DOWN]:
            self.y += 1
        if pressed_keys[K_LEFT]:
            self.x -= 1
        if pressed_keys[K_RIGHT]:
            self.x += 1

# Create our 'player'
player = Player()

# This is our while loop to keep the game running
running = True
while running:
    # Wait for keyboard events
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    
    # Get the set of keys that were pressed
    pressed_keys = pygame.key.get_pressed()
    
    # Depending on the key pressed, adjust the coordinate
    # Update player
    player.update(pressed_keys)

    # Initialize the screen with a color
    screen.fill((135, 206, 250))

    screen.blit(player.surf, (player.x, player.y))
    
    pygame.display.flip()

    # Ensure we maintain a 30 frames per second rate
    clock.tick(30)
    pass