# 프로그래머스: [PCCE 기출문제] 6번 / 물 부족
def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage = usage + usage * change[i] // 100
        total_usage += usage
        if total_usage > storage:
            return i
    
    return -1