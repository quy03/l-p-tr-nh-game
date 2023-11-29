import tkinter as tk

top = tk.Tk()  # Corrected the line to create the main window
# txt = tk.Entry(
#     top,
#     bd=5,
# )
def hello():
    print("xin chào lập trình game")
    ho_ten = txt.get()
    print("Xin chao",ho_ten)

lb = tk.Label(
    top,
    text="Ten Dang Nhap",
)
lb.pack()
txt = tk.Entry(top,bd=5);
txt.pack()

bt = tk.Button(
    top,
    text = "Click me!",
    command = hello,
)
bt.pack()


top.mainloop()