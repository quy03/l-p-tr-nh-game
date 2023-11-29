import pygame
pygame.init()

GRAY = (192, 192, 192)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (500, 500)
screen = pygame.display.set_mode(size)

rect = pygame.Rect(50, 60, 200, 80);#thiet lap toa do hcn
moving = False

running = True;
while running:
    for event in pygame.event.get():#pygame.event.get: ktra hanh dong nguoi dung
        if event.type == pygame.QUIT:#nguoi dung dong cua so thi 
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:#click chuot
            if rect.collidepoint(event.pos):
                moving = True
        elif event.type == pygame.MOUSEBUTTONUP:#tha chuot
            moving = False
        elif event.type == pygame.MOUSEMOTION and moving:
            # rect.move_ip(event.rel)
            
            new_x = rect.x + event.rel[0]
            new_y = rect.y + event.rel[1]

            if 0 <= new_x <= size[0] - rect.width and 0 <= new_y <= size[1] - rect.height:
                rect.topleft = (new_x, new_y)
                
    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect)
    if moving:
        pygame.draw.rect(screen, BLUE, rect, 4)
        
    pygame.display.flip()
    
pygame.quit()