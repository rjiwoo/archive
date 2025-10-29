N, M = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
dr = [0, 0, 1]
dc = [-1, 1, 0]

# dir == 0 왼쪽, == 1 오른쪽, == 2 아래쪽
def move_box(dir, box_number, size_r, size_c, r, c):
    rcs = []
    
    check_size = size_c if dir == 2 else size_r
    if dir == 2:
        for i in range(check_size):
            rcs.append((r+size_r-1, c+i))
    elif dir == 0:
        for i in range(check_size):
            rcs.append((r+i, c))
    else:
        for i in range(check_size):
            rcs.append((r+i, c+size_c-1))
    
    cnt = 0
    while True:
        
        flag = False
        for i in range(check_size):
            nr = rcs[i][0] + dr[dir]*(cnt+1)
            nc = rcs[i][1] + dc[dir]*(cnt+1)
            
            if nr > N or nc < 1 or nc > N or graph[nr][nc] != 0:
                flag = True
                break
        if flag:
            break

        cnt += 1

    if dir == 2:
        if cnt > 0:
            for i in range(size_r):
                for j in range(size_c):
                    graph[r+i][c+j] = 0
            
            for i in range(size_r):
                for j in range(size_c):
                    graph[r+dr[dir]*cnt+i][c+dc[dir]*cnt+j] = 1

            boxes[box_number][2], boxes[box_number][3] = (r+dr[dir]*cnt, c+dc[dir]*cnt)
            return True
        return False
    
    if (dir == 0 and c+dc[dir]*cnt == 1) or (dir == 1 and c+dc[dir]*cnt+size_c-1 == N):
        for i in range(size_r):
            for j in range(size_c):
                graph[r+i][c+j] = 0
        boxes[box_number] = -1
        return True
    return False


# 박스 정보
# - 박스 번호, 박스 사이즈, 박스 위치


# 초기 세팅
boxes = {}
box_numbers = []
answer = []
for _ in range(M):
    r = 1
    box_number, size_r, size_c, c = map(int, input().split())
    box_numbers.append(box_number)
    boxes[box_number] = [size_r, size_c, r, c]

    for i in range(size_r):
        for j in range(size_c):
            graph[r+i][c+j] = 1

    move_box(2, box_number, size_r, size_c, r, c)

box_numbers.sort()
dir = 0
while len(answer) < M:

    # 좌나 우로 빼기
    for box_number in box_numbers:
        if move_box(dir, box_number, boxes[box_number][0], boxes[box_number][1], boxes[box_number][2], boxes[box_number][3]):
            box_numbers.remove(box_number)
            answer.append(box_number)
            break

    # 내리기
    while True:
        is_down = []
        for box_number in box_numbers:
            is_down.append(move_box(2, box_number, boxes[box_number][0], boxes[box_number][1], boxes[box_number][2], boxes[box_number][3]))
        
        if True not in is_down:
            break

    dir = (dir+1)%2

for box in answer:
    print(box)