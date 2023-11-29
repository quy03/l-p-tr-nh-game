import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Các biến cơ bản
chieurong, chieucao = 400, 600
manhinh = pygame.display.set_mode((chieurong, chieucao))
dongho = pygame.time.Clock()
diemso = 0

# Tải hình ảnh quả và ro
hinh_qua = pygame.image.load("OIP.jpg")
hinh_qua = pygame.transform.scale(hinh_qua, (30, 30))  # Thay đổi kích thước nếu cần
hinh_ro = pygame.image.load("R.jpg")
hinh_ro = pygame.transform.scale(hinh_ro, (100, 60))  # Thay đổi kích thước nếu cần

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

# Tạo hình chữ nhật để điều khiển (rổ)
def ve_ro():
    manhinh.blit(hinh_ro, ro_rect)

dangchay = True
qua_dang_roi = False  # Đánh dấu xem quả đang rơi hay không
while dangchay:
    for sukien in pygame.event.get():
        if sukien.type == pygame.QUIT:
            dangchay = False

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

    # Di chuyển rổ bằng các phím mũi tên
    phim = pygame.key.get_pressed()
    if phim[pygame.K_LEFT]:
        ro_rect.x -= tocdo_ro
    if phim[pygame.K_RIGHT]:
        ro_rect.x += tocdo_ro

    # Giới hạn di chuyển của rổ trong màn hình
    ro_rect.x = max(0, min(chieurong - ro_rect.width, ro_rect.x))

    # Xóa màn hình
    manhinh.fill((255, 255, 255))

    if qua_dang_roi:
        # Vẽ qua nếu đang rơi
        manhinh.blit(hinh_qua, qua_rect)

    # Vẽ rổ
    ve_ro()

    # Hiển thị điểm số
    font = pygame.font.Font(None, 36)
    vanban_diemso = font.render("Diem So: " + str(diemso), True, (0, 0, 0))
    manhinh.blit(vanban_diemso, (10, 10))

    pygame.display.flip()

    # Giới hạn tốc độ khung hình
    dongho.tick(60)

# Kết thúc game
pygame.quit()

# Hiển thị điểm cuối cùng trên cửa sổ dòng lệnh
print("Điểm cuối cùng của bạn là:", diemso)
