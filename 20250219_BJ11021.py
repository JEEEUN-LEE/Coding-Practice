# 백준 11021번L: A+B - 7
# A+B를 출력하는 문제

n = int(input())

for i in range(1, n+1):
    a, b = map(int, input().split())
    print("Case #"+str(i)+':',a+b)