# 프로그래머스: 서울에서 김서방 찾기
## seoul 중 'Kim' 찾아서 위치 반환하는 solution 함수 만들기

def solution(seoul):
    index = seoul.index("Kim")
    return f"김서방은 {index}에 있다"
# 예시 입력
seoul = ["Jane", "Kim"]
print(solution(seoul))
## index() 메소드: 리스트 또는 문자열에서 특정 값의 위치 반환(만약 값이 없는 경우 ValueError 발생)