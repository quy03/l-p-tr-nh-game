import tkinter as tk

def add_entry():
    new_entry = entry.get()  # Lấy giá trị từ ô văn bản
    if new_entry:  # Chỉ thêm nếu có dữ liệu nhập vào
        listbox.insert(tk.END, new_entry)
        entry.delete(0, tk.END)  # Xóa nội dung ô văn bản sau khi thêm

def delete_entry():
    selected_index = listbox.curselection()  # Lấy chỉ mục của mục đã chọn
    if selected_index:
        listbox.delete(selected_index)  # Xóa mục đã chọn

# Tạo cửa sổ chính
root = tk.Tk()

# Tạo ô văn bản và nút thêm
entry = tk.Entry(root)
add_button = tk.Button(root, text="Thêm", command=add_entry)

# Tạo danh sách các mục và nút xóa
listbox = tk.Listbox(root)
delete_button = tk.Button(root, text="Xóa", command=delete_entry)

# Đặt các widget vào giao diện
entry.pack()
add_button.pack()
listbox.pack()
delete_button.pack()

# Khởi chạy ứng dụng
root.mainloop()