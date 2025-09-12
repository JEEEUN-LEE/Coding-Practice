# 프로그래머스: [PCCE 기출문제] 4번 / 저축
## 100만원 목표로 몇 달 걸리는지

start = int(input())
before = int(input())
after = int(input())

money = start
month = 1

# 70만원이면 멈추기
while money < 70:
           money += before
           month += 1

while money < 100:
           money += after
           month += 1
print(month)