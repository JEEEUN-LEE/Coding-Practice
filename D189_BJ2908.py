# 백준 2908번: 상수
# https://www.acmicpc.net/problem/2908
# 두 수를 입력받아 뒤집은 후 큰 수를 출력하는 문제

# 오답 풀이 
# a, b = map(int, input().split()) #int형은 슬라이싱 불가함!

# if a[::-1] < b[::-1]:
#     print(b)
# else:
#     print(a)

# 정답 풀이
a, b = input().split()

print(max(a[::-1], b[::-1]))
