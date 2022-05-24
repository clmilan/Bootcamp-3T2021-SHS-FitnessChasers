import pygame
import os
import random
import time
pygame.font.init()


WIDTH, HEIGHT = 460, 780
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('LARO NILA MARENG CELYN TYAKA PARENG CARLOS')

# ======== LOAD IMAGES =========

# ALL FOODS
APPLE = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'apple.png')), (80, 80))

BANANA = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'banana.png')), (80, 80))

BURGER = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'burger.png')), (80, 80))

FRIES = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'fries.png')), (80, 80))

PIZZA = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'pizza.png')), (80, 80))

POTATO = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'potato.png')), (80, 80))


TOAST = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'toast.png')), (80, 80))

TOMATO = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'ttomato.png')), (80, 80))

WATER = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'water.png')), (80, 80))


# BACKGROUND

MAIN_MENU_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'main_menu_bg.png')), (80, 80))

MAIN_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'background.jpg')), (WIDTH, HEIGHT))

# PLAYER'S BASKET
BASKET = pygame.transform.scale(pygame.image.load(
    os.path.join('fitness-chasers', 'basket.png')), (160, 130))


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
        'apple': (APPLE),
        'banana': (BANANA),
        'burger': (BURGER),
        'fries': (FRIES),
        'pizza': (PIZZA),
        'potato': (POTATO),
        'toast': (TOAST),
        'tomato': (TOMATO),
        'water': (WATER)

    }

    def __init__(self, x, y, food):
        super().__init__(x, y)
        self.item_img = self.FOOD_MAP[food]
        self.mask = pygame.mask.from_surface(self.item_img)

    def move(self, speed):
        self.y += speed


def main():
    running = True
    FPS = 60
    clock = pygame.time.Clock()

    speed = 5
    level = 0
    lives = 5

    food = []
    lost = False
    food_sets = 5
    enemy_speed = 1
    lost_count = 0
    food_choices = ['apple', 'banana', 'burger', 'fries',
                    'pizza', 'potato', 'toast', 'tomato', 'water']

    main_font = pygame.font.SysFont('comicsans', 25)
    lost_font = pygame.font.SysFont('comicsans', 30)

    player = Player(230, 610)

    def draw_window():
        # SHOW THE MAIN GAME BACKGROUND
        WIN.blit(MAIN_BG, (0, 0))

        # SHOW THE TEXT IN THE SCREEN
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        # SHOW TEXT WHEN LOST
        if lost:
            lost_label = lost_font.render('You LOST!', 1, (255, 0, 0))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        # SHOW THE FOODS FALLING FROM THE TOP OF THE SCREEN
        for foods in food:
            foods.draw(WIN)

        # SHOW THE BASKET ON THE SCREEN (REPRESENTING AS A PLAYER)
        player.draw(WIN)

        # IT WILL UPDATE THE SCREEN
        pygame.display.update()

    while running:
        # clock.tick(FPS)
        draw_window()

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
                time.sleep(2)
                food.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and player.x + player.get_width() < WIDTH:
            player.x += speed
        if keys[pygame.K_LEFT] and player.x - speed > 0:
            player.x -= speed

        for foods in food:
            foods.move(enemy_speed)
            if foods.y + foods.get_height() > HEIGHT:
                lives -= 1
                food.remove(foods)


def main_menu():
    pass


main()
