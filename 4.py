num1 = int(input("정수1 :"))
num2 = int(input("정수2 :"))

a = num1
b = num2

def div_qr():
    global a
    a = num1//num2

def div_qr2():
    global b
    b = num1%num2

div_qr()
div_qr2()
print("몫 :", a, "나머지 :", b)

