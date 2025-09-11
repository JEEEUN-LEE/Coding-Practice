#프로그래머스: 가장 많이 받은 선물 

## 이번달까지 기록으로, 다음달 누가 선물 많이 받을지 예측하기 
## 이번달까지 두사람 사이 더 많은 선물 준 사람이 다음달에 선물 하나 받기, 
## 주고받은 기록이 없거나, 같으면 선물지수가 큰 사람이 작은 사람에게 하나 받기     
# 선물지수 = (다른사람에게 준 선물 - 받은 선물 수)    
## friends 친구들 이름 배열, gift 주고받은 선물 기록
import itertools

def solution(friends, gifts):
    # 1. 변수 설계
    myGivenGift = dict()
    giftIndex = dict()
    nextMonthGift = dict()

    for fri1 in friends:
        myGivenGift[fri1] = dict()
        giftIndex[fri1] = 0
        nextMonthGift[fri1] = 0
        for fri2 in friends:
            if fri1 != fri2:
                myGivenGift[fri1][fri2] = 0

    # 2. 주고받은 기록 반영
    for gift in gifts:
        giver, receiver = gift.split()
        myGivenGift[giver][receiver] += 1
        giftIndex[giver] += 1
        giftIndex[receiver] -= 1

    # 3. 모든 친구 쌍 비교
    for f1, f2 in itertools.combinations(friends, 2):
        # A, B간 선물 횟수 비교
        if myGivenGift[f1][f2] > myGivenGift[f2][f1]:
            nextMonthGift[f1] += 1 # A가 더 많이 줬으면 → A의 nextMonthGift += 1
        elif myGivenGift[f1][f2] < myGivenGift[f2][f1]: 
            nextMonthGift[f2] += 1 #B가 더 많이 줬으면 → B의 nextMonthGift += 1
        else:  # 같으면 선물 지수 비교
            if giftIndex[f1] > giftIndex[f2]:
                nextMonthGift[f1] += 1
            elif giftIndex[f1] < giftIndex[f2]:
                nextMonthGift[f2] += 1 # 지수 더 큰 쪽이 nextMonthGift += 1
            # giftIndex 같으면 → 패스

    # 4. 이 중 최댓값 반환
    return max(nextMonthGift.values())