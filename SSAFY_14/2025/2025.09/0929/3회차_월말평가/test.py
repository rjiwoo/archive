# 부모 찾기. 어느 그룹에 속해 있는지 찾기
def find_set(x):

    # 내가 부모라면, 나를 반환
    if x == p[x]:
        return x
    
    # 경로 압축?
    p[x] = find_set(p[x])
    return x

# 합집합
def union_set(x, y):

    # 같은 집합이라면 할 거 없음
    if find_set(x) == find_set(y):
        return
    
    # 집합이 다르다면,
    if p[x] < p[y]:
        p[y] = p[x]
    else:
        p[x] = p[y]


# make-set()
# 본인의 노드는 본인을 가리킴. 나 자신이 부모.
p = [ i for i in range(3)]
print(p)

union_set(1,2)
print(p)
union_set(0,2)
print(p)

for node in p:
    
print(p)