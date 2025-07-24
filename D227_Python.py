# 프로그래머스: 가운데 글자 가져오기
## 가운데 글자 반환하는 함수 solution 만들기

def solution(s):
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid-1:mid+1] #파이썬 인덱스는 0부터 시작하니까! len(s)= 4라면, s[1:2] 추출되어야함
    else:
        return s[mid]
    
print(solution("abcde"))