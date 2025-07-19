# 프로그래머스: 문자열안에 문자열
## https://school.programmers.co.kr/learn/courses/30/lessons/120908?language=python3
## str1 안에 str2가 있다면 1, 없다면 2를 출력하는 solution 함수

def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2 

print(solution("ab6CDE443", "6CD"))