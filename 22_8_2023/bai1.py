'''print("lap trinh python")
x = int(input("Nhap x:"))
y = int(input("Nhap y:"))

# defaut
def tinhTong(x,y):
    return x+y
print("Tong x + y = ", tinhTong(x,y))
if(x < y):
    print("x nho hon y")
elif(x == y):
    print("x bang y")
else:
    print("x lon hon y")
'''

# Nhap vao so sinh vien trong 1 lop
# nhap thong tin cho tung nhan vien
# in ra danh sach nhan vien

num = int(input("Nhap so sinh vien: "))
SV = []
tenSV = []
maSV = []
# nhap thong tin
for i in range(0,num):
    print ("\nNhap thong tin cho sinh vien thu ",i+1,":")
    ms = input("Nhap ma sinh vien: ")
    # maSV.append(ms)
    ht = input("Nhap ho ten sinh vien: ")
    # tenSV.append(ht)

    SV.append("\nMa Sinh Vien: " +ms+ " | Ho Va Ten: " +ht)
# xuat thong tin
for i in range(0,len(SV)):
    print(SV[i])


# for i in range(0,num):
#     print(tenSV[i] +"|"+ maSV[i] )


    




