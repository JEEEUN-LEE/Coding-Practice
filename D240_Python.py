# 프로그래머스: 없는 숫자 더하기_2번째 풀이
## 0-9까지 숫자 중에서 없는 숫자끼리 더하기

def solution(numbers):
    answer = 0
    for i in range(0, 10):
        if i not in numbers:
            answer += i
    return answer