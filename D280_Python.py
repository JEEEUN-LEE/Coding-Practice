# 프로그래머스: 공배수
## number가 n 배수이면서 m 배수이면 1을 아니라면 0을 출력

def solution(number, n, m):
    if number % n == 0 and number % m ==0:
        return 1
    else:
        return 0

# 예시 입력
number = 60
n = 2
m = 3
print(solution(number, n, m))
