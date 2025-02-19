# 백준 25314번: Long int
# 4로 나눈 몫만큼 long 출력 + int

n = int(input())

for i in range(n//4):
    print("long", end = " ")

print("int")