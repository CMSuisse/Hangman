from turtle import back
import pygame

first_line = [(100,400),(300,400)]
second_line = [(200,400),(200,100)]
third_line = [(200,100),(325,100)]
fourth_line = [(200,150),(250,100)]
fifth_line = [(300,100),(300,150)]
sixth_cirlce = [(300,175),25]
seventh_line = [(300,200),(300,300)]
eigth_line = [(300,300),(275,350)]
ninth_line = [(300,300),(325,350)]
tenth_line = [(300,225),(275,275)]
eleventh_line = [(300,225),(325,275)]

def draw_hangman(background: pygame.Surface, errors: int):
    if errors >= 1: pygame.draw.line(background,(0,0,0),first_line[0],first_line[1],2)
    if errors >= 2: pygame.draw.line(background,(0,0,0),second_line[0],second_line[1],2)
    if errors >= 3: pygame.draw.line(background,(0,0,0),third_line[0],third_line[1],2)
    if errors >= 4: pygame.draw.line(background,(0,0,0),fourth_line[0],fourth_line[1],2)
    if errors >= 5: pygame.draw.line(background,(0,0,0),fifth_line[0],fifth_line[1],2)
    if errors >= 6: pygame.draw.circle(background,(0,0,0),sixth_cirlce[0],sixth_cirlce[1],2)
    if errors >= 7: pygame.draw.line(background,(0,0,0),seventh_line[0],seventh_line[1],2)
    if errors >= 8: pygame.draw.line(background,(0,0,0),eigth_line[0],eigth_line[1],2)
    if errors >= 9: pygame.draw.line(background,(0,0,0),ninth_line[0],ninth_line[1],2)
    if errors >= 10: pygame.draw.line(background,(0,0,0),tenth_line[0],tenth_line[1],2)
    if errors >= 11: pygame.draw.line(background,(0,0,0),eleventh_line[0],eleventh_line[1],2)