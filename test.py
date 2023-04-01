import pygame
from sys import exit

# pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Turtle beach')
clock = pygame.time.Clock()

beach_surface = pygame.image.load('graphics/beach.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(beach_surface,(0,0))

    pygame.display.update()
    clock.tick(60)