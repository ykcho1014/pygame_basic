import pygame
from pygame import time
from pygame.constants import KEYDOWN

pygame.init()

# Display Setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Display Name
pygame.display.set_caption("Game Name")

# FPS
clock = pygame.time.Clock()

# 1. User Game Initialization (Background Image,Game Image,Coordinate, Speed, Font, and etc.)


running = True
while running:
    dt = clock.tick(30)

    #print("fps : " + str(clock.get_fps()))

    # 2. Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. Game Character Position    
    
    # 4. Collision Handler

    # 5. Display Update

    pygame.display.update()
    
pygame.time.delay(2000)
pygame.quit()