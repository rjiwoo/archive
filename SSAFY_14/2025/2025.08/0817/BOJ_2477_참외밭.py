# 백준 2477번 참외밭

n = int(input()) # 참외개수

graph = []
# 육각형이라 6번 
for _ in range(6):
    graph.append(list(map(int, input().split())))

# print(graph)

max_width = 0
max_height = 0
max_width_idx = 0
max_height_idx = 0

# 가장 긴 가로, 세로 찾기
for r in range(6):
    # 가로 방향 (동:1, 서:2)
    if graph[r][0] == 1 or graph[r][0] == 2:
        if graph[r][1] > max_width:
            max_width = graph[r][1]
            max_width_idx = r

    # 세로 방향 (남:3, 북:4)
    if graph[r][0] == 3 or graph[r][0] == 4:
        if graph[r][1] > max_height:
            max_height = graph[r][1]
            max_height_idx = r

# 큰 사각형
max_area = max_width * max_height


# 작은 사각형 가로: 긴 가로 변의 양 옆 차이
min_width = abs(graph[(max_width_idx - 1) % 6][1] - graph[(max_width_idx + 1) % 6][1])

# 작은 사각형 세로: 긴 세로 변의 양 옆 차이
min_height = abs(graph[(max_height_idx - 1) % 6][1] - graph[(max_height_idx + 1) % 6][1])

min_area = min_width * min_height

# 전체 넓이
print((max_area - min_area) * n)


# 영권오빠 코드 변경

# mango = int(input())
# direction = []
# length = []
# for i in range(6):
#     d, dist = map(int, input().split())
#     direction.append(d)
#     length.append(dist)


# small_square = 0
# for i in range(6):
#     if direction[i] == direction[(i + 2)%6] and direction[(i+1)%6] == direction[(i + 3)%6]:
#         small_square = length[(i + 1)%6] * length[(i + 2)%6]
#         break

# max_width = 0
# max_height = 0
# for j in range(len(direction)):
#     if direction[j] == 1 or direction[j] == 2:
#         max_width = max(length[j], max_width)

#     elif direction[j] == 3 or direction[j] == 4:
#         max_height = max(length[j], max_height)

# large_square = max_height * max_width
# print(mango*(large_square-small_square))         