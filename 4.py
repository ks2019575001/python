score = int(input("점수 :"))
deg = {10:'A', 9:'A', 8:'B', 7:'C', 6:'D', 5:'F', 4:'F', 3:'F', 2:'F', 1:'F', 0:'F'}
print(score, ':', deg[(score//10)])
