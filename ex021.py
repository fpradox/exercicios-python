import pygame
pygame.init()

pygame.mixer.music.load('exc021.mp3')  # troque 'musica.mp3' pelo nome real do arquivo
pygame.mixer.music.play()
input('Aperte Enter para encerrar...')
