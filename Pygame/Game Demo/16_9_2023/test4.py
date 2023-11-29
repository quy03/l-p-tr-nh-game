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

running = True
clock = pygame.time.Clock()

# Khởi tạo tốc độ ban đầu và khoảng cách di chuyển
speed = [0, 0]
move_distance = 20

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = [-move_distance, 0]  # Di chuyển sang trái khi nút mũi tên trái được nhấn
            elif event.key == pygame.K_RIGHT:
                speed = [move_distance, 0]  # Di chuyển sang phải khi nút mũi tên phải được nhấn
            elif event.key == pygame.K_UP:
                speed = [0, -move_distance]  # Di chuyển lên trên khi nút mũi tên lên được nhấn
            elif event.key == pygame.K_DOWN:
                speed = [0, move_distance]  # Di chuyển xuống dưới khi nút mũi tên xuống được nhấn

    # Cập nhật vị trí dựa trên tốc độ
    rect.move_ip(speed)

    # Kiểm tra va chạm với tường và điều chỉnh vị trí nếu cần
    if rect.left < 0:
        rect.left = 0
    elif rect.right > width:
        rect.right = width
    if rect.top < 0:
        rect.top = 0
    elif rect.bottom > height:
        rect.bottom = height

    screen.fill(background)
    pygame.draw.rect(screen, RED, rect, 1)
    screen.blit(ball, rect.topleft)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
