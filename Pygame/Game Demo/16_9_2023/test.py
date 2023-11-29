import pygame
pygame.init();

screen = pygame.display.set_mode((600,300));
background =(255,250,240);
RED = (255,0,0);
GREEN = (0,255,0);
BLUE = (0,0,255)
screen.fill(background);
pygame.display.update();

running = True;
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED;
            elif event.key == pygame.K_g:
                background = GREEN;
            elif event.key == pygame.K_b:
                background = BLUE;
        screen.fill(background);
        pygame.display.update();

pygame.quit();

