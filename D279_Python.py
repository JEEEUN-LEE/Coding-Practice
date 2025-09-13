# 프로그래머스: [PCCE 기출문제] 5번 / 가습기

## 문제 풀이를 위한 틀
## 각 모드별 설정 함수, solution 함수로 모드대로 함수 호출
def func1(humidity, val_set):
    if humidity < val_set:
        return 3

    return 1

def func2(humidity):
    if humidity >= 50:
        return 0
    elif humidity >= 40:
        return 1
    elif humidity >= 30:
        return 2
    elif humidity >= 20:
        return 3
    elif humidity >= 10:
        return 4

    return 5


def func3(humidity, val_set):
    if humidity < val_set:
        return 1
    return 0


def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func2(humidity)

    elif mode_type == "target":
        answer = func1(humidity, val_set)

    elif mode_type == "minimum":
        answer = func3(humidity, val_set)

    return answer



def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func2(humidity)

    elif mode_type == "target":
        answer = func1(humidity, val_set)

    elif mode_type == "minimum":
        answer = func3(humidity, val_set)

    return answer
