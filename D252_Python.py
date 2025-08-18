# 프로그래머스: 약수의 개수와 덧셈
## 약수가 짝수면 약수의 최댓값을 더하고, 홀수면 약수의 최솟값을 더함
def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        if int(n**0.5) == n**0.5:  # 제곱수라면 약수 개수는 홀수
            answer -= n
        else:
            answer += n  # 제곱수가 아니라면 약수 개수는 짝수
    return answer 
# 예시 입력
print(solution(13, 17))
