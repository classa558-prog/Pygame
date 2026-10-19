import pygame
pygame.init()
screen = pygame.display.set_mode((400, 500))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.draw.circle(screen, (18, 181, 62), (200, 250), 65)
    pygame.draw.circle(screen, (15, 159, 166), (100, 450), 65, 10)
    pygame.display.flip()