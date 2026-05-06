import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

pygame.display.set_caption("Mario")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((92, 148, 252))

    pygame.draw.rect(screen, (150, 75, 0), pygame.Rect(0, 550, 1000, 50))
    pygame.draw.rect(screen, (140, 60, 0), pygame.Rect(400, 320, 50, 50))
    pygame.draw.circle(screen, (150, 60, 0), (400, 320, 50, 50), 5)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()