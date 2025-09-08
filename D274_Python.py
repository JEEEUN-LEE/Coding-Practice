# 프로그래머스: [PCCE 기출문제] 6번 / 가채점
## 가채점 점수가 실점수랑 같으면 same, 다르면 different 
def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:
            answer.append("Same")
        else:
            answer.append("Different")
    
    return answer

# 풀이: 4번째줄 가채점한 결과 = 실제 성적이 되어야 한다.
## score_list는 1번째 학생부터 순서대로 실 성적이 들어있으므로 numbers[i]로 위치값을 넣어주고, score_list에서 그 위치에 해당하는 값을 불러옴. 단, 인덱스는 0부터 시작하므로 -1을 해줌