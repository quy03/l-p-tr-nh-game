import pygame
pygame.init()

size = 500, 500
width, height = size
screen = pygame.display.set_mode(size)
background = (255, 250, 240)
b1 = (244, 164, 96)
RED = (255, 0, 0)

running = True  # Biến này sẽ giúp quản lý việc thoát khỏi vòng lặp chính

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Nếu người dùng đóng cửa sổ, dừng vòng lặp

screen.fill(background)  # Đặt màu nền

# Ở đây, bạn có thể vẽ các hình hoặc đối tượng Pygame khác lên cửa sổ

pygame.display.update()  # Cập nhật màn hình

pygame.quit()

