# 프로그래머스: PCCE- 8번 창고 정리

## 정리된 창고에서 개수가 가장 많은 물건 이름 출력



## 문제 풀이를 위한 틀



def solution(storage, num):

    clean_storage = []

    clean_num = []

    for i in range(len(storage)):

        if storage[i] in clean_storage: # clean_storage에 있는거면 위치 찾아서, 개수 더하기

            pos = clean_storage.index(storage[i])

            clean_num[pos] += num[i]

        else:

            clean_storage.append(storage[i]) # clean_storage에 없으면 새로운 항목을 clean_storage에 추가 

            clean_num.append(num[i]) # clean_num에 추가



    max_num = max(clean_num)

    answer = clean_storage[clean_num.index(max_num)] # max_num을 가진 인덱스를 찾고, 그거의 상품을 찾기

    return answer 





# <깨알 통계 - 신뢰구간 95%의 정확한 의미는?>

# - 구간 추정이란 추정값이 폭을 가지고 추정하는 것. 

# - 신뢰 계수란 구간 추정 폭에 대한 신뢰 정도를 확률로 표현한 것

# - 구간 추정에 필요한 정보는 자유도(표본크기 - 1), 표본 평균, 표본 오차이다.

# - 1. 모집단분포에서 표본을 추출한다.

# 2. 같은 방법으로 95% 신뢰구간을 계산한다.

# 3. 이 시행을 여러번 반복한다.

# 4. 모든 시행 중 원래 모집단이 신뢰구간에 포함되는 비율이 95%이다.

# (95% 신뢰구간을 구하는 시행을 2만번 반복 수행)

