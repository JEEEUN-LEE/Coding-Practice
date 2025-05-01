# 백준: 3052번: 나머지
# https://www.acmicpc.net/problem/3052
# 문제: 10개의 수를 입력받아, 그 수들을 42로 나눈 나머지를 구하고, 서로 다른 값이 몇 개 있는지 알아내는 프로그램을 작성하시오.

n = []

for i in range(10):
    a = int(input()) #10개 수 입력받기
    b = a % 42 # 42로 나눈 나머지 구하기
    n.append(b) # 나머지 리스트에 추가하기

s = set(n) # set()은 중복된 값을 제거하고, 고유한 값만 남긴다.
print(len(s))
