# 프로그래머스: 푸드 파이트 대회
## 음식을 왼쪽-> 오른쪽/ 오른쪽-> 왼쪽 순으로 먹고 가운데 물을 먼저 먹는 선수 승리
## 칼로리가 낮은 음식부터 먼저 먹기 
## 0번(물)은 무조건 1개, 그 뒤부터 1번음식 개수, 2번음식 개수..food 배열, 그럴 경우 대회용 음식 배치를 문자열로 출력

# 문제 풀이를 위한 틀
## 왼쪽 절반 음식 리스트 만들어서 문자열로 합치고, 가운데 "0", 왼쪽 절반의 역순으로 붙이기

def solution(food):
    left_parts = [] #왼쪽 절반 음식 리스트
    
    for i in range(1, len(food)): #0번은 무조건 물 1개여서 제외
        cnt = food[i] // 2 
        if cnt > 0: # 음식 개수가 2개 이상인 경우 배치
            left_parts.append(str(i) *cnt) #음식 번호 * 개수 만큼 문자열로 만들어서 리스트에 넣기
    left = ''.join(left_parts) #리스트를 문자열로 합치기 
    return left + '0' + left[::-1]

# 예시 입력
print(solution([1, 3, 4, 6])) # "122333022111"

## 다른 풀이
def solution(food):
	answer = ''
	rev = ''
	for i in range(1, len(food)):
		answer += str(i) * (food[i] // 2)
	rev = answer[::-1]
	answer += '0'

	return answer + rev