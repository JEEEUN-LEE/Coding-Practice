# 프로그래머스: 평균 구하기
## 배열 arr의 평균값 출력
def solution(arr):
    answer = sum(arr) / len(arr) # 총합을 배열 개수로 나누기
    return answer