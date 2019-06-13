data = [21, 7, 43, 65, 2, 8, 72, 52, 9]

for i in range(9):
    a = int(input("찾을 값 :"))
    if a in data:
        print("위치 :", data.index(a))
    else:
        break
print("찾지 못함")
