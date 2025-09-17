# 문제2 : 사과수확(배점: 35점)

## 아니면 그냥 갈 수 있는거 다 조합해서 거리 계산하고 짧은거 저장

def perm(count):
    if count == N:
        # 시작과 처음은 무조건 0.0으로 돌아와야함
        print(picked)
        
        return

    for i in range(N): 
        if not visited[i]:
            picked.append(i)
            visited[i] = 1
            perm(count + 1)
            picked.pop()
            visited[i] = 0




T = int(input())

for tc in range(1, T+1):

    N = int(input()) # 사과의 개수
    apple_index = [tuple(map(int, input().split())) for _ in range(N)]
    answer = 0

    print(apple_index)

    picked = []
    visited = [0] * N

    perm(0)

    # arr = [[0] * 10 for _ in range(10)]
    # print(arr)

    # for r in range(10):
    #     for c in range(10):
    #         arr[r][c] = abs(apple_index[c][0] - apple_index[c+1][0]) + abs(apple_index[c+1][1] - apple_index[c+1][1])


    # for i in range(len(apple_index)):
    #     for r in range(N+1):
    #         for c in range(N+1):
    #             # for i in range(len(apple_index)):
    #                 arr[r][c] = abs(apple_index[i][0]-apple_index[i+1][0]) + abs(apple_index[i][1]-apple_index[i+1][1])

    print(f'#{tc} {answer}')



