# 백준 15686번 치킨 배달

# N×N인 도시
# 0 빈 칸, 2 치킨집, 1 집
# 도시의 칸은 (r, c)와 같은 형태 r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미 
# r과 c는 1부터 시작한다.

# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
# 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다. 
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합
# 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|

# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업
# 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램


# 현재 치킨 집 중에서 M개를 골라 -> 조합
# 각 조합에서 치킨 거리를 계산해서 모두 합쳐서 '도시의 치킨거리'
# '도시의 치킨거리'를 min_answer로 정해서 최솟값 찾아서 출력

# 어떤 치킨 집을 남길건지 골라
def comb(count, idx):
    # print(picked)
    # 종료조건
    if count == M:
        # print(picked)
        comb_chicken.append(picked[:]) # 깊은 복사해야지 다 복사됨..
        return
    
    for i in range(idx, len(chicken)):
        picked.append(chicken[i])
        comb(count + 1, i + 1)
        picked.pop()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 현재 치킨 집 위치를 저장할 리스트
chicken = []

# 치킨 집을 조합하기 위해 만들어 둔 리스트
picked = []

# 남겨둘 치킨집의 조합들
comb_chicken = []

# 현재 치킨 집의 위치를 저장해
for r in range(N):
    for c in range(N):
        if arr[r][c] == 2:
            chicken.append((r,c))

# 어떤 치킨 집을 남길지 조합 구하기
comb(0,0)
# print(comb_chicken)


# 도시의 치킨거리 최소값
min_answer = 21e9

for i in range(len(comb_chicken)):
    temp = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                min_distance = 21e9 # 현재 집의 치킨거리
                # 치킨집과 집과의 거리 구하기(치킨거리)
                # 해당 집의 최소 치킨거리 구하기
                for j in comb_chicken[i]:
                    distance = abs(j[0] - r) + abs(j[1] - c)
                    min_distance = min(min_distance, distance) # 치킨 거리 확정
                temp += min_distance # 그 도시의 치킨 거리를 구하는 중
               
    min_answer = min(min_answer, temp) # 치킨 집 조합에 따라 도시의 치킨 거리 중에 최소값을 저장

print(min_answer)





