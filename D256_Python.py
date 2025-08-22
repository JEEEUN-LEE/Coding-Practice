# 문제 이해 : 각 스테이지 실패율을 구하고, 그 실패율이 높은 순서대로 스테이지 번호 정렬하여 반환
## 실패율: 스테이지 도달했지만 아직 클리어 못한사람 / 스테이지에 도달한 사람
## 스테이지 도달했지만 아직 클리어 못한사람: stages에 해당 번호가 들어있는 유저 수
## 스테이지 도달한 사람: stages에서 해당 스테이지 이상에 있는 유저 수 

# 문제 풀이를 위한 틀
## N, stages[i] = x 일 때 x == N+1 이면 클리어

def solution(N, stages):
    answer = []
    total_player = len(stages) #전체 유저 수
    result = []
    for i in range(1, N+1):
        if total_player > 0: 
            fail = stages.count(i) #아직 클리어 못한 유저 수
            fail_rate = fail / total_player #실패율
            total_player -= fail #해당 스테이지 클리어한 유저 수 제외
        else:
            fail_rate = 0 #전체 유저가 없으면 실패율 0
        result.append((-fail_rate, i))  
        result.sort()
    
    # 스테이지만 꺼내기
    return [stage for _, stage in result]
# 예시 입력
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3, 4, 2, 1, 5]