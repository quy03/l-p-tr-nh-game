# class person:
#     hoTen = "Trinh Bao Quy"
#     tuoi = 20
#     def __init__(seft,hoTen,tuoi):
#         seft.name = hoTen;
#         seft.age = tuoi;

# p1 = person("Nguyen Van A", 30);
# print(p1.name)


'''
# Nhap vao so sinh vien trong 1 lop
# nhap thong tin cho tung nhan vien
# in ra danh sach nhan vien
'''


class SinhVien():
    def __init__(self):
        self.masv = ""
        self.hoTen = ""

    def nhap(self):
        self.masv = input("Nhap ma sinh vien: ")
        self.hoTen = input("Nhap ho va ten: ")

    def xuat(self):
        print("\nMa so sinh vien:", self.masv)
        print("Ho va ten sinh vien:", self.hoTen)


number = int(input("Nhap so sinh vien: "))
sv = []

for i in range(number):
    s = SinhVien()
    s.nhap()
    sv.append(s)

for s in sv:
    s.xuat()
