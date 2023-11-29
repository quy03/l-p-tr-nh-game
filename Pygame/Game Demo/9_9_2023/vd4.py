import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Cần cài đặt thư viện Pillow (PIL)

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
    if file_path:
        display_image(file_path)

def display_image(file_path):
    img = Image.open(file_path)
    img.thumbnail((300, 300))  # Thay đổi kích thước ảnh
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img  # Bắt buộc giữ tham chiếu đến ảnh để tránh bị thu gom

root = tk.Tk()

# Tạo nút để duyệt tập tin hình ảnh
browse_button = tk.Button(root, text="Chọn ảnh", command=browse_image)
browse_button.pack()

# Tạo một nhãn để hiển thị ảnh
image_label = tk.Label(root)
image_label.pack()

root.mainloop()
