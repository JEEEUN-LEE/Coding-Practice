# 프로그래머스: 정수 내림차순으로 배치하기
## 주어진 정수 n의 각 자리수를 내림차순으로 정렬하여 새로운 정수를 반환하는 함수를 작성하세요.
def solution(n):
    return int(''.join(sorted(str(n), reverse = True)))
# 예시
n = 12345
print(solution(n))