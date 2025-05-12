# 백준 1152번: 단어의 개수
# https://www.acmicpc.net/problem/1152
# 문제: 영어 대소문자와 공백으로 이루어진 문자열이 주어질 때, 단어의 개수를 세는 프로그램을 작성하시오.

word = input()
print(len(word.split())) # split()은 공백 기준을 나누고 리스트로 반환함