import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 258))
clock = pygame.time.Clock()
running = True
bg = pygame.image.load('"C:\Users\zcnguyen\Downloads\supermario  1-1 map.png"')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("black")


    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()