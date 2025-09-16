# 백준 1018번 체스판 다시 칠하기

N, M = map(int, input().split())

graph = [list(input()) for _ in range(N)]

min_count = 64

for r in range(N-7):
    for c in range(M-7):
        count_1 = 0 # 짝수가 검정(첫번째칸 검정)
        count_2 = 0 # 홀수가 검정(첫번째칸 흰색)

        for i in range(8):
            for j in range(8):

                if (i+j) % 2 == 0: # 짝수칸
                    if graph[r+i][c+j] != 'B': # 짝수칸이 검정이 아니면
                        count_1 += 1
                    if graph[r+i][c+j] != 'W': # 짝수칸이 흰색이 아니면
                        count_2 += 1
                else:
                    if graph[r+i][c+j] != 'W': # 홀수칸이 흰색이 아니면
                        count_1 += 1
                    if graph[r+i][c+j] != 'B': # 홀수칸이 검정이 아니면
                        count_2 += 1

        # 첫번째칸 검정으로 칠하는 경우 VS 흰색으로 칠하는 경우
        count = min(count_1,count_2)
        
        if min_count > count:
            min_count = count

print(min_count)