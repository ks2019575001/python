num1 = int(input("정수1 :"))
num2 = int(input("정수2 :"))


def div_qr(num1,num2):
    a = num1//num2
    return a

def div_qr2(num1,num2):
    b = num1%num2
    return b

r = div_qr(num1,num2)
s = div_qr2(num1,num2)
print("몫 :", r, "나머지 :", s)
