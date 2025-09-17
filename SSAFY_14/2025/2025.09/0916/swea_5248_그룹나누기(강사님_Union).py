def find_set(x):
    if x == parents[x]:
        return x
     
    parents[x] = find_set(parents[x])
    return parents[x]
 
def union_set(x, y):
    x_parent = find_set(x)
    y_parent = find_set(y)
 
    if x_parent < y_parent:
        parents[y_parent] = x_parent
    elif x_parent > y_parent:
        parents[x_parent] = y_parent
     
T = int(input())
  
for tc in range(1, T+1):
    N, M = map(int, input().split())
    connections = list(map(int, input().split()))
 
    # make - set
    parents = [i for i in range(N+1)]
 
    for i in range(0, M*2, 2):
        union_set(connections[i], connections[i+1])
 
    for node in range(1, N+1):
        find_set(node)
 
    print(f'#{tc} {len(set(parents[1:]))}')