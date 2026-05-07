import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 240))
clock = pygame.time.Clock()
running = True


while running:
    bg = screen.blit(pygame.image.load('mariomap.png').convert_alpha(), (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mario_map = pygame.image.load('mariomap.png').convert_alpha()


    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()