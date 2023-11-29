import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Cài đặt cửa sổ trò chơi
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

# Màu sắc
white = (255, 255, 255)
blue = (0, 0, 255)

# Khởi tạo con chim
bird = pygame.Rect(100, height // 2, 40, 40)
bird_speed = 0
gravity = 0.5

# Khởi tạo ống nước
pipes = []
pipe_gap = 150
pipe_width = 50
pipe_speed = 3
next_pipe_time = 0

clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -10

    bird_speed += gravity
    bird.y += bird_speed

    if bird.y < 0:
        bird.y = 0
    elif bird.y > height:
        bird.y = height

    if pygame.time.get_ticks() > next_pipe_time:
        pipe_height = random.randint(50, height - pipe_gap - 50)
        pipes.append(pygame.Rect(width, 0, pipe_width, pipe_height))
        pipes.append(pygame.Rect(width, pipe_height + pipe_gap, pipe_width, height - pipe_height - pipe_gap))
        next_pipe_time = pygame.time.get_ticks() + 2000

    for pipe in pipes:
        pipe.x -= pipe_speed
        if pipe.colliderect(bird):
            game_over = True
        if pipe.x + pipe.width < 0:
            pipes.remove(pipe)

    screen.fill(white)

    for pipe in pipes:
        pygame.draw.rect(screen, blue, pipe)

    pygame.draw.rect(screen, blue, bird)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
 