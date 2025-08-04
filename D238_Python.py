# 프로그래머스: 문자열 내 p와 y의 개수
## 문자열 s에 p와 y의 개수가 같으면 True, 다르면 False 출력

# 문제 풀이를 위한 틀
##1. 
def solution(s):
    s = s.lower()
    p_count = s.count("p")
    y_count = s.count("y")
    if p_count == y_count:
        return True
    else:
        return False
# 예시 입력
s = "pPoooyY"
print(solution(s))