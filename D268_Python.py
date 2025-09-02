# 프로그래머스: PCCP 1번 붕대 감기

# 문제 풀이를 위한 틀
## 반복문으로 변수 카운팅해서 조건에 부합할 떄 상태 체크
## attacks 순회하면 계산 전부 마무리 
# 시간 단위로 반복 → time을 1씩 증가시키며 확인
# 조건 체크
# attacks에 해당 시간 공격이 있으면 → 피해량 적용, 연속 성공(bonus) 초기화
# 공격이 없으면 → 회복 (x씩 증가, t초마다 추가 y 회복)
# 체력 보정
# 체력이 최대 체력을 넘으면 max_health로 보정
# 체력이 0 이하로 떨어지면 -1 반환 (사망)
# 모든 공격이 끝날 때까지 진행 후, 최종 체력 반환

def solution(bandage, health, attacks):
    max_health = health  # 최대 체력 기억
    ch = health          # 현재 체력
    time = 0
    bonus = 0
    idx = 0              # 공격 인덱스

    while idx < len(attacks):
        time += 1

        # 공격 시간인 경우
        if attacks[idx][0] == time:
            ch -= attacks[idx][1]
            bonus = 0
            idx += 1
            if ch <= 0:
                return -1
            continue

        # 회복 시간인 경우
        bonus += 1
        if bonus == bandage[0]:   # 연속 성공 보너스
            ch += bandage[1] + bandage[2]
            bonus = 0
        else:                     # 기본 회복
            ch += bandage[1]

        if ch > max_health:       # 최대 체력으로 보정
            ch = max_health

    return ch
# 예시 입력
print(solution([3, 10, 20], 100, [[2, 30], [5, 50], [10, 20]]))
