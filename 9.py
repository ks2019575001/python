data = [[21,7,43,65], [2,8,72,52]]
search = int(input("찾을 값 :"))
a = len(data)
b = len(data[0])
for i in range(len(data)):
    for j in range(len(data[0])):
        if search == data[i][j]:
            a = i
            b = j
            break;
if a < len(data) and b < len(data[0]):
    print("위치 : %d행 %d열"%(a+1,b+1))
else:
    print("찾지 못함")
