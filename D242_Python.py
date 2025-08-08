# 프로그래머스: 음양 더하기
## sings이 false이면 음수로 취급하여 absolutes 각 숫자의 총 합 더하기

def solution(absolutes, signs):
    result = 0
    for i in range(len(absolutes)):
        if signs[i] == False:
            result -= absolutes[i]
        else:
            result += absolutes[i]
    return result
# 예시 입력
absolutes = [4, 7, 12]
signs = [True, False, True]
print(solution(absolutes, signs))