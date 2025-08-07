# 프로그래머스: 같은 숫자는 싫어
## 주어진 리스트에서 연속된 같은 숫자를 제거하고, 남은 숫자들로 새로운 리스트를 반환

# 문제 풀이를 위한 틀
## 1. 빈 리스트 생성
## 2. arr 배열 돌면서 이전 숫자와 같지 않으면 리스트에 추가
def solution(arr):
    answer = []
    for i in arr:
        if not answer or answer[-1] != i: # 초기 빈 리스트 제외, 이전 숫자와 같은 경우 제외
            answer.append(i)
    return answer
# 예시 입력
arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))