# 백준 15649번 N과 M (1)

# 자연수 N과 M이 주어졌을 때, 
# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

# 해당 숫자를 넣고 다시 넣고 해야하니까 재귀함수?
def solve():
    # 수열의 길이가 M과 같아지면 종료
    if len(arr) == M:
        print(*arr)
        return
    
    # 1부터 N까지 숫자 하나씩 확인
    for i in range(1, N+1):
        if i not in arr: # 현재 숫자가 포함되어 있지 않으면
            arr.append(i) # 숫자 추가
            solve() # 다음 숫자 찾기
            arr.pop() # 마지막에 추가한 숫자 삭제


N, M = map(int, input().split())
arr = [] # 현재까지 만든 수열 저장

solve()
