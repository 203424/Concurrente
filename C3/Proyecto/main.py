import pygame, sys
from sprites_tropa import Archer, Knight, Lancer, Dragon
pygame.init()

#color
BG = (201,194,190)
W = 600
H = 400
size = (W,H)
fps = 8
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

all_sprite_list = pygame.sprite.Group()
my_group = pygame.sprite.Group()

def invocar_archer():
    archer = Archer("red")
    my_group.add(archer) 
def invocar_knight():
    knight = Knight("red")
    my_group.add(knight) 
def invocar_lancer():
    lancer = Lancer("red")
    my_group.add(lancer) 
def invocar_dragon():
    dragon = Dragon("red")
    my_group.add(dragon) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                invocar_archer()
            if event.key == pygame.K_w:
                invocar_knight()
            if event.key == pygame.K_e:
                invocar_lancer()
            if event.key == pygame.K_r:
                invocar_dragon()
    my_group.update()
    screen.fill(BG)
    my_group.draw(screen)
    pygame.display.update()
    clock.tick(fps)