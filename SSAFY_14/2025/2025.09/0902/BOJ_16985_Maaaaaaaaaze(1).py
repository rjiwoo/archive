from pprint import pprint
from itertools import permutations
from collections import deque

def rotate_90_degree(arr):
    rotate_maze = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            rotate_maze[j][4 - i] = arr[i][j]
    return rotate_maze

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
    first, second, third, fourth, fifth = maze[p[0]], maze[p[1]], maze[p[2]], maze[p[3]], maze[p[4]]
    for _ in range(4):
        first = rotate_90_degree(first)
        for _ in range(4):
            second = rotate_90_degree(second)
            for _ in range(4):
                third = rotate_90_degree(third)
                for _ in range(4):
                    fourth = rotate_90_degree(fourth)
                    for _ in range(4):
                        fifth = rotate_90_degree(fifth)

                        current_maze = [first, second, third, fourth, fifth]
                        ans = min(ans, bfs(current_maze))

if ans == 125:
    ans = -1

print(ans)
