#백준 5622번: 다이얼
# https://www.acmicpc.net/problem/5622
# 문제: 전화를 걸기 위해 다이얼을 돌려야 하는데, 각 알파벳에 따라 다이얼을 돌리는 시간이 다르다.
# 각 알파벳에 해당하는 다이얼을 돌리는 시간을 계산하는 프로그램을 작성하시오.

 #1. 입력 받기
 #2. 각 알파벳에 해당하는 시간 딕셔너리 만들기
 #3. for문으로 알파벳 하나씩 돌면서 해당하는 시간을 더하기

word = input()
dial_time = {
    'A':3, 'B':3, 'C':3,
    'D':4, 'E':4, 'F':4,
    'G':5, 'H':5, 'I':5,
    'J':6, 'K':6, 'L':6,
    'M':7, 'N':7, 'O':7,
    'P':8, 'Q':8, 'R':8, 'S':8,
    'T':9, 'U':9, 'V':9,
    'W':10, 'X':10, 'Y':10, 'Z':10
}

time = 0 
for i in word:
    time +=dial_time[i]

print(time)


# 다른 풀이
# word = input()
# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# time = 0

# for i in range(len(word)): # 입력된 문자 수 만큼
#     for j in dial: #다이얼 각 그룹
#         if(word[i] in j): #해당 문자가 다이얼 그룹에 속하면
#             time += dial.index(j) + 3 #인덱스 + 3 더하기

# print(time)