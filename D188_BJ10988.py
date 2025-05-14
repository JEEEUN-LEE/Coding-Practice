# 백준 10988번: 팰린드롬인지 확인하기
# https://www.acmicpc.net/problem/10988
# 문제: 주어진 문자열이 팰린드롬인지 확인하는 문제

word = input()

if word == word[::-1]:
    print(1)
else:
    print(0)