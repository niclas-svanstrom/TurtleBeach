import pygame
from sys import exit

# pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Turtle beach')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

beach_surface = pygame.image.load('graphics/beach.png').convert()
text_surface = test_font.render('Turtle beach', False, 'Black')

turtle_surface = pygame.image.load('graphics/turtle.png').convert_alpha()
turtle_surface = pygame.transform.scale(turtle_surface, (54,64))
turtle_y_pos = 550

bird_surf = pygame.image.load('graphics/bird.png').convert_alpha()
bird_surf = pygame.transform.scale(bird_surf, (64,54))
bird_rect = bird_surf.get_rect(topleft = (700,150))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(beach_surface,(0,0))
    screen.blit(text_surface,(300,30))
    turtle_y_pos -= 1.5
    if turtle_y_pos < 100: turtle_y_pos = 550
    screen.blit(turtle_surface,(50,turtle_y_pos))
    screen.blit(bird_surf,bird_rect)
    pygame.display.update()
    clock.tick(60)