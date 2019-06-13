abc = input("문자열 : ")
print("개별 문자 출력 :", end="")
for i in range(len(abc)):
    print(abc[i], end="")
print()

print("역순 개별 문자 출력 :", end="")
for i in range(len(abc)-1,-1,-1):
    print(abc[i], end="")


