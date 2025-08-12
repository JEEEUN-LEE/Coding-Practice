# 프로그래머스: 부족한 금액 계산하기
## 이용료- 기본료 price, N번째*price
## 금액이 얼마 부족한지 출력, 부족하지 않으면 0 출력
def solution(price, money, count):
    total = 0 # 필요한 금액
    for i in range(1, count+1): #N번 반복 실행
        total += price*i #price * n만큼 더해주기
    answer = total - money
    return answer if answer > 0 else 0
# 예시 입력
price = 3
money = 20
count = 4
print(solution(price, money, count))