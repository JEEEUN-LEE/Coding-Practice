# 프로그래머스: 문자열 다루기 기본
## s 문자열 길이가 4 or 6이고, 숫자로만 되어 있는지 확인하여 True, False 출력

def solution(s):
    if len(s) == 4 or len(s) == 6:   
        for ch in s:
            if ch < '0' or ch > '9': # 숫자 범위 벗어나면 False
                return False
        return True                  
    return False

## 다른 풀이   
def solution(s):
    if len(s) in [4, 6] and s.isdigit(): # 길이 4 또는 6이고, 숫자로만 되어있으면 True
        return True
    return False
# 예시 입력
print(solution("1234")) # True
print(solution("1ag23456")) # False
    
## isdigit: 문자열이 숫자로만 이루어져 있는지 확인하는 메서드
