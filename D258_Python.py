# 프로그래머스: 과일 장수
## 사과 최대 점수 k, 한상자에 들어가는 사과 수 m, 사과 점수 score에서 최대 이익을 낼 수 있는 함수 만들기
## 문제 풀이를 위한 틀
## score을 내림차순 정렬, m개씩 잘라서 상자 만들기, 각 상자에서 마지막 원소(최솟값) * 상자개수 출력
def solution(k, m, score):
    score.sort(reverse = True)
    result = 0 
    for i in range(0, len(score), m):
        box = score[i:i+m]
        if len(box) == m:
            result += min(box) * m
    return result
# 예시 입력
print(solution(5, 3, [1, 2, 3, 4, 5, 6])) # 15