# 백준 2001번 파리퇴치
# N*N 배열 : 안의 숫자는 파리의 개수
# M*M 크기의 파리채
# 한 번 내리쳐 최대한 많은 파리 죽임

T = int(input()) #테스트 케이스

for tc in range(1, T+1):
    N, M = map(int, input().split()) 

    # N*N 안의 숫자 받기(2차원 배열 받기)
    arr = [list(map(int, input().split())) for _ in range(N)]

    # for row in arr:
    #     print(*row)
    max_value = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            
            temp = 0
            for i in range(M):
                for j in range(M):
                    temp += arr[r+i][c+j]

            if max_value < temp:
                max_value = temp
    print(f'#{tc} {max_value}')