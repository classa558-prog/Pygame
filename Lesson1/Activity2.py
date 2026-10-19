import pygame
pygame.init()
display_width_height = pygame.display.set_mode((400,500))
done = False
pygame.display.set_caption(("Adding image and adding background."))
background = pygame.transform.scale(pygame.image.load('Nice bg.jfif').convert(), (400, 500))
front = pygame.transform.scale(pygame.image.load('Front_Image.jfif').convert(), (100, 100))
front_rect = front.get_rect(center = (200, 250))
text = pygame.font.Font(None, 36).render("Hello World", True, pygame.Color('black'))
front_rect2 = text.get_rect(center = (200, 450))
def gameloop():
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
        display_width_height.blit(background, (0, 0))
        display_width_height.blit(front, front_rect)
        display_width_height.blit(text, front_rect2)
        pygame.display.flip()
if __name__ == '__main__':
    gameloop()