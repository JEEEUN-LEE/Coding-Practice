# 프로그래머스: 문자열 붙여서 출력하기
## 문자열끼리 이어서 출력

str1, str2 = input().strip().split(' ') #문자열 2개 인자 받아서, '+'로 이어주기
print(str1+str2)

# 프로그래머스: [PCCE 기출문제] 9번 / 지폐 접기 
## rule: 항상 길이가 긴 쪽을 반으로 접기, 접기 전 길이가 홀수였다면 접은 후 소수점 이하 버리기, 접힌 지폐를 그대로 또는 90도 돌려서 지갑에 넣을 수 있다면 그만 접기
## wallet- 지갑 가로, 세로 크기/ bill - 지폐 가로, 세로 크기
## 지갑 넣기 위해 최소 몇 번 접어야 하는지 출력

def solution(wallet, bill):
    answer = 0
    # 종료조건: 어느 한쪽이 지갑보다 큰 경우 무한 반복
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        # 더 큰 쪽을 찾아서 접기
        if bill[0] > bill[1]: # 가로가 더 길 때
            bill[0] = bill[0] // 2
        else: # 세로가 더 길 때
            bill[1] = bill[1] // 2
        answer += 1 # 접는 횟수 증가
    return answer

# 예시 입력
wallet = [6, 4]
bill = [18, 3]
print(solution(wallet, bill))
