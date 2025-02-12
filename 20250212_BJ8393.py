# n이 주어졌을 때 1~n 까지 합을 구하는 프로그램 
n = int(input())

total = 0 
for i in range(1, n+1):
    total +=i
print(total)