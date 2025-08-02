# 프로그래머스: 없는 숫자 더하기
## numbers에 한번도 없는 숫자를 찾아, 모두 더한 값 구하기
def solution(numbers):
    # numbers에 있는 숫자를 돌아가면서 0-9 있는지 확이
    # 없으면 answer에 넣어서 누적 더하기 
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer
# 예시 입력
number = [1, 2, 3, 4, 5, 6, 7, 8, 0]
print(solution(number))