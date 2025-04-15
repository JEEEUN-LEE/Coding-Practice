# 백준 2675번
# https://www.acmicpc.net/problem/2675
# 문자열 반복

N = int(input())

for i in range(N):
    a, b = input().split()
    for j in range(len(b)): #b글자수만큼 반복
        print(b[j] * int(a), end = '') #b 각 문자열을 a횟수만큼 곱해줌, 줄바꿈 없이 이어서 출력
    print('') #줄바꿈