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
rect.topleft = (0, 0)

running = True
clock = pygame.time.Clock()

# Khởi tạo tốc độ ban đầu và biến để theo dõi trạng thái dừng/tiếp tục
speed = [0, 0]
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = [-5, 0]  # Di chuyển sang trái khi nút mũi tên trái được nhấn
            elif event.key == pygame.K_RIGHT:
                speed = [5, 0]  # Di chuyển sang phải khi nút mũi tên phải được nhấn
            elif event.key == pygame.K_UP:
                speed = [0, -5]  # Di chuyển lên trên khi nút mũi tên lên được nhấn
            elif event.key == pygame.K_DOWN:
                speed = [0, 5]  # Di chuyển xuống dưới khi nút mũi tên xuống được nhấn
            elif event.key == pygame.K_SPACE:
                speed = [0, 0]
            elif event.key == pygame.K_r:
                rect.topleft = (0, 0)  # Đặt lại vị trí ban đầu khi nhấn R

    # Cập nhật vị trí dựa trên tốc độ nếu không bị dừng
    if not paused:
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
    # delays
    clock.tick(60)

pygame.quit()
