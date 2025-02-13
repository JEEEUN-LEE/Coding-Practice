# 백준 25304번: 영수증
# X원을 지불하고자 한다. 그런데 영수증에는 N개의 물건이 적혀있고, 각 물건은 Ai원에 Bi개 팔고 있다.
# 가격이 맞아 떨어지면 Yes, 아니면 No를 출력하시오.

X = int(input())
N = int(input())

sum = 0 # 초기화
for i in range(N):
    a, b = map(int, input().split())
    sum += (a*b)

if X == sum:
    print("Yes")
else:
    print("No")