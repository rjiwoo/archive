# swea 4861번 회문

# 문자열 거꾸로 뒤집기
def reverse(temp):
    a = []
    for i in range(len(temp)-1, -1, -1):
        a.append(temp[i])
    return a

# 회문 확인
def search_same():

    # 가로
    for r in range(N):
        r_temp = 0
        for c in range(N-M+1):
            r_temp = arr[r][c:c+M]

            if r_temp == reverse(r_temp):
                return r_temp
    
    # 세로
    for r in range(N):
        for c in range(N-M+1):
            c_temp = []
            for k in range(M):
                c_temp.append(arr[c+k][r]) 
                
            if c_temp == reverse(c_temp):
                return c_temp

    return ''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range (N)]

    answer = search_same()

    print(f"#{tc} {''.join(answer)} ")