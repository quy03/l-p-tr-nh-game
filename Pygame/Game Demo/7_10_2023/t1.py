import pygame
from pygame.locals import *
RED = (255, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0,255,0)
pygame.init()
w, h = 640, 240
screen = pygame.display.set_mode((w, h)) 
running = True
path = "bird-icon.png"
img0 = pygame.image.load(path)
img0.convert()
rect0 = img0.get_rect()
pygame.draw.rect(img0, GREEN, rect0, 1)
center = w//2, h//2
img = img0
rect = img.get_rect()
rect.center = center
angle = 0
scale = 1
while running:
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False
        if event.type == KEYDOWN:
            if event.key == K_r:
                if event.mod & KMOD_SHIFT: 
                    angle -= 30
                else:
                    angle += 30
                img = pygame.transform.rotozoom(img0, angle, scale)
            elif event.key == K_s:
                if event.mod & KMOD_SHIFT:
                    scale /= 1.1 
                else:
                    scale *= 1.1
                img = pygame.transform.rotozoom(img0, angle, scale)
            elif event.key == K_h:
                img = pygame.transform.flip(img, True, False)
            elif event.key == K_v:
                img = pygame.transform.flip(img, False, True)
            rect = img.get_rect()
            rect.center = center
    screen.fill(GRAY)
    screen.blit(img, rect)
    pygame.draw.rect(screen, RED, rect, 1)
    pygame.display.update()
pygame.quit()