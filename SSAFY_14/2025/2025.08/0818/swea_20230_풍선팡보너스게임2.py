# 어떤 풍선을 터트리면 같은 행과 열의 풍선이 모두 터진다
# 최대 점수

T = int(input()) # 스테이지 개수

for tc in range(1, T+1):
    N = int(input()) # N*N 배열

    arr = [list(map(int, input().split())) for _ in range(N)]
    max_count = -1

    for r in range(N):
        for c in range(N):

            count = 0
            for i in range(N):
                count += arr[r][i] + arr[i][c]
            count = count - arr[r][c]
            
            if max_count < count:
                max_count = count

    print(f'#{tc} {max_count}')