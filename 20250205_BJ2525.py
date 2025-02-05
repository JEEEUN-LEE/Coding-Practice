# 2525: 오븐 시계
    # 시간 입력받기
    # 입력받은 시간에 요리 시간 더하기
    # 60분 이상 넘어가면 시간으로 바꾸기
    # 24시간 넘어가면 0시로 바꾸기

H, M = map(int, input().split())
T = int(input())

M += T
# 분이 60일 때
if M >= 60:
    H += M//60 #60으로 나눈 몫을 더해줌
    M %= 60 #60으로 나눈 나머지를 분으로
    
# 24시간 넘으면 0시로
if H >= 24:
    H -= 24 #24를 빼줌
    
print(H,M)
