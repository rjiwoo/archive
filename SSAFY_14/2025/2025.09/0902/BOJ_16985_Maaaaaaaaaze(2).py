from collections import deque
from itertools import permutations
# 판이 5개 주어짐
# 쌓는 순서와, 판의 회전 여부는 자유(90도,180도,270도)
# 0,0,0으로 입장, 4,4,4로 탈출

# 가지치기 -> 완탐
# 1. 불능해 sort
# 1.1 시작점(0,0,0)과 끝점(4,4,4)는 반드시 1
# 1.2 1.1을 만족하는 경우에서, 5개의 판을 겹쳐 쌓았을때(0과 1이 만나면 1로) 미로 탈출 불가능하면 불능해
# 2. 불능해를 만난 경우에는 보고 있는 판을 돌려서 다시 1번의 과정을 수행
# 3. 불능이 아닌 해에 대해 BFS 수행 후 해를 출력
# 
# 추가 아이디어
# 모든 판의 회전 횟수가 같으면 원형이랑 같다(볼 필요 없다. 이미 본 것)
# 판 별 회전 횟수를 받아주는 변수도 있어야 할 것
# 
 
# 회전 함수 turn
dir=0
def turn(plate):
    turn_plate=[[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            turn_plate[i][j]=plate[4-j][i]
    return turn_plate

# 미로 탈출 함수
def bfs(maze):
    cnt = 125

    if maze[0][0][0] == 1 and maze[4][4][4] == 1:
        q = deque()
        q.append([0, 0, 0])
        visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
        visited[0][0][0] = 1

        while q:
            r, c, k = q.popleft()
            if r == 4 and c == 4 and k == 4:
                cnt = min(cnt, visited[r][c][k]-1)
                break
            for dr, dc, dk in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
                nr = r + dr
                nc = c + dc
                nk = k + dk
                if 0 <= nr <= 4 and 0 <= nc <= 4 and 0 <= nk <= 4:
                    if visited[nr][nc][nk] == 0 and maze[nr][nc][nk] == 1:
                        q.append([nr, nc, nk])
                        visited[nr][nc][nk] = visited[r][c][k] + 1
    return cnt

maze = []
ans = 125
for _ in range(5):
    temp = []
    for _ in range(5):
        temp.append(list(map(int, input().split())))
    maze.append(temp)

perm = list(permutations([0, 1, 2, 3, 4], 5))

for p in perm:
    r0, r1, r2, r3, r4 = maze[p[0]], maze[p[1]], maze[p[2]], maze[p[3]], maze[p[4]]
    for _ in range(4):
        r0 = turn(r0)
        for _ in range(4):
            r1 = turn(r1)
            for _ in range(4):
                r2 = turn(r2)
                for _ in range(4):
                    r3 = turn(r3)
                    for _ in range(4):
                        r4 = turn(r4)
                        current_maze = [r0, r1, r2, r3, r4]
                        ans = min(ans, bfs(current_maze))
                        if ans==12:
                            print(12)
                            exit()

if ans == 125:
    ans = -1

print(ans)