# SWEA 2819. 격자판의 숫자 이어 붙이기

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 1. 종료 조건: 숫자 7자리 일 때 종료
# 2. 가지의 수 : 4개 (상하좌우)
def recur(r, c, number):

    if len(number) == 7: # 7자리면 종료
        result.add(number) # set 에 추가
        return

    for i in range(4): # 상하좌우
        nr = r + dr[i]
        nc = c + dc[i]

        # 범위 밖이면 다음 방향 확인 continue
        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
            continue

        # 다음 위치로 이동
        recur(nr, nc, number + matrix[nr][nc])


T = int(input())

for tc in range(1, T+1):
    matrix = [input().split() for _ in range(4)]
    result = set()

    # 7자리 만드는 코드
    #   - 4 * 4 가 모두 출발점이 될 수 있다.
    for sr in range(4):
        for sc in range(4):
            recur(sr, sc, matrix[sr][sc])

    print(f'#{tc} {len(result)}')