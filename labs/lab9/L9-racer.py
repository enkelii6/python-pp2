# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialzing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
coin2 = 0
# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("labs/lab8/AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# background sound
pygame.mixer.music.load('labs/lab8/background.wav')
pygame.mixer.music.play(-1) # i use -1 to loop the music

# Create a sprite group Enemy
class Enemy(pygame.sprite.Sprite):
    # constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("labs/lab8/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    # move method
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Create a sprite group Player
class Player(pygame.sprite.Sprite):
    # constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("labs/lab8/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    # move method
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Create a sprite group Coin
class Coin(pygame.sprite.Sprite):
    # constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("labs/lab9/free-icon-dollar-coin-9787486.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def reset(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

class BigCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('labs/lab9/free-icon-dollar-coin-9787486-fotor-2024030511740.png')
        self.rect = self.image.get_rect()
    def move(self):
        self.rect.move_ip(0, SPEED)

# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()
B1 = BigCoin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

big_coins = pygame.sprite.Group()
big_coins.add(B1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, C1, B1, E1)
# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    counter = font_small.render(str(coin2), True, BLACK)
    DISPLAYSURF.blit(counter, (380, 10))

    # Check for collision with coins
    collided_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collided_coins:
        coin2 += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
        new_coin.rect.top = 0
        new_coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        if coin2 % 10 == 0:
            SPEED += 1
            new_coin = BigCoin()
            big_coins.add(new_coin)
            all_sprites.add(new_coin)
            new_coin.rect.top = 0
            new_coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    big_coins_collided = pygame.sprite.spritecollide(P1, big_coins, True)
    for big_coin in big_coins_collided:
        coin2 += 5
        big_coin.kill()

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('labs/lab8/crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)