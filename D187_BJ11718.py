# 백준 11718번: 그대로 출력하기
# 문제: https://www.acmicpc.net/problem/11718
# 문제: 입력받은 문자열을 그대로 출력하는 문제

while True:
    try:
        print(input()) 
    except EOFError: # EOFError는 파일의 끝에 도달했을 때 발생하는 예외
        break
# 입력을 계속 받아 출력하다가 EOFError가 발생하면 반복문을 종료

