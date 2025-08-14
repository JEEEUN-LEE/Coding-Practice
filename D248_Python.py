# 프로그래머스: 제일 작은 수 제거하기
## arr 에서 가장 작은수를 제거한 후 출력, 빈 배열이면 -1 출력
def solution(arr):
	if len(arr) == 1:
		return [-1]
	else:
		min_value = min(arr)
		arr.remove(min_value)
		return arr
# 예시 입력
arr = [3, 2, 1, 4]
print(solution(arr))