import pygame
pygame.init()

size = 500, 500
width, height = size
screen = pygame.display.set_mode(size)

background = (255, 250, 240)
RED = (255, 0, 0)

running = True
start = (0, 0)
end = (0, 0)
drawing = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start = event.pos
            end = event.pos
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            end = event.pos
            drawing = False

    screen.fill(background)
    
    if drawing:
        end = pygame.mouse.get_pos()  # Lấy vị trí hiện tại của chuột
        x = min(start[0], end[0])
        y = min(start[1], end[1])
        width = abs(end[0] - start[0])
        height = abs(end[1] - start[1])
    
        pygame.draw.rect(screen, RED, (x, y, width, height), 2)
        
    pygame.display.update()

pygame.quit()