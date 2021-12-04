import random
import pygame

pygame.init()

# Display Setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Display Name
pygame.display.set_caption("Quiz")

# FPS
clock = pygame.time.Clock()

# 1. User Game Initialization (Background Image,Game Image,Coordinate, Speed, Font, and etc.)
# Background
background = pygame.image.load("C:/Users/ykcho/Downloads/MyPythonWorkspace/pygame_basic/background.png")

# Character
character = pygame.image.load("C:/Users/ykcho/Downloads/MyPythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width)/2
character_y_pos = screen_height - character_height

# Move Position
to_x = 0
character_speed = 10

# Enemy
ddong = pygame.image.load("C:/Users/ykcho/Downloads/MyPythonWorkspace/pygame_basic/enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10


running = True
while running:
    dt = clock.tick(30)

    #print("fps : " + str(clock.get_fps()))

    # 2. Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. Game Character Position    
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        
    ddong_y_pos += ddong_speed

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)
    
    # 4. Collision Handler
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("Collision!!")
        running = False

    # 5. Display Update
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong,(ddong_x_pos,ddong_y_pos))

    pygame.display.update()
    

pygame.quit()