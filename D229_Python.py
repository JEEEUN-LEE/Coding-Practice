# 딕셔너리 컴프리헨션
# comp_dic = {key:0 for key in range(0,10)}
# 결과: {0:0, 1:0, 2:0, 3:0...}
# {key: value for key in range(1,10)}

# 이전 코드에 적용하면 
def solution(name, yearning, photo):
    # 딕셔너리 컴프리헨션으로 score_dict 생성
    score_dict = {n: y for n, y in zip(name, yearning)}
    
    answer = []
    for p in photo:
        total = 0
        for person in p:
            if person in score_dict:
                total += score_dict[person]
        answer.append(total)
    return answer

# 예시 입력
name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain"], ["radi"], ["may", "kain", "radi"]]
print(solution(name, yearning, photo))
