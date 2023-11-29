import pygame
pygame.init()

size = 800, 500
width, height = size

screen = pygame.display.set_mode(size)
background = (255, 250, 240)
b1 = (244, 164, 96)
RED = (255, 0, 0)

screen.fill(b1)

ball = pygame.image.load("ball.jpg")
rect = ball.get_rect()
rect.topleft = (width // 2, height // 2)
speed = [5, 0]  # Ban đầu chỉ di chuyển theo chiều ngang

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        speed = [-5, 0]  # Di chuyển sang trái khi nút mũi tên trái được nhấn
    elif keys[pygame.K_RIGHT]:
        speed = [5, 0]  # Di chuyển sang phải khi nút mũi tên phải được nhấn
    elif keys[pygame.K_UP]:
        speed = [0, -5]  # Di chuyển lên trên khi nút mũi tên lên được nhấn
    elif keys[pygame.K_DOWN]:
        speed = [0, 5]  # Di chuyển xuống dưới khi nút mũi tên xuống được nhấn
        
    rect = rect.move(speed)

    # Kiểm tra va chạm với ranh giới màn hình và đảo ngược hướng nếu cần
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(background)
    pygame.draw.rect(screen, RED, rect, 1)
    screen.blit(ball, rect.topleft)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
