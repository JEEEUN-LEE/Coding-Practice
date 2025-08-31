# 프로그래머스: PCCE 3번 버스
## year와 age_type을 통해, 2030년에 몇 살인지 구하기 

year = int(input())
age_type = input()

if age_type == "Korea":
    answer = (2030 - year) + 1

elif age_type == "Year":
    answer = 2030 - year

print(answer)