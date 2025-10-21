# 코드트리 
# 2025 하반기 오전 1번 - 택배 하차

# 택배 N x N
# 택배 투입 : 택배는 직사각형 모양, 직사각형 왼쪽 열의 위치 c, 가로크기 w, 세로크기 h, 택배 번호 k
# 택배는 맨 아래로 떨어짐. 내려가던 중 다른 짐을 만나면 멈춤

# 택배 하차
# 좌측 : 왼쪽으로 이동했을 때, 다른 택배와 부딪히지 않고 뺄 수 있는 택배 먼저 하차
#        여러개의 경우 택배 번호 k 가 작은 택배 먼저 하차
#        택배 하차 후, 떨어질 수 있는 택배는 떨어짐
# 우측 : 좌측 하차와 동일
# 
# 택배를 모두 하차할 때까지 2, 3의 과정 반복
# 하차되는 택배의 번호를 순서대로 출력

# 풀이 생각
#   1. 택배가 투입되서 최종적으로 위치할 공간을 찾기
#       - 택배 공간의 바닥에 닿으면 멈춤
#       - 다른 택배가 이미 공간을 자치하고 있으면 그 전에 멈춤
#   2. 공간에 택배로 채우기(해당 택배 번호로 채울 것)  
#   3. 맨 왼쪽에 있는 택배 찾기(택배의 왼쪽에 아무것도 없는 택배들을 찾으면 될 듯)
#   4. 택배 번호가 작은 순서대로 제거(제거하는 택배의 번호 순서를 따로 저장해두기) 
#   5. 하나 제거하면 공간 다시 탐색해서 떨어질 택배 있으면 떨구기
#       - 맨 아래의 택배부터 확인해서 떨어지는게 가능하면 위의 택배도 떨구면 되려나?   
#   6. 왼쪽 다 빼고 나면, 오른쪽도 위의 순서 반복

# 풀이 생각 1.택배가 투입되서 최종적으로 위치할 공간을 찾기
def find_r(h, w, c):
    # graph의 맨 위(r=0)부터 맨 아래(N-h)까지 반복
    for r in range(N - h + 1):  # r은 택배의 맨 위 행의 번호
        if r + h == N:          # r + h - 1 = 택배의 맨 아래 행의 번호
            return r
        else: 
            for i in range(c, c + w):
                if graph[r + h][i] != 0:
                    return r

# 풀이 생각 2.해당 위치에 박스로 채우기
def fill_box(k, h, w, r, c):
    for i in range(r, r + h):
        for j in range(c, c + w):
            graph[i][j] = k

# 왼쪽 택배 하차 가능한지 확인
def can_remove_left(k):
    h, w, r, c = box_info[k]

    # 맨 왼쪽에 위치하면 택배 하차 가능
    if c == 0:
        return True
    
    # 해당 택배의 왼쪽이 다 공백이 아니면 하차 불가능
    for i in range(r, r + h):
        for j in range(c):
            if graph[i][j] != 0:
                return False
    return True
    

# 박스 제거
def remove(k):
    for r in range(N):
        for c in range(N):
            if graph[r][c] == k:
                graph[r][c] = 0


N, M = map(int, input().split())   # 택배가 쌓일 공간 N x N , 투입될 택배의 개수 M
graph = [[0]*N for _ in range(N)]   # 택배가 쌓일 공간 0으로 생성
remove_order = []   # 박스 하차한 순서 저장
box_info = {} # 택배 정보를 저장

for _ in range(M):
    k, h, w, c = map(int, input().split())
    c = c - 1   # graph는 0부터 시작인데, c는 1부터 시작이라서 맞춰주기
    box_info[k] = (h, w, r ,c) 

    # 1. 택배가 시작하는 r(행) 위치 찾기. -> 왼쪽 상단의 시작점을 알 수 있음
    r = find_r(h, w, c) 

    # 2. 택배 채우기
    fill_box(k, h, w, r, c)
# print(graph)

# 3. 맨 왼쪽 찾기
#       - 택배 번호가 작은 것부터 확인
#       - 택배의 왼쪽 면만큼 
for k in range(1, M + 1):
    if k not in box_info:
        continue
    # 왼쪽으로 택배 하차가 가능하다면,
    if can_remove_left(k):
        remove(k)   # 택배 제거
        remove_order.append(k)  # 제거한 택배 번호 저장
        del box_info[k]


    # 다시 택배공간 봐서 택배가 아래로 이동할 수 있으면 이동
    # 제거한 택배의 위의 박스만 보면 될 것 같은데, 아래로 내리면 되니까 
    


