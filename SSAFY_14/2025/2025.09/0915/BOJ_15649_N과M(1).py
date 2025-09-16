#  15649번 N과 M (1)

# 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

# 사전 순으로 증가하는 순서로 출력
# -> 순열

def perm(count):

    if count == M:
        print(*picked)  
        return
    
    for i in range(N):
        if not visited[i]:
            picked.append(arr[i])
            visited[i] = 1
            perm(count + 1)
            visited[i] = 0
            picked.pop()

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
# print(arr)

picked = []
visited = [0] * N

perm(0)