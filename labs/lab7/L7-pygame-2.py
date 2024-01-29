import pygame

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((960, 600))
done = False
songs = ['music/Playboi Carti - H00DBYAIR (Official Music Video) (256  kbps).mp3',
         'music/BACKR00MS FT TRAVIS SCOTT SEXISDEATH INDIANA420BITCH (256  kbps).mp3',
         'music/PLAYBOI CARTI - UR THE MOON (MUSIC VIDEO) (256  kbps).mp3']
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
i = 0
a = True
background_image = pygame.image.load("music/86c87d3748b1b8ee27db7c60e44ddae6.jpg")
background_rect = background_image.get_rect()

while not done:
    screen.blit(background_image, background_rect)  # Draw background first
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