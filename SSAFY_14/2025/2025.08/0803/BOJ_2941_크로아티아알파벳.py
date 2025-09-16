# 백준) 6단계. 심화 1 - 2941번. 크로아티아 알파벳

# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력
# c_alph 에 들어있는 문자는 무조건 하나의 알파벳으로 쓰임


c_alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

# 해당 문자열에 하나의 알파벳으로 인식되는 문자가 있으면, 'a'로 변경해서 개수 세기
for i in c_alph:
    word = word.replace(i,'a')

print(len(word))



# word가 문자열이라는 것을 잊고, remove를 사용해서 삭제해보고자 했음
# 문자열은 불변 객체. 

# count = 0
# alph = []

# for i in c_alph:
#     if i in word:
#         word.remove(i)
#         count += 1
        
# count += len(word)



