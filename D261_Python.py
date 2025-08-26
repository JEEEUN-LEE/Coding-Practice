# 프로그래머스: 병과분류

## 환자 코드 따라 어디 병과 진료인지 출력

code = input()

last_four_words = code[-4:] #마지막 네글자

if last_four_words == '_eye':
    print('Ophthalmology')

elif last_four_words == 'head':
    print('Neurosurgery')

elif last_four_words == 'infl':
    print('Orthopedics')

elif last_four_words == 'skin':
    print('Dermatology')

else:
    print('direct recommendation')