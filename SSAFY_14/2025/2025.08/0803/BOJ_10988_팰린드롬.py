# 백준) 6단계. 심화 1 - 10988번. 팰린드롬인지 확인하기
# 앞으로 읽을 때 == 거꾸로 읽을 때, 참/거짓 확인

word = input() # 단어 입력 받기
back_word = word[::-1] # 단어 거꾸로 저장

for i in range(len(word)):
    if word[i] != back_word[i]:
        print(0)
        break
else:
    print(1)