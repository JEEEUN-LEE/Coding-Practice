# 프로그래머스: [PCCE 기출문제] 7번 버스
## 각 정류장마다 승객이 몇 명 타고, 몇 명 내리는지 주어짐, 최종적으로 버스 잔여석 출력 

# 0보다 작으면 0으로 출력
def func1(num):
    if 0 > num:
        return 0
    else:
        return num
def func2(num):
    if num > 0:
        return 0

def func3(station):
    num = 0
    for people in station:
        if people == 'Off':
            num += 1
    return num

def func4(station):
    num = 0 
    for people in station:
        if people == 'On':
            num += 1
    return num

def solution(seat, passengers):
    num_passenger = 0
    for station in passengers:
        num_passenger += func4(station) # 탑승 인원 더하기
        num_passenger -= func3(station) # 하차 인원 빼기
    answer = func1(seat - num_passenger) # 음수면 0으로
    return answer