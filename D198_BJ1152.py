# 백준 1152번: 단어의 개수
# https://www.acmicpc.net/problem/1152

sent = input()
word_cnt = len(sent.split())
print(word_cnt)


#============================
# DataFrame의 'A' 컬럼에 문장이 여러 개 들어 있고, 각 문장의 단어 개수 구하기!!
df['word_count'] = df['A'].str.split().str.len()
# .str.split().str.len()