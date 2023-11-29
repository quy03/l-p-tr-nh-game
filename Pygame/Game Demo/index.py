import tkinter as tk
import pygame
import random

# Hàm để bắt đầu trò chơi
def start_game():
    pygame.init()
    
    # Cài đặt cửa sổ pygame
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Bắn Gà")
    
    # Hình ảnh gà
    chicken = pygame.image.load("chicken.png")
    chicken_rect = chicken.get_rect()
    
    # Vị trí ban đầu của gà
    chicken_rect.x = random.randint(0, 700)
    chicken_rect.y = random.randint(50, 500)
    
    # Bắt đầu vòng lặp trò chơi
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Di chuyển gà
        chicken_rect.x += random.randint(-5, 5)
        chicken_rect.y += random.randint(-5, 5)
        
        # Vẽ mọi thứ lên màn hình
        screen.fill((255, 255, 255))
        screen.blit(chicken, chicken_rect)
        pygame.display.update()
    
    pygame.quit()

# Tạo cửa sổ tkinter
root = tk.Tk()
root.title("Bắn Gà")

# Tạo nút "Bắt đầu"
start_button = tk.Button(root, text="Bắt đầu", command=start_game)
start_button.pack()

# Bắt đầu vòng lặp chạy của ứng dụng tkinter
root.mainloop()
