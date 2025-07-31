# 프로그래머스: 가장 가까운 같은 글자
## 문자열 s, 각 문자마다 앞에 있는 것 중에서 가장 가까운 글자를 찾고 그 글자와 위치 차이만큼 수를 출력하기. 단, 앞에 같은 글자 없는 경우 -1로 출력

def solution(s):
	answer = []
	last_seen = {}

	for i, ch in enumerate(s):
		if ch in last_seen:
			answer.append(i - last_seen[ch]) # 같은 문자 있으면 현재 인덱스와 차이만큼 저장 
		else:
			answer.append(-1)
		last_seen[ch] = i # 현재 위치 갱신
	return answer
# 예시 입력
s = "banana"
print(solution(s))


