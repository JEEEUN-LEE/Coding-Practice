# 프로그래머스: 나머지가 1이 되는 수 찾기
## n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x 출력
# 문제를 위한 틀
## n-1의 약수 중에서 1을 제외한 가장 작은 수 구하기

def solution(n):
    for x in range(2, n):
        if n % x == 1:
            return x
# 예시 입력
print(solution(10)) # 3
print(solution(12)) # 5