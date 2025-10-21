# 각 집합을 만들어주는 함수
def make_set(n):
    # 1~n 까지의 원소가 "각자 자기 자신이 대표자라고 설정"
    p = [i for i in range(n+1)]
    return p


# # 집합의 대표자를 찾는 함수
# def find_set(x):
#     # 자신 == 부모 -> 해당 집합의 대표자
#     if x == p[x]:
#         return x
    
#     # x의 부모노드를 기준으로 다시 부모를 검색
#     return find_set(p[x])

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
    
    p[y] = rep_x

    # 더 작은쪽으로 연결하는 문제라면, 조건을 추가해준다.
    # if rep_x < rep_y:
    #     p[rep_y] = rep_x
    # else:
    #     p[x] = rep_y

N = 6
p = make_set(N)