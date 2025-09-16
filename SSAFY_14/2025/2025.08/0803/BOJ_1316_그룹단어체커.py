# 백준) 6단계. 심화 1 - 1316번. 그룹 단어 체커

# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
# 한국말 이해가 어려웠음. 그룹 단어를 개수를 세라는 게 연속된 알파벳 개수를 세라고 착각함
# for-else 사용법 다시 한 번 읽기

N = int(input())

group_word = 0

for _ in range(N):
    word = input()

    # 이미 나온 문자를 체크
    check = []
    
    for i in word:
        # 현재 문자가 이전에 나온 적이 없는 경우
        if i not in check:
            check.append(i)

        # 현재 문자가 이전에 나온 적이 있는 경우
        elif i != check[-1]:    # 바로 앞의 문자랑 다르면 그룹 단어X
            break

    # break문이 실행되지 않으면 그룹 단어임
    else: group_word += 1
            
print(group_word)