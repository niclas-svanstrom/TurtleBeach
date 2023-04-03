import pygame
from sys import exit
from random import randint, choice

class Turtle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        turtle_frame_1 = pygame.image.load('graphics/Turtle/turtle1.png').convert_alpha()
        turtle_frame_2 = pygame.image.load('graphics/Turtle/turtle2.png').convert_alpha()
        self.frames = [turtle_frame_1,turtle_frame_2]
        self.turtle_frame_index = 0
        x_pos = randint(100,600)

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
        if self.rect.y <= -100:
            score += 1
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'bird':
            bird_frame_1 = pygame.image.load('graphics/Bird/bird1.png').convert_alpha()
            bird_frame_2 = pygame.image.load('graphics/Bird/bird2.png').convert_alpha()
            self.frames = [bird_frame_1,bird_frame_2]
            y_pos = randint(100,300)
        else:
            crab_frame_1 = pygame.image.load('graphics/Crab/crab1.png').convert_alpha()
            crab_frame_2 = pygame.image.load('graphics/Crab/crab2.png').convert_alpha()
            self.frames = [crab_frame_1,crab_frame_2]
            y_pos = randint(300,500)

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), y_pos))
    
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    def update(self):
        self.animation_state()
        self.rect.x -= 1
        self.delete()
    def delete(self):
        if self.rect.x <= -100:
            self.kill()

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
        if pygame.sprite.groupcollide(turtle_group,enemy_group,True, False):
            lives -= 1
            if lives == 0:
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
pygame.time.set_timer(obstacle_timer, 4000)

turtle_timer = pygame.USEREVENT + 2
pygame.time.set_timer(turtle_timer, 3000)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            pass
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    game_active = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
        if game_active:
            if event.type == obstacle_timer:
                enemy_group.add(Enemy(choice(['bird','crab'])))
            if event.type == turtle_timer:
                turtle_group.add(Turtle())

            
    if game_active:
        screen.blit(beach_surface,(0,0))
        score = display_score(score)
        lives = display_lives(lives)


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