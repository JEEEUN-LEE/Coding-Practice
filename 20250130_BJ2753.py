year = int(input())

# 윤년은 연도가 4의 배수이면서, (100의 배수가 아닐 때 또는 400배의 배수)일 때를 의미함. 
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(1)
else:
    print(0)