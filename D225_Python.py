# 프로그래머스: 유연근무제
## 일주일 동안 지각 안한 직원 수 구하기
## 출근희망 시각 + 10분까지 오케이, 주말 영향 X
## 모든 시각은 시에 100을 곱하고 분을 더한 정수로 표현됩니다. 예를 들어 10시 13분은 1013이 되고 9시 58분은 958이 됩니다.

# 1. 시간을 분 단위로 변환하는 함수
def to_minutes(time):
    h = time // 100     # 시(hour)만 추출
    m = time % 100      # 분(minute)만 추출
    return h * 60 + m   # 시*60 + 분 = 총 분

# 일주일간 지각 안한 직원 수 구하기
def solution(schedules, timelogs, startday):
    answer = 0  # 조건을 만족한 직원 수

    # 각 직원에 대해 검사
    for i in range(len(schedules)):
        s = startday  # 현재 요일 인덱스
        schedule = to_minutes(schedules[i])  # 직원의 출근 희망 시각

        # 일주일 동안의 출근 기록 확인
        for time in timelogs[i]:
            weekday = s % 7  # 요일을 0~6 범위로 순환시킴

            # 주말(토요일: 6, 일요일: 0)은 이벤트 대상 아님 → 건너뜀
            if weekday in [0, 6]:
                s += 1
                continue

            # 실제 출근 시각을 분 단위로 변환
            t = to_minutes(time)

            # 희망 시각 + 10분보다 늦게 출근했으면 → 실패
            if schedule + 10 < t:
                break  # 더 이상 볼 필요 없이 탈락
            s += 1  # 다음 요일로 이동

        else:
            # for 루프를 정상 종료했으면 (=지각이 없었다면)
            answer += 1

    return answer  # 최종 상품 받을 직원 수 반환
