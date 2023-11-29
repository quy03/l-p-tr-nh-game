import tkinter as tk

def hello():
    ho_ten = txt.get()
    result_label.config(text=f"Xin chào {ho_ten}")

top = tk.Tk()

lb = tk.Label(
    top,
    text="Ten Dang Nhap",
)
lb.pack()

txt = tk.Entry(top, bd=5)
txt.pack()

bt = tk.Button(
    top,
    text="Click me!",
    command=hello,
)
bt.pack()

result_label = tk.Label(
    top,
    text="",
)
result_label.pack()

top.mainloop()
