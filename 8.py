word = input("문자열 :")

while True:
    a = input("문자 :")
    if a == '':
        break
    elif a in word:
        print("문자", a, "가 문자열", word, "에 존재함")
    else:
        print("문자", a, "가 문자열", word, "에 존재하지 않음")
