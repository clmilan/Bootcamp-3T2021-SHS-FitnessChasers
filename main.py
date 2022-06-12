# from ossaudiodev import SNDCTL_COPR_RESET
# from asyncio import run_coroutine_threadsafe
from pygame import mixer
import pygame
import os
import random
import time
pygame.font.init()
pygame.init()


logo = pygame.image.load(os.path.join(
    'Start Up ELements', 'Kaon Ta Logo-2.png'))
WIDTH, HEIGHT = 460, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('KAON TA!!')
pygame.display.set_icon(logo)
# ======== LOAD IMAGES =========

# ALL FOODS
COCONUT = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'COCONUT.png')), (55, 55))

LECHE_FLAN = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'LECHE FLAN.png')), (55, 55))

PANCIT = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'PANCIT.png')), (55, 55))

SINIGANG = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'SINIGANG NA BANGUS.png')), (55, 55))

ZAGU = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'ZAGU.png')), (55, 55))

KWEK_KWEK = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'KWEK-KWEK.png')), (55, 55))

CHICHARON = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'CHICHARON.png')), (55, 55))

CHOPSUEY = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'CHOPSUEY.png')), (55, 55))

MANGO = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'MANGO.png')), (55, 55))


# BACKGROUND

MAIN_MENU_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'menu_bg.png')), (WIDTH, HEIGHT))

MAIN_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'bg.png')), (WIDTH, HEIGHT))

MAIN_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'bg.png')), (WIDTH, HEIGHT))

LOGO = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'logo.png')), (350, 300))

# BUTTONS
START = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'start_btn.png')), (190, 90))

QUIT = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'quit_btn.png')), (190, 90))


# GAME OVER SPRITES
BUKO_GO = pygame.transform.scale(pygame.image.load(
    os.path.join('SPRITES GAME OVER', 'BUKO_GO.jpg')), (WIDTH, HEIGHT))

CHICHARON_GO = pygame.transform.scale(pygame.image.load(
    os.path.join('SPRITES GAME OVER', 'CHICHARON_GO.jpg')), (WIDTH, HEIGHT))


CHOPSUEY_GO = pygame.transform.scale(pygame.image.load(
    os.path.join('SPRITES GAME OVER', 'CHOPSUEY_GO.jpg')), (WIDTH, HEIGHT))

KWEK_KWEK_GO = pygame.transform.scale(pygame.image.load(
    os.path.join('SPRITES GAME OVER', 'KWEK KWEK_GO.jpg')), (WIDTH, HEIGHT))

LECHE_FLAN_GO = pygame.transform.scale(pygame.image.load(
    os.path.join('SPRITES GAME OVER', 'LECHE FLAN_GO.jpg')), (WIDTH, HEIGHT))

LUMPIANG_SARIWA_GO = pygame.transform.scale(pygame.image.load(
    os.path.join('SPRITES GAME OVER', 'LUMPIANG SARIWA_GO.jpg')), (WIDTH, HEIGHT))

MANGGA_GO = pygame.transform.scale(pygame.image.load(
    os.path.join('SPRITES GAME OVER', 'MANGGA_GO.jpg')), (WIDTH, HEIGHT))

PANCIT_BIHON_GO = pygame.transform.scale(pygame.image.load(
    os.path.join('SPRITES GAME OVER', 'PANCIT BIHON_GO.jpg')), (WIDTH, HEIGHT))

SINIGANG_GO = pygame.transform.scale(pygame.image.load(
    os.path.join('SPRITES GAME OVER', 'SINIGANG_GO.jpg')), (WIDTH, HEIGHT))

ZAGU_GO = pygame.transform.scale(pygame.image.load(
    os.path.join('SPRITES GAME OVER', 'ZAGU_GO.jpg')), (WIDTH, HEIGHT))

# PLAYER'S BASKET
BASKET = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'BASKET.png')), (100, 80))

# INSTRUCTIONS
INSTRUCTIONS = pygame.transform.scale(pygame.image.load(
    os.path.join('Start Up Elements', 'INSTRUCTIONS_UP.jpg')), (WIDTH, HEIGHT))


class Items:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.item_img = None

    def draw(self, window):

        window.blit(self.item_img, (self.x, self.y))

    def get_width(self):
        return self.item_img.get_width()

    def get_height(self):
        return self.item_img.get_height()


class Player(Items):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.item_img = BASKET
        self.mask = pygame.mask.from_surface(self.item_img)


class Foods(Items):
    FOOD_MAP = {
        'COCONUT': {
            'img': COCONUT,
            'type': 'good'
        },
        'KWEK_KWEK': {
            'img': KWEK_KWEK,
            'type': 'bad'
        },

        'LECHE_FLAN': {
            'img': LECHE_FLAN,
            'type': 'bad'
        },
        'PANCIT': {
            'img': PANCIT,
            'type': 'good'
        },
        'SINIGANG': {
            'img': SINIGANG,
            'type': 'good'
        },
        'ZAGU': {
            'img': ZAGU,
            'type': 'bad'
        },
        'CHICHARON': {
            'img': CHICHARON,
            'type': 'bad'
        },
        'CHOPSUEY': {
            'img': CHOPSUEY,
            'type': 'bad'
        },
        'MANGO': {
            'img': MANGO,
            'type': 'bad'
        },

    }
    # YUNG TATLONG ARGUMENTS, NAKA RANDOM LAHAT

    def __init__(self, x, y, food_choice):
        super().__init__(x, y)
        # Get the image from random food choice.

        #  CHINECHECK NG "FOOD VARIABLE (WHICH IS YUNG RANDOM)" YUNG FOODMAP
        #  NAKADEPENDE SA FOOD VARIABLE KUNG ANO YUNG LALABAS NA PICTURE
        #  FOR EXAMPLE, MANGO YUNG NAKUHA,

        self.item_img = self.FOOD_MAP[food_choice]['img']
        self.mask = pygame.mask.from_surface(self.item_img)
        self.claimed = False

    def move(self, speed):
        self.y += speed


class Food_Game_Over:
    FOOD_MAP = {
        'COCONUT': (BUKO_GO),
        'CHICHARON': (CHICHARON_GO),
        'CHOPSUEY': (CHOPSUEY_GO),
        'KWEK_KWEK': (KWEK_KWEK_GO),
        'LECHE_FLAN': (LECHE_FLAN_GO),
        'LUMPIANG_SARIWA': (LUMPIANG_SARIWA_GO),
        'MANGGA': (MANGGA_GO),
        'PANCIT_BIHON': (PANCIT_BIHON_GO),
        'SINIGANG': (SINIGANG_GO),
        'ZAGU': (ZAGU_GO),

    }

    def __init__(self, food):
        self.item_img = self.FOOD_MAP[food]
        self.mask = pygame.mask.from_surface(self.item_img)
        self.isShowed = False

    def draw(self, win):
        win.blit(self.item_img, (0, 0))


class Button:
    def __init__(self, x, y, img, name):
        self.x = x
        self.y = y
        self.name = name
        self.img = img
        self.rect = self.img.get_rect(center=(self.x, self.y))

    def draw_window(self, win, rect):
        win.blit(self.img, (rect))

    def check_click(self, pos):
        self.pos = pos
        self.clicked = False
        if self.rect.collidepoint(pos):
            self.clicked = True
            return self.clicked


def collide(obj1, obj2):

    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def main():
    main_game_sound = mixer.Sound(os.path.join(
        'music', 'game_music.mp3'))
    main_game_sound.play()
    running = True
    FPS = 60
    clock = pygame.time.Clock()

    speed = 7
    level = 0
    lives = 5
    score = 0

    # set ng array for later purposes
    food = []

    bad_food = []
    good_food = None
    first_drop = False
    lost = False
    food_sets = 2
    enemy_speed = .8

    food_choice = ['COCONUT',
                   'PANCIT', 'SINIGANG', 'CHICHARON', 'MANGO', 'CHOPSUEY']

    bad_food_choice = ["LECHE_FLAN", 'ZAGU', "KWEK_KWEK", "CHICHARON", ]

    main_font = pygame.font.SysFont('comicsans', 25)

    player = Player(230, 640)

    def draw_window():
        game_over_init = False
        # SHOW THE MAIN GAME BACKGROUND
        WIN.blit(MAIN_BG, (0, 0))

        # SHOW THE TEXT IN THE SCREEN
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        score_label = main_font.render(
            f"Score: {round(score, 1)}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        WIN.blit(score_label, (10, 50))

        # SHOW THE FOODS FALLING FROM THE TOP OF THE SCREEN
        for bad_fud in bad_food:
            bad_fud.draw(WIN)

        for foods in food:
            foods.draw(WIN)

        # SHOW THE BASKET ON THE SCREEN (REPRESENTING AS A PLAYER)
        player.draw(WIN)
        # ['COCOCNUT', "KWEK_KWEK", "LECHE_FLAN", 'PANCIT', 'SINIGANG', 'ZAGU']

        # IT WILL UPDATE THE SCREEN
        pygame.display.update()

    while running:
        clock.tick(FPS)
        draw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if lives <= 4:
            lost = True

        # RANDOM POSITIONS AND IMAGE AND NAGKAKALAMAN YUNG ARRAY
        if len(food) == 0:
            level += 1
            enemy_speed += .1
            # WILL LOOP 3 TIMES
            for i in range(4):
                # FOODS(x, y, food_choice)
                if i <= 1:

                    first_food = Foods(random.randrange(50, WIDTH - 50),
                                       random.randrange(-610, -100), random.choice(food_choice))
                    food.append(first_food)

                print('second drop')
                good_food = Foods(random.randrange(50, WIDTH - 50),
                                  random.randrange(-3000, -100), random.choice(food_choice))
                # GIVEN AMOUNT OF TIME
                if time.time() > 50000:
                    # ADDING TO FOOD ARRAY
                    food.append(good_food)

            for i in range(4):
                print('Third Drop')
                if i <= 1:

                    first_bad_food = Foods(random.randrange(50, WIDTH - 50),
                                           random.randrange(-610, -100), random.choice(food_choice))
                    food.append(first_bad_food)

                bad = Foods(random.randrange(50, WIDTH - 50),
                            random.randrange(-3000, -100), random.choice(bad_food_choice))

                if time.time() > 50000:
                    bad_food.append(bad)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and player.x + player.get_width() < WIDTH:
            player.x += speed
        if keys[pygame.K_LEFT] and player.x - speed > 0:
            player.x -= speed

        for foods in food:
            foods.move(enemy_speed)

            # IF COLLIDE (GOOD FOOD) DADAGDAG NG SCORE
            if collide(foods, player):
                # AVOIDING HIGH SCORE
                if foods.claimed == False:
                    catch_sound = mixer.Sound(
                        os.path.join('music', 'catch_sound.wav'))
                    catch_sound.play()
                    score += 10
                    foods.claimed = True

                    food.remove(foods)

            if foods.y + foods.get_height() > HEIGHT:
                lives -= 1
                food.remove(foods)

        for badfoods in bad_food:

            badfoods.move(enemy_speed)
            if collide(badfoods, player):

                lives -= 1

                bad_food.remove(badfoods)

        if lost:
            main_game_sound.stop()
            game_over()

    pygame.quit()


def main_menu():
    has_started = False
    running = True

    main_menu_sound = mixer.Sound(os.path.join(
        'music', 'backgroundmusic_sound.wav'))
    main_menu_sound.play()

    WIN.blit(MAIN_MENU_BG, (0, 0))
    WIN.blit(LOGO, (50, 100))

    START_BTN = Button(230, 450, START, 'start')
    QUIT_BTN = Button(230, 600, QUIT, 'quit')

    buttons = [START_BTN, QUIT_BTN]
    for items in buttons:
        items.draw_window(WIN, items.rect)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                start = buttons[0].check_click(pos)
                quitted = buttons[1].check_click(pos)
                if start:
                    has_started = True
                if quitted:
                    quit()
            if has_started:
                WIN.blit(INSTRUCTIONS, (0, 0))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        main_menu_sound.stop()
                        main()

        pygame.display.update()

    pygame.quit()


def game_over():
    gameover_sound = mixer.Sound(
        os.path.join('music', 'gameover_sound.wav'))
    gameover_sound.play()
    running = True
    lost = False
    game_over_img = []
    food_choices = ['COCONUT', 'KWEK_KWEK', 'CHICHARON', 'LUMPIANG_SARIWA',
                    'LECHE_FLAN', 'PANCIT_BIHON', 'SINIGANG', 'ZAGU']
    game_over_init = False

    while running:
        # WIN.blit(MAIN_MENU_BG, (0, 0))
        # WIN.blit(LOGO, (50, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            go_img = Food_Game_Over(random.choice(food_choices))
            game_over_img.append(go_img)

            if not game_over_init:

                img_avail = random.choice(game_over_img)
                WIN.blit(img_avail.item_img, (0, 0))

                game_over_init = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    main()
                if event.key == pygame.K_x:
                    quit()

        pygame.display.update()


main_menu()
# game_over()
# import random

# list1 = ['aser', 'james', 'hubero', 'carlos', 'celyn', 'mauie']

# print(random.choice(list1))
