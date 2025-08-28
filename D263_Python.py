# 프로그래머스: [PCCE 기출문제] 3번 / 수 나누기
## 주어진 수를 100으로 나눈 나머지를 모두 더한 값을 출력
number = int(input())

answer = 0

while number > 0:
    answer += number % 100
    number //= 100

print(int(answer))

# 다른 방식
number = input() # 문자열
answer = 0

while len(number) > 0: # 문자열 길이가 0보다 클 때까지 반복
    answer += int(number[-2:]) # 마지막 두 자리 수를 뽑아서 더하고, 정수로 변환
    number = number[:-2] # 마지막 두자리 제외한 수(문자열 그대로)
    
print(answer)