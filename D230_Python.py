# 프로그래머스: 핸드폰 번호 가리기
## 마지막 4글자 외 나머지 "*"로 가리기

##전체 문자열에서 4글자 뺀만큼 "*" 표시하고
## 마지막 4글자는 출력

def solution(phone_number):
    stars = '*' * (len(phone_number) - 4)
    last_num4 = phone_number[-4:] # 마지막 4글자
    return stars + last_num4
# 예시 입력
phone_number = "01012345678"
print(solution(phone_number))