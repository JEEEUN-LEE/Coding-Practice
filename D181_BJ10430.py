# 10430번: 나머지
# https://www.acmicpc.net/problem/10430
# 나머지 연산을 이용한 문제

A, B, C= map(int, input().split())

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)