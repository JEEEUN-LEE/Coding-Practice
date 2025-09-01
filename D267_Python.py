# 프로그래머스: PCCP- 3번 충돌 위험

## 물류센터 로봇 이용한 자동 운송 시스템 운영
## (r, c) 좌표로 나타낼 수 있는 n개의 포인트 존재, 정해진 운송 경로 m개의 포인트
## 운송시스템 로봇은 x대, 0초에서 시작해서 1초마다 r 좌표, c 좌표 중 하나가 1만큼 감소 또는 증가 
## 최단 경로로 이동하며 여러가지일 떄는 r 좌표가 c 좌표보다 먼저 변함
## 마지막 포인트 도착 시 운송 마치고 물류 센터 벗어남

## 운송포인트 n개의 좌표를 담은 2차원 정수 배열 points, 로봇 x대의 운송 경로를 담은 2차원 정수 배열 routes 
## 같은 좌표에 2대 이상 모인 경우 위험상황. 위험상황이 몇 번 발생하는지 구하기. 
## 어떤 시간에 여러 좌표에서 위험 상황이 발생한다면 그 횟수를 모두 더함

# 딕셔너리 사용한 시뮬레이션 구현
def solution(points, routes):
    # 번호별로 좌표를 map에 담음
    point_map = dict()
    for i in range(len(points)):
        point_map[i+1] = [points]
    
    robots = []
    for route in routes:
        start_x, start_y = point_map.get(route[0])
        robots.append((start_x, start_y, route[::-1]))

    cnt = 0
    while robots:
        tmp_robots = []
        robots_pos = dict()
        for robot in robots:
            x, y, route = robot
            # 로봇 충돌 계산을 위해 현재 위치 로봇 count 추가
            if (x, y) in robots_pos:
                robots_pos[(x, y)] += 1
            else:
                robots_pos[(x, y)] = 1

            # 현재 위치가 목표에 도달한 경우, 목표 경로 제거
            if [x, y] == point_map.get(route[-1]):
                route.pop()
            # 다음 경로가 남은 경우
            if route:
                to_x, to_y = point_map.get(route[-1])
                x, y = move(x, y, to_x, to_y)
                tmp_robots.append((x, y, route))

        # 충돌 위험 계산
        cnt += sum([1 if i >= 2 else 0 for i in robots_pos.values()])
        robots = tmp_robots

    return cnt

def move(x, y, to_x, to_y):
    if x > to_x:
        return (x-1, y)
    elif x < to_x:
        return (x+1, y)
    
    if y > to_y:
        return (x, y-1)
    elif x < to_x:
        return (x, y+1)
    
    return (x, y)