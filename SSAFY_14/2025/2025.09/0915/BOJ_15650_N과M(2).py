#  15650번 N과 M (2)

# 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순

# -> 조합?

def comb(count, idx):
    if count == M:
        print(*picked, )
        return

    for i in range(idx, N):
        picked.append(arr[i])
        comb(count + 1, i + 1)
        picked.pop()



N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

picked = []
comb(0,0)