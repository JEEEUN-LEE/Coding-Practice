# 프로그래머스: 삼총사
## 3명의 학생 정수번호 합이 0일 때 삼총사
## 삼총사를 만들 수 있는 방법의 수를 출력
def solution(number):
    answer = 0
    n = len(number)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer
# 예시 입력
number = [-2, 3, 0, 2, -5, 5, 1, 1, -1]
print(solution(number))
