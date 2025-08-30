# 프로그래머스: PCCE 8번 닉네임 규칙

def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    if len(answer) < 3:
        answer += "o" * (4 - len(answer)) # 길이가 4가 될 때까지 o 추가
    if len(answer) > 8:
        answer = answer[:8]
    return answer