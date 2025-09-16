#  15651번 N과 M (3) 

# 래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

# 사전 순으로 증가하는 순서로 출력해

 # 중복 순열

def dupli_perm(count):
    if count == M:
        print(*picked)
        return
    
    for i in range(N):
        picked.append(arr[i])
        dupli_perm(count + 1)
        picked.pop()


N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
picked = []
dupli_perm(0)