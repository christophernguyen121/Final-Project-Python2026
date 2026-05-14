import pygame
scroll = 0
p1_speed = 20
p1_gravity = 5
p1_x = 136
p1_y = 187
x = 20
y = 20
class Player(pygame.sprite.Sprite):




    pygame.init()
screen = pygame.display.set_mode((800, 240))
clock = pygame.time.Clock()
running = True

scroll = 0
scroll = 5

while running:
    image = screen.blit(pygame.image.load('mariomap.png').convert_alpha(), (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen_x = pygame.rect
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        p1_x -= p1_gravity
    if keys[pygame.K_RIGHT]:
        p1_x += p1_gravity
    if keys[pygame.K_UP]:
        p1_y -= p1_gravity
    if keys[pygame.K_DOWN]:
        p1_y += p1_gravity


    p1 = pygame.draw.rect(screen, (150, 75, 0), pygame.Rect(0, 550, 1000, 50))
    pygame.draw.rect(screen, (140, 60, 0), pygame.Rect(400, 320, 50, 50))
    p3 = pygame.draw.circle(screen, (150, 60, 0), (p1_x, p1_y), 8, )
    pygame.display.flip()
    clock.tick(60)

    screen.blit()

    clock.tick(60)

pygame.quit()