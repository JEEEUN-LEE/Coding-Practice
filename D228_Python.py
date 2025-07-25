# 프로그래머스: 추억 점수
## name, yearning을 입력받으면, photo에서 해당 인물에 대한 yearning을 찾고, 총 추억점수를 더하기

## name과 yearning을 매칭시켜 딕셔너리로 만들기
## 사진 속 인물 name과 동일한 인물의 추억점수를 딕셔너리에서 찾고, 사진의 총 추억점수를 구하기
def solution(name, yearning, photo):
	score_dict = {}
	for n, y in zip(name, yearning):
		score_dict[n] = y

	answer = []
	for p in photo:
		total = 0
		for person in p:
			if person in score_dict:
				total += score_dict[person]
		answer.append(total)
	return answer