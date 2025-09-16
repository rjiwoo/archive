# 백준) 7단계. 2차원 배열 - 10798번. 세로 읽기

n = [list(input()) for _ in range (5)]

# print(n)

new = ''
for r in range(15):
    for c in range(5):
        # 인덱스가 없는 경우, 건너뛰기
        if len(n[c]) > r:
            # continue

        # if n[c][r] is False:
        #     continue
            new += n[c][r]

print(new)


# 열을 읽어나갈 때, 글자가 없는 경우 때문에 
#     new += n[c][r]
#            ~~~~^^^
# IndexError: list index out of range