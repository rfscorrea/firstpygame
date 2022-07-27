import pygame
from sys import exit

# creating a window
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('first_game')
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 100))
test_surface.fill('Red ')

while True:
    # create a way for the player close de window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()      # stop the code

    screen.blit(test_surface, (200, 100))

    pygame.display.update()
    clock.tick(60)      # set the ceiling to 60fps
