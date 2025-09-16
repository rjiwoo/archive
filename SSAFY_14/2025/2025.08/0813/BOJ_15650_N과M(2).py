# 백준 15650번. N과 M(2) 

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.


def comb(start):
    if len(picked_nums) == M:
        print(*picked_nums)
        return
    
    for i in range(start, N+1):
        picked_nums.append(i)
        comb(i+1)
        picked_nums.pop()

N, M = map(int, input().split())

picked_nums = []

comb(1)