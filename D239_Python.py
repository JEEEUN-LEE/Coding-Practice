def solution(a, b, n):
	answer = 0
# 1. 빈병 개수 n이 교환 가능한 최소 숫자 a 이상일 때까지 반복
	while n >= a:
		# 2. 현재 빈 병으로 받을 수 있는 병 계산
		new_count = n // a*b
		leftover = n % a
		# 3. 총 받은 개수 
		answer += new_count
		n = leftover + new_count
	return answer
# 예시 입력
a = 2
b = 3
n = 10
print(solution(a,b,n))