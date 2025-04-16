# 백준 10809: 알파벳 찾기
# https://www.acmicpc.net/problem/10809

S = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    print(S.find(i),end = ' ') # find()는 찾는 문자가 없으면 -1을 반환
# end = ' '로 한 줄로 출력
