# SWEA 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기

# 3회차 월말평가

# 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 적어서 제출
# 한 조에 제한X
# 여러 사람이 한 사람을 지목한 경우 모두 같은 조

# 적지 않고, 지목되지 않은 사람은 단독으로 조 구성
# 1~N번까지 출석번호 
# M 장의 신청서 제출
# 몇 개의 조가 만들어지는지?


# 집합의 대표자를 찾는 함수 + 경로 압축
def find_set(x):
    # 자신 == 부모 -> 해당 집합의 대표자
    if x == p[x]:
        return x
    
    # 경로 압축 (대표자를 바로 가르키도록하는 것)
    p[x] = find_set(p[x])
    
    # x의 부모노드를 기준으로 다시 부모를 검색
    return p[x]


# 두 집합을 합치는 함수
def union_set(x, y):
    # x, y 의 대표자를 검색
    rep_x = find_set(x)
    rep_y = find_set(y)

    # 만약 이미 같은 집합
    if rep_x == rep_y:
        return # 같은 집합끼리는 합칠 필요가 없다.
    
    # p[y] = rep_x

    # 더 작은쪽으로 연결하는 문제라면, 조건을 추가해준다.
    if rep_x < rep_y:
        p[rep_y] = rep_x
    else:
        p[x] = rep_y


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = list(map(int, input().split()))

    # make set() : 각 집합을 만드는 것
    p = [i for i in range(N+1)]

    # adj_list = [[] for _ in range(N+1)]   # 인접리스트
    for i in range(0, len(info), 2):
        union_set(info[i], info[i+1])
        # adj_list[info[i]].append(info[i+1])

    # print(adj_list)

    print(p)

    # 경로 압축?
    for node in range(1, N+1):
        find_set(node)
 
    print(f'#{tc} {len(set(p[1:]))}')