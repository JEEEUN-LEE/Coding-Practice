# 프로그래머스: [PCCE 기출문제] 3번 / 수 나누기
## 주어진 수를 100으로 나눈 나머지를 모두 더한 값을 출력
number = int(input())

answer = 0

while number > 0:
    answer += number % 100
    number //= 100

print(int(answer))