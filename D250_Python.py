# 프로그래머스: 자릿수 더하기
## N 각 자릿수 합을 더해서 출력

def solution(n):
    n = str(n) #문자열로 변환
    answer = 0
    for i in n:
        answer += int(i) # 각 자릿수 정수로 변환해서 더하기
    return answer

# 예시 입력
print(solution(1234)) # 10
print(solution(9876)) # 30