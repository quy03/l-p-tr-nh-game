import pygame
import random
import threading
import tkinter as tk

# Khởi tạo Pygame
pygame.init()

# Các biến cơ bản
chieurong, chieucao = 400, 600

# Tạo cửa sổ Pygame cho màn hình chơi game
manhinh_game = pygame.display.set_mode((chieurong, chieucao))

dongho = pygame.time.Clock()
diemso = 0

# Tạo cửa sổ Tkinter cho thanh menu
root = tk.Tk()
root.geometry("400x100")

# Tạo thanh menu chính
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Tạo menu "Game"
game_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Game", menu=game_menu)

# Thêm các tùy chọn vào menu "Game"
game_menu.add_command(label="New")
game_menu.add_command(label="Save")
game_menu.add_command(label="Quit")

# Tải hình ảnh quả và rổ
hinh_qua = pygame.image.load("OIP.jpg")
hinh_qua = pygame.transform.scale(hinh_qua, (30, 30))
hinh_ro = pygame.image.load("R.jpg")
hinh_ro = pygame.transform.scale(hinh_ro, (100, 60))

# Hình tròn (qua)
qua_rect = hinh_qua.get_rect()
qua_rect.x = random.randint(0, chieurong - qua_rect.width)
qua_rect.y = 0
tocdo_qua = 10

# Hình chữ nhật (rổ)
ro_rect = hinh_ro.get_rect()
ro_rect.x = (chieurong - ro_rect.width) // 2
ro_rect.y = chieucao - ro_rect.height
tocdo_ro = 10

# Tạo font để vẽ điểm số
font = pygame.font.Font(None, 36)

# Tạo hình chữ nhật để điều khiển (rổ)
def ve_ro():
    manhinh_game.blit(hinh_ro, ro_rect)

# Game loop function
def game_loop():
    global diemso
    dangchay = True
    qua_dang_roi = False  # Đánh dấu xem quả đang rơi hay không
    while dangchay:
        for sukien in pygame.event.get():
            if sukien.type == pygame.QUIT:
                dangchay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ro_rect.x -= tocdo_ro
        if keys[pygame.K_RIGHT]:
            ro_rect.x += tocdo_ro

        if not qua_dang_roi:
            # Nếu quả không đang rơi, xác định ngẫu nhiên khi nào bắt đầu rơi
            if random.random() < 0.02:
                qua_dang_roi = True
                qua_rect.x = random.randint(0, chieurong - qua_rect.width)
                qua_rect.y = 0

        if qua_dang_roi:
            # Di chuyển qua xuống
            qua_rect.y += tocdo_qua

            # Kiểm tra va chạm giữa rổ và qua
            if qua_rect.colliderect(ro_rect):
                qua_rect.x = random.randint(0, chieurong - qua_rect.width)
                qua_rect.y = 0
                diemso += 1
                qua_dang_roi = False

            # Nếu qua chạm đáy, kết thúc trò chơi
            if qua_rect.y > chieucao:
                dangchay = False

        # Giới hạn di chuyển của rổ trong màn hình
        ro_rect.x = max(0, min(chieurong - ro_rect.width, ro_rect.x))

        # Xóa màn hình trò chơi
        manhinh_game.fill((255, 255, 255))

        if qua_dang_roi:
            # Vẽ qua nếu đang rơi
            manhinh_game.blit(hinh_qua, qua_rect)

        # Vẽ rổ
        ve_ro()

        # Hiển thị điểm số
        vanban_diemso = font.render("Diem So: " + str(diemso), True, (0, 0, 0))
        manhinh_game.blit(vanban_diemso, (10, 10))

        # Cập nhật cửa sổ Pygame
        pygame.display.update()

        # Giới hạn tốc độ khung hình
        dongho.tick(60)

# Khởi động game loop và Tkinter mainloop trong cùng một luồng
game_thread = threading.Thread(target=game_loop)
game_thread.daemon = True
game_thread.start()

root.mainloop()
