import pygame
from sys import exit
from random import randint, choice
import math
import time

class Turtle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        turtle_frame_1 = pygame.image.load('graphics/Turtle/turtle1.png').convert_alpha()
        turtle_frame_1 = pygame.transform.scale(turtle_frame_1,(70,60))
        turtle_frame_2 = pygame.image.load('graphics/Turtle/turtle2.png').convert_alpha()
        turtle_frame_2 = pygame.transform.scale(turtle_frame_2,(70,60))
        self.frames = [turtle_frame_1,turtle_frame_2]
        self.turtle_frame_index = 0
        x_pos = choice([200,400,600])

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect =  self.image.get_rect(midbottom = (x_pos,600))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    def update(self):
        self.animation_state()
        self.rect.y -= 1
        self.delete()
    def delete(self):
        global score
        if self.rect.y <= -50:
            score += 1
            self.kill()

class Enemy_right(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'bird':
                bird_frame_1 = pygame.image.load('graphics/Bird/bird1.png').convert_alpha()
                bird_frame_2 = pygame.image.load('graphics/Bird/bird2.png').convert_alpha()
                self.frames = [bird_frame_1,bird_frame_2]
                y_pos = randint(100,300)
        else: 
            crab_frame_1 = pygame.image.load('graphics/Crab/crab1.png').convert_alpha()
            crab_frame_1 = pygame.transform.scale(crab_frame_1,(60,40))
            crab_frame_2 = pygame.image.load('graphics/Crab/crab2.png').convert_alpha()
            crab_frame_2 = pygame.transform.scale(crab_frame_2,(60,40))
            self.frames = [crab_frame_1,crab_frame_2]
            y_pos = randint(300,500)


        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(bottomleft = (800, y_pos))

    
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    def update(self):
        self.animation_state()
        self.rect.x -= 1.5
        self.delete()
    def delete(self):
        if self.rect.x <= -100:
            self.kill()

class Enemy_left(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'bird':
            bird_frame_1 = pygame.image.load('graphics/Bird/bird1.png').convert_alpha()
            bird_frame_1 = pygame.transform.flip(bird_frame_1, True, False)
            bird_frame_2 = pygame.image.load('graphics/Bird/bird2.png').convert_alpha()
            bird_frame_2 = pygame.transform.flip(bird_frame_2, True, False)
            self.frames = [bird_frame_1,bird_frame_2]
            y_pos = randint(100,300)
        else:
            crab_frame_1 = pygame.image.load('graphics/Crab/crab1.png').convert_alpha()
            crab_frame_1 = pygame.transform.scale(crab_frame_1,(60,40))
            crab_frame_2 = pygame.image.load('graphics/Crab/crab2.png').convert_alpha()
            crab_frame_2 = pygame.transform.scale(crab_frame_2,(60,40))
            self.frames = [crab_frame_1,crab_frame_2]
            y_pos = randint(300,500)


        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(bottomright = (0, y_pos))
    
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    def update(self):
        self.animation_state()
        self.rect.x += 1
        self.delete()
    def delete(self):
        if self.rect.x >= 800:
            self.kill()


class Shell(pygame.sprite.Sprite):
    def __init__(self, target_pos):
        super().__init__()
        self.speed = 5
        turtle_frame_1 = pygame.image.load('graphics/shell.png').convert_alpha()
        turtle_frame_1 = pygame.transform.scale(turtle_frame_1,(30,35))
        turtle_frame_2 = pygame.transform.rotate(turtle_frame_1,90)
        turtle_frame_3 = pygame.transform.rotate(turtle_frame_2,90)
        self.frames = [turtle_frame_1,turtle_frame_2, turtle_frame_3]
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect()
        start_pos = (400,550)
        self.rect.center = start_pos
        self.angle = math.atan2(target_pos[1] - start_pos[1], target_pos[0] - start_pos[0])
        self.last_shot = 0
        self.cooldown_time = 1000


    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def move(self):
        self.rect.move_ip(self.speed * math.cos(self.angle), self.speed * math.sin(self.angle))
        if not screen.get_rect().contains(self.rect):
            self.kill()

    def update(self):
        self.animation_state()
        self.move()


def display_score(score):
    score_surf = test_font.render(f'Score: {score}',False,'Black')
    score_rect = score_surf.get_rect(center = (200, 30))
    screen.blit(score_surf,score_rect)
    return score

def display_lives(lives):
    lives_surf = test_font.render(f'Lives: {lives}',False,'Black')
    lives_rect = lives_surf.get_rect(center = (600, 30))
    screen.blit(lives_surf,lives_rect)
    return lives

def collision_sprite():
        global lives
        if pygame.sprite.groupcollide(shell_group,enemy_group,True, True):
            pass
        if pygame.sprite.groupcollide(turtle_group,enemy_group,True, False):
            lives -= 1
            if lives == 0:
                turtle_group.empty()
                enemy_group.empty()
                shell_group.empty()
                return False
            return True
        else:
            return True
    
# pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Turtle beach')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
score = 0
lives = 3

beach_surface = pygame.image.load('graphics/beach.png').convert()

#groups
turtle_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
shell_group = pygame.sprite.Group()

#Intro Screen
game_name = test_font.render('Turtle beach', False, 'Black')
game_name_rect = game_name.get_rect(center = (400, 100))

turtle_stand = pygame.image.load('graphics//Turtle/turtle1.png').convert_alpha()
turtle_stand = pygame.transform.rotozoom(turtle_stand, 0,4)
turtle_stand_rect = turtle_stand.get_rect(center = (400,250))

start_surf = test_font.render('START', False, 'Black')
start_rect = start_surf.get_rect(center = (400, 400))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 3000)

turtle_timer = pygame.USEREVENT + 2
pygame.time.set_timer(turtle_timer, 3000)

last_shot_time = 0
SHOOT_DELAY = 1
one_time = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    current_time = time.monotonic()
                    if current_time - last_shot_time > SHOOT_DELAY:
                    # Skapa en ny missil som åker mot musens position när spelaren vänsterklickar
                        shell_group.add(Shell(pygame.mouse.get_pos()))
                        last_shot_time = current_time
            if event.type == obstacle_timer:
                if score >= 5 and one_time:
                    pygame.time.set_timer(obstacle_timer, 1000)
                    one_time = False
                random = randint(1,2)
                if random == 1:
                    enemy_group.add(Enemy_right(choice(['bird','crab'])))
                else:
                    enemy_group.add(Enemy_left(choice(['bird','crab'])))
            if event.type == turtle_timer:
                turtle_group.add(Turtle())
        else:
            pygame.time.set_timer(obstacle_timer, 3000)
            lives = 3
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    game_active = True
                    score = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                score = 0


            
    if game_active:
        screen.blit(beach_surface,(0,0))
        score = display_score(score)
        lives = display_lives(lives)

        shell_group.draw(screen)
        shell_group.update()

        turtle_group.draw(screen)
        turtle_group.update()

        enemy_group.draw(screen)
        enemy_group.update()

        #collisions
        game_active = collision_sprite()

    else:
        screen.fill((94,129,162))
        screen.blit(turtle_stand, turtle_stand_rect)
        screen.blit(game_name, game_name_rect)

        score_message = test_font.render(f'Your score: {score}', False, 'Black')
        score_message_rect = score_message.get_rect(center = (400,400))

        if score == 0:
            screen.blit(start_surf,start_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)