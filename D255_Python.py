# 프로그래머스: 카드 뭉치
## 문자열로 이루어진 배열 여러개를 활용하여, goal의 배열을 만들 수 있으면 Yes를/ 없으면 No를 출력
## 단, 각 배열의 순서를 변경할 수 없음

# 문제 풀이를 위한 틀 
## goal의 각 배열을 뽑아서, 해당 단어가 cards1 또는 cards2에서 있는 확인하고 꺼내기, 없으면 No를 출력 

def solution(cards1, cards2, goal):
    for word in goal:
        if len(cards1) > 0 and cards1[0] == word:
            cards1.pop(0) #cards1에서 단어 꺼내기
        elif len(cards2) > 0 and cards2[0] == word:
            cards2.pop(0) #cards2에서 단어 꺼내기
        else:
            return "No"
    return "Yes"

# 예시 입력
print(solution(["i", "card", "you"], ["have", "a", "dream"], ["i", "have", "a", "dream"])) # Yes
print(solution(["i", "card", "you"], ["have", "a", "dream"], ["i", "have", "dream"])) # No