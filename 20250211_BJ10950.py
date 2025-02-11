# 10950: A+B - 3
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
T = int(input())

for i in range(T): # T=5라면 a+b를 5번 반복
    a, b = map(int, input().split())
    print(a+b)