# 프로그래머스: 콜라츠 추축 
## 총 몇 번을 반복해야 1이 되는 횟수 출력, 단 500번 이상해도 1이 안되면 -1 출력, 주어진 수가 1이면 0 출력

def solution(num):
	count = 0
	if num == 1: # 1일 때 0반환
		return 0
	
	while num!= 1: # 1이 아닐 때
		if num % 2 == 0: # 짝수
			num = num // 2
		else: # 홀수
			num = num *3 +1
		count +=1
		
		if count >= 500:
			return -1
	return count