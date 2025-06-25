# 10708번: 세로읽기
# 세로로 읽은 단어를 출력하는 문제

# 외부 반복문은 최대 15자여서 15까지
# 내부 반복문은 총 5줄이여서 5까지
# 각 단어 i 번쨰 글자를 가져와서 result에 추가
words = [input().strip() for _ in range(5)]
result = ""

for i in range(15):
    for j in range(5):
        if i < len(words[j]):
            result += words[j][i]

print(result)
