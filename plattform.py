import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,'Black')
    score_rect = score_surf.get_rect(center = (400, 30))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 450:
                screen.blit(crab_surf,obstacle_rect)
            else:
                screen.blit(bird_surf,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else: 
        return []
    
def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True
# pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Turtle beach')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

beach_surface = pygame.image.load('graphics/beach.png').convert()

turtle_surf = pygame.image.load('graphics/turtle.png').convert_alpha()
turtle_surf = pygame.transform.scale(turtle_surf, (54,64))
turtle_surf = pygame.transform.rotate(turtle_surf,-90)
turtle_rect = turtle_surf.get_rect(bottomleft = (75,450))
turtle_gravity = 0

#obstacles
bird_surf = pygame.image.load('graphics/bird.png').convert_alpha()
bird_surf = pygame.transform.scale(bird_surf, (64,54))

crab_surf = pygame.image.load('graphics/crab.png').convert_alpha()
crab_surf = pygame.transform.scale(crab_surf, (64,54))


obstacle_rect_list = []

#Intro Screen
game_name = test_font.render('Turtle beach', False, 'Black')
game_name_rect = game_name.get_rect(center = (400, 100))

turtle_stand = pygame.image.load('graphics/turtle.png').convert_alpha()
turtle_stand = pygame.transform.rotozoom(turtle_stand, 0,4)
turtle_stand_rect = turtle_stand.get_rect(center = (400,250))

start_surf = test_font.render('START', False, 'Black')
start_rect = start_surf.get_rect(center = (400, 400))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     print(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and turtle_rect.bottom == 450:
                    turtle_gravity = -15
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(bird_surf.get_rect(bottomright = (randint(900,1100),390)))
            else: 
                obstacle_rect_list.append(crab_surf.get_rect(bottomright = (randint(900,1100),450)))
    if game_active:
        screen.blit(beach_surface,(0,0))
        # pygame.draw.rect(screen,'Green', score_rect)
        # screen.blit(score_surf,(score_rect))
        score = display_score()

        turtle_gravity += 0.5
        turtle_rect.y += turtle_gravity
        if turtle_rect.bottom >= 450: turtle_rect.bottom = 450
        screen.blit(turtle_surf,(turtle_rect))

        #obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collisions
        game_active = collisions(turtle_rect,obstacle_rect_list)

    else:
        screen.fill((94,129,162))
        screen.blit(turtle_stand, turtle_stand_rect)
        screen.blit(game_name, game_name_rect)
        obstacle_rect_list.clear()

        score_message = test_font.render(f'Your score: {score}', False, 'Black')
        score_message_rect = score_message.get_rect(center = (400,400))

        if score == 0:
            screen.blit(start_surf,start_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)