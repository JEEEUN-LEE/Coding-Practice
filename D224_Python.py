# 프로그래머스: 종이 자르기
## M, N이 주어질 때 M*N 크기의 종이를 최소로 가위질 해야하는 횟수 구하기

def solution(M, N):
	return M*N-1 

M, N = map(int, input().split())
print(solution(M, N))
