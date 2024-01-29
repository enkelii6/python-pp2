import pygame

pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
done = False
songs = ['music/Playboi Carti - H00DBYAIR (Official Music Video) (256  kbps).mp3',
        'music/BACKR00MS FT TRAVIS SCOTT SEXISDEATH INDIANA420BITCH (256  kbps).mp3',
        'music/PLAYBOI CARTI - UR THE MOON (MUSIC VIDEO) (256  kbps).mp3']
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
i = 0


while not done:
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

