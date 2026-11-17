while True :
    try :
        so = int(input())
        if so> 0 :
            break
        else :
            print("Số bạn nhập không là số dương, yêu cầu nhập lại!")
    except ValueError :
        print("Đầu vào không hợp lệ, yêu cầu nhập lại!")
def kiem_tra_so_nguyen_to(n) :
    if n<= 1 :
        return False
    for i in range (1,int(n**0.5)+1) :
        if n % i== 0 :
            return False
    return True
if kiem_tra_so_nguyen_to(so) :
    print(f'{so} la so nguyen to ')
else :
    print(f'{so} khong la so nguyen to')