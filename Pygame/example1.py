import tkinter as tk

# Tạo một cửa sổ gốc
root = tk.Tk()

# Tạo một nhãn và hiển thị nó trong cửa sổ
# label = tk.Label(root, text="Chào mừng bạn đến với tkinter!")
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label.pack()

# Bắt đầu vòng lặp chạy của ứng dụng
root.mainloop()
