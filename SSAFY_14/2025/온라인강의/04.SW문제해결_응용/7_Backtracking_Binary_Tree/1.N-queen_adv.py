#  일차원 배열로 효율적으로 하는 방법

def check(row):
    for prev_row in range(row):
        # 세로 체크
        if visited[row] == visited[prev_row]:
            return False

        # 열과 행의 차이가 같다 == 현재 col 의 좌우 대각선이다
        # visited 에 저장된 값 = 어느 col에 두었는 가 ?
        # row - prev_row = 행의 차이
        # visited[row] - visited[prev_row] = 열의 차이
        # 이 두 개가 같으면 대각선
        if abs(row - prev_row) == abs(visited[row] - visited[prev_row]):
            return False

    return True


def dfs(row):
    global cnt

    if row == N:
        cnt += 1
        return

    for col in range(N):
        visited[row] = col  # 현재 row 의 col 에 놓았다 라고 가정하고
        if not check(row):  # 세로와 대각선을 체크해준다.
            continue

        dfs(row + 1)

N = 8
visited = [0] * N
cnt = 0

dfs(0)
print(f'N = {N} / answer = {cnt}')
