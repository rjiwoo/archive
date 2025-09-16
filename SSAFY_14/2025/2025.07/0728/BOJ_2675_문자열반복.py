# 2675번 문자열 반복

T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    for i in range(len(S)):
        print(S[i]*R, end='')
    print()