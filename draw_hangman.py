import pygame

matrix = [[(100,400),(300,400)], #line 1
          [(200,400),(200,100)], #line 2
          [(200,100),(325,100)], #line 3
          [(200,150),(250,100)], #line 4
          [(300,100),(300,150)], #line 5
          [(300,175),25],        #line 6
          [(300,200),(300,300)], #line 7
          [(300,300),(275,350)], #line 8
          [(300,300),(325,350)], #line 9
          [(300,225),(275,275)], #line 10
          [(300,225),(325,275)]] #line 11

def draw_hangman(background: pygame.Surface, errors: int) -> None:
    if errors > 11: errors = 11
    for i in range(errors):
        if i == 5:
            pygame.draw.circle(background, (0, 0, 0), matrix[i][0], matrix[i][1], 2)
            continue
        pygame.draw.line(background, (0, 0, 0), matrix[i][0], matrix[i][1], 2)