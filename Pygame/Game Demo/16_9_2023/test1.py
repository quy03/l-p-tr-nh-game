import pygame
pygame.init();

size = 800,500;
width, height = size;


screen = pygame.display.set_mode(size);
background =(255,250,240);
b1 = (244,164,96);
RED = (255,0,0);
GREEN = (0,255,0);
screen.fill(b1);

ball = pygame.image.load("ball.jpg");
rect = ball.get_rect();
speed = [2,2]
pygame.display.update();

running = True;
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        rect = rect.move(speed);
        if rect.left < 0 or rect.right > width:
            speed[0] = -speed[0];
        elif rect.top < 0 or rect.bottom > height:
            speed[1] = -speed[1];
    screen.fill(background);
    pygame.draw.rect(screen,RED, rect,1);
    screen.blit(ball,rect);
    pygame.display.update();

pygame.quit();