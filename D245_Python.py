# 프로그래머스 명예의 전당 (1)
## 상위 k개만큼 명예의 전당 올림, 명예의 전당 스코어 중 최하위 점수 출력 

def solution(k, score):
    answer = [] # 일단 점수를 리스트에 넣고, 정렬해서, 상위 k개 외에는 삭제
    honor = []
    for i in score: 
        honor.append(i)
        honor.sort(reverse = True)
        # k개를 초과하면, 상위 k개 외에 삭제
        if len(honor) > k:
            honor.pop()
        # 명예의 전당 중 최하위 점수 출력
        answer.append(honor[-1])
    return answer
# 예시 입력
k = 3
score = [10, 100, 20, 150, 1, 100, 200]
print(solution(k, score))
