# 백준 15686번 치킨 배달

# 현재 치킨 집 중에서 M개를 골라 -> 조합
# 각 조합에서 치킨 거리를 계산해서 모두 합쳐서 '도시의 치킨거리'
# '도시의 치킨거리'를 min_answer로 정해서 최솟값 찾아서 출력
#  ==> 중복 계산이 너무 많아
# 거리를 다 저장해두고 꺼내와서 쓰자

# 내가 뽑고 싶은게 4개 있었을 때, 

# 직접 조합을 만들어야하는 경우 : 뽑다가 더 뽑을 필요가 없으면 그만 보는 경우
# itertools를 써야하는 경우 : 중도포기가 안됨. 모든 케이스를 다 봐야한다


def comb(count, idx):
    global min_total 

    if 1 <= count <= M:
        hab = 0
        for j in range(len(house)):
            min_l = 1e9
            for i in range(len(picked)):
                min_l = min(picked[i][j], min_l)
            hab += min_l
        a.append(hab)

    if count == M:
        return
    
    for i in range(idx, len(chi)):
        picked.append(length[i])
        comb(count + 1, i + 1)
        picked.pop()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 좌표 값 1: 그냥 집
house = [] # 그냥 집 x, y 좌표
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i, j])

# 좌표 값 2: 치킨 집
chi = [] # 치킨 집 x, y 좌표
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chi.append([i, j])

# 거리 계산 (2차원 리스트로)
length = []
for c in chi:
    row = []
    for h in house:
        cha = abs(h[0] - c[0]) + abs(h[1] - c[1])
        row.append(cha)
    length.append(row)

picked = []
min_total = 1e9
a = []


comb(0,0)
print(min(a))