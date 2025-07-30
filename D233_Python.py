# 프로그래머스: 둘만의 암호
# 문제 설명
# 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔주되, skip에 해당하는 문자는 건너뛰고, z를 넘으면 다시 a로 돌아간다.
# 예를 들어 s = "aukks", skip = "wbqd", index = 5 일 때, "happy"를 반환한다.

## < 문제 해결 위한 풀이 틀 >
## 1. 먼저 26개 알파벳 문자열 생성, 반복문으로 skip 문자는 제외하고 사용 가능한 알파벳으로만 문자열 생성
## 2. s 문자열 각 문자가 usable 중 몇 번째 인덱스인지, 인덱스만큼 뒤로 이동하고, 변환된 문자를 새 문자열로 추가


def solution(s, skip, index):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    usable = [ch for ch in alphabet if ch not in skip]
    result = ''
    
    for ch in s:
        idx = usable.index(ch)
        new_ch = usable[(idx + index) % len(usable)] # 뒤로 index만큼 가되, z까지 가면 처음부터 a부터 다시 시작
        result += new_ch

    return result
# 예시 입력
s = "aukks"
skip = "wbqd"
index = 5
print(solution(s, skip, index))
