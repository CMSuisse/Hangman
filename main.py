import pygame
from draw_hangman import draw_hangman

pygame.init()

word = "test"
letters_guessed = ["_"*len(word)]
errors = 5
Clock = pygame.time.Clock()

size = 600, 600
background_color = 100, 100, 100
screen = pygame.display.set_mode(size)
screen.fill(background_color)

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        
    draw_hangman(screen,errors)
    pygame.display.flip()
    Clock.tick(60)

pygame.quit()