# 백준 9086번 문자열
# https://www.acmicpc.net/problem/9086
# 문자열의 첫번째 글자와 마지막 글자를 출력하는 문제
T = int(input())#테스트 개수 입력

for i in range(T): #테스트 개수만큼 반복 
    word = input()
    print(word[0]+word[-1]) #첫번째 글자랑 마지막 글자만 출력