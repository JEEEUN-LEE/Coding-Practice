# 프로그래머스: [PCCE 기출문제] 9번 / 이웃한 칸

# 주어진 칸의 색깔과 상하좌우 칸의 색깔이 같은지 비교해서 개수 세기
# 문제 풀이를 위한 틀
    # 1. 정수를 저장할 변수 n을 만들고 board의 길이를 저장합니다.
    # 2. 같은 색으로 색칠된 칸의 개수를 저장할 변수 count를 만들고 0을 저장합니다.
    # 3. h와 w의 변화량을 저장할 정수 리스트 dh, dw를 만들고 각각 [0, 1, -1, 0], [1, 0, 0, -1]을 저장합니다.
    # 4. 반복문을 이용해 i 값을 0부터 3까지 1 씩 증가시키며 아래 작업을 반복합니다.
    #     4-1. 체크할 칸의 h, w 좌표를 나타내는 변수 h_check, w_check를 만들고 각각 h + dh[i], w + dw[i]를 저장합니다.
    #     4-2. h_check가 0 이상 n 미만이고 w_check가 0 이상 n 미만이라면 다음을 수행합니다.
    #         4-2-a. board[h][w]와 board[h_check][w_check]의 값이 동일하다면 count의 값을 1 증가시킵니다.
    # 5. count의 값을 return합니다. 
    
def solution(board, h, w):
	n = len(board)
	cnt = 0
	dh = [0, 1, -1, 0] # 상하좌우 행 변화
	dw = [1, 0, 0, -1] # 상하좌우 열 변화a

	for i in range(4): #상하좌우 
		h_check = h + dh[i]
		w_check = w + dw[i]
	
		# 인덱스가 보드 안쪽일 때만 비교
		if 0 <= h_check < n and 0 <= w_check < n:
			if board[h][w] == board[h_check][w_check]:
				cnt += 1
	return cnt

# 예시
board = [[1, 2, 3], [3, 2, 1], [1, 1, 1]]
h = 1
w = 1
print(solution(board, h, w)) # 1
