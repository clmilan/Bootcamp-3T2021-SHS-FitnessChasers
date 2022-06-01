# from ossaudiodev import SNDCTL_COPR_RESET
# from asyncio import run_coroutine_threadsafe
from pygame import mixer
import pygame
import os
import random
import time
pygame.font.init()
pygame.init()


WIDTH, HEIGHT = 460, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('LARO NILA MARENG CELYN TYAKA PARENG CARLOS')

# ======== LOAD IMAGES =========

# ALL FOODS
COCONUT = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'COCONUT.png')), (80, 80))

LECHE_FLAN = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'LECHE FLAN.png')), (80, 80))

PANCIT = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'PANCIT.png')), (80, 80))

SINIGANG = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'SINIGANG NA BANGUS.png')), (80, 80))

ZAGU = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'ZAGU.png')), (80, 80))

KWEK_KWEK = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'KWEK-KWEK.png')), (80, 80))


# TOAST = pygame.transform.scale(pygame.image.load(
#     os.path.join('fitness-chasers', 'toast.png')), (80, 80))

# TOMATO = pygame.transform.scale(pygame.image.load(
#     os.path.join('fitness-chasers', 'ttomato.png')), (80, 80))

# WATER = pygame.transform.scale(pygame.image.load(
#     os.path.join('fitness-chasers', 'water.png')), (80, 80))


# BACKGROUND

MAIN_MENU_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'menu_bg.png')), (WIDTH, HEIGHT))

MAIN_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'bg.png')), (WIDTH, HEIGHT))

MAIN_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'bg.png')), (WIDTH, HEIGHT))

LOGO = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'logo.png')), (350, 300))


# PLAYER'S BASKET
BASKET = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'BASKET.png')), (160, 130))


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
        'COCONUT': (COCONUT),
        'KWEK_KWEK': (KWEK_KWEK),
        'LECHE_FLAN': (LECHE_FLAN),
        'PANCIT': (PANCIT),
        'SINIGANG': (SINIGANG),
        'ZAGU': (ZAGU),

    }

    def __init__(self, x, y, food):
        super().__init__(x, y)
        self.item_img, self.type = self.FOOD_MAP[food], self.FOOD_MAP[food]
        self.mask = pygame.mask.from_surface(self.item_img)
        self.claimed = False

    def move(self, speed):
        self.y += speed


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def main():
    mixer.music.load(os.path.join('fitness-chasers', 'game_music.mp3'))
    mixer.music.play(-1)
    running = True
    FPS = 60
    clock = pygame.time.Clock()

    speed = 5
    level = 0
    lives = 5
    score = 0
    multiplier = .1

    food = []
    lost = False
    food_sets = 5
    enemy_speed = 1
    lost_count = 0
    food_choices = ['COCONUT', 'KWEK_KWEK',
                    'LECHE_FLAN', 'PANCIT', 'SINIGANG', 'ZAGU']

    main_font = pygame.font.SysFont('comicsans', 25)
    lost_font = pygame.font.SysFont('comicsans', 30)

    player = Player(230, 610)

    def draw_window():
        # SHOW THE MAIN GAME BACKGROUND
        WIN.blit(MAIN_BG, (0, 0))

        # SHOW THE TEXT IN THE SCREEN
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        score_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        WIN.blit(score_label, (10, 50))

        # SHOW TEXT WHEN LOST
        if lost:
            lost_label = lost_font.render('You LOST!', 1, (255, 0, 0))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        # SHOW THE FOODS FALLING FROM THE TOP OF THE SCREEN
        # for foods in food:
        #     foods.draw(WIN)

        # SHOW THE BASKET ON THE SCREEN (REPRESENTING AS A PLAYER)
        player.draw(WIN)

        # IT WILL UPDATE THE SCREEN
        pygame.display.update()

    while running:
        clock.tick(FPS)
        draw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if lives <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                running = False
            else:
                continue

        if len(food) == 0:
            level += 1
            enemy_speed += 1
            food_sets += 5
            for i in range(food_sets):
                enemy = Foods(random.randrange(50, WIDTH - 50),
                              random.randrange(-2000, -100), random.choice(food_choices))
                # pygame.time.set_timer(enemy, 2)
                food.append(enemy)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and player.x + player.get_width() < WIDTH:
            player.x += speed
        if keys[pygame.K_LEFT] and player.x - speed > 0:
            player.x -= speed

        # for foods in food:
        #     foods.move(enemy_speed)
            # if foods.y + foods.get_height() > HEIGHT:
            #     lives -= 1
            #     food.remove(foods)

        for foods in food:
            foods.move(enemy_speed)

            if collide(foods, player):
                if foods.claimed == False:
                    score += 10
                    foods.claimed = True
                    score *= multiplier
                    multiplier += .2
                    food.remove(foods)

            if foods.y + foods.get_height() > HEIGHT:
                lives -= 1

                food.remove(foods)

    pygame.quit()


class Button:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.rect = self.img.get_rect(center=(self.x, self.y))

    def draw_window(self, win, rect):
        win.blit(self.img, (rect))

    def check_click(self, pos):
        self.pos = pos
        self.clicked = False
        if self.rect.colliderect(pos):
            print(f"{self.name} was clicked")


def main_menu():
    buttons = []
    running = True

    def draw_window():
        # SHOW THE BACKGROUND
        WIN.blit(MAIN_MENU_BG, (0, 0))
        WIN.blit(LOGO, (50, 100))

        START = pygame.transform.scale(pygame.image.load(
            os.path.join('fitness-chasers', 'start_btn.png')), (190, 90))

        QUIT = pygame.transform.scale(pygame.image.load(
            os.path.join('fitness-chasers', 'quit_btn.png')), (190, 90))

        # SHOW BUTTON
        START_BTN = Button(230, 450, START)
        QUIT_BTN = Button(230, 600, QUIT)

        buttons = [START_BTN, QUIT_BTN]
        for items in buttons:
            WIN.blit(items.img, items.rect)

        # SHOW THE TEXT TO THE SCREEN
        pygame.display.update()

    pygame.quit()

    # mixer.music.load(os.path.join('fitness-chasers', 'default_music.mp3'))
    # mixer.music.play(-1)
    running = True

    while running:
        draw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    main()
                    print('Letter G Was Pressed')

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for items in buttons:
                    print(items.name)

    pygame.quit()


main_menu()
