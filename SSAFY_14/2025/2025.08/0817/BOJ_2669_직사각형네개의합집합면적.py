# 백준 2669번 직사각형 네개의 합집합 면적 구하기

graph = [[0]*101 for _ in range(101)]

# print(graph)

for _ in range(4):
    left_x, left_y, right_x, right_y = map(int, input().split())

    # 2차원 배열에서는 x,y가 반대임
    for x in range(left_x, right_x):
        for y in range(left_y, right_y):
            graph[x][y] = 1

count = 0
for r in range(101):
    for c in range(101):
        if graph[r][c] == 1:
            count += 1

print(count)