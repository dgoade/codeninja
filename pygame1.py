import pygame
import sys

pygame.init()

SCREEN_WIDTH_IN_PIXELS = 400
SCREEN_HEIGHT_IN_PIXELS = 400
screen = pygame.display.set_mode((SCREEN_HEIGHT_IN_PIXELS, SCREEN_HEIGHT_IN_PIXELS))

player_x = 200
player_y = 200

PLAYER_COLOR = pygame.Color(255, 255, 255)
while True:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            pygame.quit()
            sys.exit()


        if pygame.KEYDOWN == event.type:
            if pygame.K_UP == event.key:
                player_y = player_y - 10
            else:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_w]:
                    PLAYER_COLOR = pygame.Color(100, 100, 100)


    BACKGROUND_COLOR = pygame.Color(255, 0, 0)
    screen.fill(BACKGROUND_COLOR)

    PLAYER_SIZE_IN_PIXELS = 20
    player_rectangle = pygame.Rect(
        player_x,
        player_y,
        PLAYER_SIZE_IN_PIXELS,
        PLAYER_SIZE_IN_PIXELS)
    pygame.draw.rect(screen, PLAYER_COLOR, player_rectangle)

    pygame.display.update()
