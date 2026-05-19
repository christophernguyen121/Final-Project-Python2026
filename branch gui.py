import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)





        pygame.init()

scroll = 0
p1_speed = 5
p1_gravity = 5
p1_x = 136
p1_y = 193.5

width = 800
height = 240
scroll_area_width = 200

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True


background = pygame.image.load("mariomap.png").convert_alpha()

offset_x = 0

while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        p1_x -= p1_speed
    if keys[pygame.K_RIGHT]:
        p1_x += p1_speed
    if keys[pygame.K_UP]:
        p1_y -= p1_speed
    if keys[pygame.K_DOWN]:
        p1_y += p1_speed




    screen_player_x = p1_x - offset_x

    if screen_player_x > width - scroll_area_width:
        offset_x += p1_speed

    if screen_player_x < scroll_area_width:
        offset_x -= p1_speed


    screen.blit(background, (-offset_x, 0))







    
    pygame.draw.circle(
        screen,
        (150, 60, 0),
        (p1_x - offset_x, p1_y),
        8
    )

    pygame.display.flip()
    clock.tick(60)







pygame.quit()