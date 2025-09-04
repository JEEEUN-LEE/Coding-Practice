# 프로그래머스: [PCCE 기출문제] 2번 / 각도 합치기
# 문제 풀이를 위한 틀
## 각도 합친 값을 360으로 나눈 나머지 출력

angle1 = int(input())
angle2 = int(input())

sum_angle = (angle1 + angle2) % 360 #나머지만 출력
print(sum_angle)