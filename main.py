import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
isGrounded = False
p1_speed = 5
p1_gravity = 6
p1_x = 25
p1_y = 510
p1_jump = 10
timer = 0
jumping = False

pygame.display.set_caption("Mario")

running = True
while running:
    def jump():
        global p1_jump
        global p1_y
        global p1_gravity
        global timer
        while timer < 45:
            if timer <= 15:
                p1_y -= p1_gravity + p1_jump
                timer += 1
                if p1_jump >= 2:
                    p1_jump -= .005
            elif timer > 15:
                p1_y += p1_gravity + p1_jump
                p1_jump += 1
                timer += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((92, 148, 252))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        p1_x -= p1_speed
    if keys[pygame.K_RIGHT]:
        p1_x += p1_speed
    #if keys[pygame.K_a]:

    p1_y += p1_gravity
    print(timer)



    p1 = pygame.draw.rect(screen, (150, 75, 0), pygame.Rect(0, 550, 1000, 50))
    pygame.draw.rect(screen, (140, 60, 0), pygame.Rect(400, 320, 50, 50))
    p3 = pygame.draw.circle(screen, (150, 60, 0), (p1_x, p1_y), 22,)
    pygame.display.flip()
    clock.tick(60)

    if pygame.Rect.colliderect(p3, p1):
        isGrounded = True

    else:
        isGrounded = False
    if isGrounded:
        p1_y -= p1_gravity + 0.001
    if isGrounded:
        timer = 0
        p1_jump = 10


pygame.quit()