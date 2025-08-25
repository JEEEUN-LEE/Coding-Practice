# 프로그래머스: PCCE 기출문제- 심폐소생술
## 방법이 정수 배열로 주어짐.  각 몇 번째 단계인지 순서대로 담아 출력

def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        for i in range(0, len(basic_order)):
            if action == basic_order[i]:
                answer.append(i+1)
    return answer

# 예시 입력
print(solution(["pressure","check", "call", "respiration", "repeat"]))
