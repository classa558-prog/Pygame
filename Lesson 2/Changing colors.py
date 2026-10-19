import pygame
pygame.init()
current_color = 0
x = 30
y = 30
screen = pygame.display.set_mode((400, 500))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x -= 1
    if pressed[pygame.K_RIGHT]: x += 1
    if pressed[pygame.K_UP]: y -= 1
    if pressed[pygame.K_DOWN]: y += 1
    x = min(max(0, x), 400 - 60)
    y = min(max(0, y), 500 - 60)
    if x == 0: current_color = (15, 159, 166)
    if y == 0: current_color = (255, 23, 9)
    elif y == 500 - 60: 
        current_color = (0, 0, 255)
    elif x == 400 - 60:
        current_color = (0, 255, 0)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, current_color, (x, y, 60, 60))
    pygame.display.flip()
    
    
    
    
