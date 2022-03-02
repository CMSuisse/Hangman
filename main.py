import pygame
from draw_hangman import draw_hangman
from WordClass import Word

pygame.init()

word = Word(input("Word that the player should guess: ").lower())
Clock = pygame.time.Clock()
display_font = pygame.font.SysFont("Arial", 40)
used_font = pygame.font.SysFont("Arial", 25, True)

size = 600, 600
background_color = 100, 100, 100
screen = pygame.display.set_mode(size)
screen.fill(background_color)
pygame.display.set_caption("The best Hangman ever")

def display_word() -> None:
    i = 0
    for letter in word.getWort():
        rendered_letter = display_font.render(letter,False,(0,0,0))
        screen.blit(rendered_letter,(i*25 + 100, 525))
        i += 1

    i = 0
    for letter in word.getLetterGuess():
        rendered_letter = used_font.render(letter,False,(0,0,0))
        screen.blit(rendered_letter,(500, i*20 + 50))
        i += 1

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            guess = chr(event.key)
            word.testword(guess)

    Clock.tick(60) 
    draw_hangman(screen,word.geterrors())
    display_word()
    pygame.display.flip()

pygame.quit()