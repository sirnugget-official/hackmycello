# setting canvas
import pygame
# https://www.pygame.org/docs/
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("yellow")

    #game renderingg (this is their example in the pygame docs belokw)
    pygame.draw.rect(screen, "blue", (player_pos.x - 50, player_pos.y - 50, 100, 100))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 *dt
    if keys[pygame.K_s]:
        player_pos.y += 300 *dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 *dt
    if keys[pygame.K_d]:
        player_pos.x += 300 *dt

    pygame.display.flip()
    dt= clock.tick(60) / 1000 # this is the fps, maybe a settings menu where it can be adjusted??

pygame.quit()