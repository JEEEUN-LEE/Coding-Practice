# 프로그래머스: 이상한 문자 만들기
## 문자열 s, 짝수번째는 대문자, 홀수번쨰는 소문자 
def solution(s):
    answer = ''
    words = s.split(' ')
    
    for word in words:
        new_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        answer += new_word + " "
    return answer [:-1]

# 입력 예시
print(solution("try hello world")) # "TrY HeLlO WoRlD"
