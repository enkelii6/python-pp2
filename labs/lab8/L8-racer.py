import pygame
from pygame.locals import *
import random

pygame.init()
done = False
screen = pygame.display.set_mode((400, 600))
w = 400
h = 600

FPS = pygame.time.Clock()
FPS.tick(60)

screen.fill((0, 0, 0))  # making screen white
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40, w-40), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):


p1 = Player()
e1 = Enemy()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    pygame.display.update()
