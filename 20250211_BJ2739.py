# 2739: 구구단
# n * 1부터 n * 9까지 출력하는 프로그램
n = int(input())

for i in range(1, 10):
    print(n,"*",i, "=", n*i)