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

# 문제 해결 위한 풀이 틀
# 1. 빈 리스트 answer와 빈 딕셔너리 last_seen 생성
# 2. enumerate()로 문자열 s의 각 문자와 인덱스 i를 순회
# 3. 만약 현재 문자 ch가 last_seen에 있다면, answer에 현재 인덱스 i와 last_seen[ch]의 차이를 추가
# 4. 만약 현재 문자 ch가 last_seen에 없다면, answer에 -1을 추가
# 5. 마지막으로, last_seen[ch]에 현재 인덱스 i를 저장하여 다음 순회에서 사용할 수 있도록 갱신
# 6. answer를 반환

