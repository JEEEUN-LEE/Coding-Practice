# 백준 11022번: A+B - 8
# A+B를 계산하시오.
T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A} + {B} = {A+B}")