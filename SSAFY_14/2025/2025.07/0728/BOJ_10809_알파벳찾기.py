# 10809번. 알파벳 찾기

S = input()

# 알파벳
alpha = 'abcdefghijklmnopqrstuvwxyz'


for i in alpha:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')