# 프로그래머스: 편지
## 글자 한자 당 2cm 크기로 적을 때, 필요한 편지지 최소 가로 길이 출력하는 solution 함수

def solution(message):
	return len(message) * 2 #글자 당 2cm니까 글자수보다 2 곱한 만큼

print(solution("happy birthday")) 