# Tocar um música mp3
# Não é possível fazer isso no QPython

import pygame


pygame.init()
pygame.mixer.load("ex_021.mp3")
pygame.mixer.play()
pygame.event.wait()
