# 프로그래머스: n보다 커질 때까지 더하기
## numbers 배열의 원소 더하면서, n 정수보다 커지는 순간 이때까지 더한 원소 합 출력

def solution(numbers, n):
    answer = 0

    for i in numbers:
        answer += i
        if answer > n:
            return answer

    return answer

# 짧은 풀이
def solution(numbers, n):
    for i in range(len(numbers)+1): #원소 수만큼 반복
        if sum(numbers[:i]) > n:
            return sum(numbers[:i])

