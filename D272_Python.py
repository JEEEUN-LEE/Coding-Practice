# 프로그래머스: [PCCE 기출문제] 10번 / 데이터 분석
## data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후 sort_by에 해당하는 값을 기준으로 오름차순으로 정렬
# 핵심은 데이터 안 원소 돌면서 ext, val_ext 기준으로 데이터 고르기

def solution(data, ext, val_ext, sort_by):
    
    # 데이터 타입
    data_type = { "code":0, "date": 1, "maximum":2, "remain":3 }
    
    # data를 ext 기준으로 val_ext보다 작은 것만 추출
    filtered_data = []
    
    for d in data: # 데이터 원소 하나씩 체크
        if d[data_type[ext]] < val_ext: 
            filtered_data.append(d)
            
    # 추출된 데이터 오름차순 정렬
    sorted_filtered_data = sorted(filtered_data, key = lambda x: x[data_type[sort_by]]) #sort_by 키 값을 찾아, 키 값 기준으로 각 원소 x[1]-> date로 정렬
    return sorted_filtered_data

# 예시 입력
data = [
    [1, "2023-01-01", 100, 50],
    [2, "2023-01-02", 200, 100],
    [3, "2023-01-03", 300, 150],
    [4, "2023-01-04", 400, 200],
]
ext = "maximum"
val_ext = 250
sort_by = "date"

print(solution(data, ext, val_ext, sort_by))