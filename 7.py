jn = input("주민등록번호 년월일 :")

import time

now = time.localtime()
year = now.tm_year
age = year - (int(jn[0:2]) + 2000)+1

if age <= 0:
    age = year - (int(jn[0:2]) + 1900)+1

print("나이 :", age)
