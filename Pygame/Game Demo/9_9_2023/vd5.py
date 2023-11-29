import tkinter as tk
from tkinter import filedialog

def new_file():
    pass

def open_file():
    # askopenfilename: Hàm này được sử dụng để mở một hộp thoại lựa chọn tệp
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        pass

def save_file():
    pass

def save_as_file():
    # asksaveasfilename: để mở hộp thoại lựa chọn tệp để lưu một tệp mới hoặc ghi đè lên một tệp hiện có.
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        pass

def close_file():
    pass

root = tk.Tk()

# Tạo thanh menu chính
menu_bar = tk.Menu(root)#một đối tượng menu chính (menu bar)
root.config(menu=menu_bar)#đặt menu chính này cho cửa sổ chính (root) của ứng dụng Tkinter



# Tạo menu "File"
file_menu = tk.Menu(menu_bar, tearoff=0)
#tearoff=0 làm cho menu con không thể "bứt ra" (tách ra) từ cửa sổ chính. Nếu đặt tearoff=1, người dùng có thể kéo menu con ra thành cửa sổ độc lập.
menu_bar.add_cascade(label="File", menu=file_menu)
# .add_cascade: để thêm menu con vào menu chính



# Thêm các tùy chọn vào menu "File"
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As...", command=save_as_file)
file_menu.add_separator()# đường gạch ngang
file_menu.add_command(label="Close", command=close_file)

root.mainloop()
