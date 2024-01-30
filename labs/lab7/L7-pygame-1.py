import pygame

pygame.init()
screen = pygame.display.set_mode((651, 488))
done = False
bg_image = pygame.image.load('imgs/Снимок экрана 2024-01-30 091904.png')
bg_rect = bg_image.get_rect()
sec_img = pygame.image.load('imgs/sec.png')
min_img = pygame.image.load('imgs/min.png')

while not done:
    screen.blit(bg_image, bg_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(sec_img, (300, 94))
    screen.blit(min_img, (160, 100))


    pygame.display.flip()

