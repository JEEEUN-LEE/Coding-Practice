# 프로그래머스: 두 개 뽑아서 더하기
## 배열 numbers에서 두 정수 합의 경우를 모두 오름차순으로 출력
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(set(answer)) #중복 제거하고, 오름차순 정렬
    
# 예시 입력
print(solution([2, 1, 3, 4, 1])) # [2, 3, 4, 5, 6, 7]
 

