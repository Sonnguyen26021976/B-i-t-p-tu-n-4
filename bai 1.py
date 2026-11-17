n = int(input("Nhap vao so n( duoi 1000) :"))
if n >1000 :
    print("Yeu cau nhap so duoi 1000")
else :
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
print(f'Tong la {sum}')