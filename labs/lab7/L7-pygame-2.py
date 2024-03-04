import pygame

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((960, 600))
done = False
songs = ['labs/lab7/music/Playboi Carti - H00DBYAIR (Official Music Video) (256  kbps).mp3',
         'labs/lab7/music/BACKR00MS FT TRAVIS SCOTT SEXISDEATH INDIANA420BITCH (256  kbps).mp3',
         'labs/lab7/music/PLAYBOI CARTI - UR THE MOON (MUSIC VIDEO) (256  kbps).mp3',
         'labs/lab7/music/Yung_Lean_x_Bladee_-_Hennessy_and_Sailor_Moon_55724191.mp3']
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
i = 0
a = True
background_image = pygame.image.load("labs/lab7/music/86c87d3748b1b8ee27db7c60e44ddae6.jpg")
background_rect = background_image.get_rect()

while not done:
    if i == 3:
        background_image = pygame.image.load('labs/lab7/music/d4e27433-f6a7-454a-a5c7-66dd5ad2baf9.jpg')
        background_rect = background_image.get_rect()
        screen.blit(background_image, background_rect)
    else:
        background_image = pygame.image.load("labs/lab7/music/86c87d3748b1b8ee27db7c60e44ddae6.jpg")
        background_rect = background_image.get_rect()
        screen.blit(background_image, background_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                i = (i + 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                i = (i - 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_SPACE:
                if a:
                    pygame.mixer.music.stop()
                    a = False
                else:
                    pygame.mixer.music.play()
                    a = True

    pygame.display.flip()