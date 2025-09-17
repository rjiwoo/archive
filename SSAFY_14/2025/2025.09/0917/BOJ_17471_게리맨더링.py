# 백준 17471번 게리맨더링 (필수제출)

# N개의 구역으로 나누어져 있고, 구역은 1번부터 N번까지 번호가 매겨져 있다
# 구역을 두 개의 선거구로 나눠야 하고, 각 구역은 두 선거구 중 하나에 포함
# 선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결

# 구역 A에서 인접한 구역을 통해서 구역 B로 갈 수 있을 때, 두 구역은 연결되어 있다고 한다. 
# 중간에 통하는 인접한 구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함된 구역

from collections import deque

def bfs(group):
    # 아. 방문체크한 길이가 A랑 다르면 연결안된거임. 
    visited = [0] * (N+1)
    q = deque()

    q.append(group[0])
    visited[group[0]] = 1
    count = 1

    while q :
        cur = q.popleft()

        # 현재 위치와 인접한 구역을 확인
        for next in adj[cur]:
            # 다음이 그룹에 포함되어 있고, 방문하지 않았으면
            if next in group and not visited[next]:
                visited[next] = 1
                q.append(next)
                count += 1
    
    # 방문체크한 길이가 group이랑 다르면 연결안된거
    if count == len(group):
        return True
    else:
        return False


def comb(count, idx, target):
    global answer

    if count == target:
        A = picked[:]
        B = [i for i in range(1, N+1) if i not in picked]
        # print(A)
        # print(B)

        # 확인해야하는 거.
        # A랑 B에 속해 있는 구역이 다 인접해 있는가?
        # A랑 B가 똑같은 그룹이 아닌가?

        # bfs로 인접한지 확인할 수 있다는 것 같음..
        # 아. 방문체크한 길이가 A랑 다르면 연결안된거임. 
        # 만약 연결 안되어 있으면 추가적으로 더 할 필요 없는 조합이니까 건너뛰기.
        check_A = bfs(A)
        if check_A == False:
            # print(A)
            return 
        check_B = bfs(B)
        if check_B == False:
            # print(B)
            return 
        
        sum_people_A = sum(people_nums[i] for i in A)
        sum_people_B = sum(people_nums[i] for i in B)
        answer = min(answer, abs(sum_people_A - sum_people_B))


    for i in range(idx, N+1):
        picked.append(i)
        comb(count + 1, i + 1, target)
        picked.pop()


N = int(input()) # 구역의 개수

# 인구가 1번 구역부터 N번 구역까지 순서
people_nums = [0] + list(map(int, input().split()))

# 인접리스트 웅연결된 거 저장하기
adj = [[] for _ in range(N + 1)]
for i in range(1, N+1):
    temp = list(map(int, input().split()))
    adj[i] = temp[1:]

# print(adj)
answer = 1000
picked = []
for i in range(1, N//2+1): # 반만 만들면 중복 안됨
    comb(0,1,i)


if answer == 1000:
    answer = -1
print(answer)