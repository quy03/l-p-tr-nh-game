import tkinter as tk

def new():
    pass

def save():
    pass

def quit():
    pass

root = tk.Tk()

# Tạo thanh menu chính
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Tạo menu "File"
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Thêm các tùy chọn vào menu "File"
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Save", command=save)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit)

root.mainloop()
