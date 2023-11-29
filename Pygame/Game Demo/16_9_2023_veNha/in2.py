import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Cấu hình cửa sổ
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moving Ball")

# Khởi tạo thông số cho hình ảnh quả bóng
ball_image = pygame.image.load("ball.jpg")  # Load hình ảnh quả bóng
ball_rect = ball_image.get_rect()
ball_rect.center = (size[0] // 2, size[1] // 2)
ball_speed = 5

# Vòng lặp chính
running = True
is_moving = False  # Biến để kiểm tra xem quả bóng có đang di chuyển không
target_x, target_y = ball_rect.center

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Khi nhấn chuột, đặt điểm đích cho quả bóng
            target_x, target_y = pygame.mouse.get_pos()
            is_moving = True

    # Di chuyển quả bóng đến điểm đích
    if is_moving:
        dx = target_x - ball_rect.centerx
        dy = target_y - ball_rect.centery
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance > ball_speed:
            ratio = ball_speed / distance
            ball_rect.centerx += int(dx * ratio)
            ball_rect.centery += int(dy * ratio)
        else:
            ball_rect.center = (target_x, target_y)
            is_moving = False

    # Xóa màn hình
    screen.fill((255, 255, 255))

    # Vẽ hình ảnh quả bóng
    screen.blit(ball_image, ball_rect.topleft)

    # Cập nhật màn hình
    pygame.display.flip()

    # Đặt giới hạn frames per second (FPS)
    pygame.time.Clock().tick(60)

# Kết thúc Pygame
pygame.quit()

# Thoát khỏi chương trình
sys.exit()
