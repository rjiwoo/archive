# 문제1) 합성곱 (배점:40점)

# 합성곱이란 N*N 크기 입력에 M*M 크기의 필터를 슬라이딩하며 
# 각 위치에서 요소별 곱을 합산해 새로운 출력

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]   # 입력데이터 N*N
    fil = [list(map(int, input().split())) for _ in range(M)]   # 필터 입력 M*M

    # 합성곱 연산의 결과 크기만큼 2차원 배열 미리 만들어두기(초기화)
    result = [[0]*(N-M+1) for _ in range(N-M+1)]
    # print(result)

    # N*N에서 필터의 크기만큼 잘라서 필터와 합성곱 연산 할 것
    for r in range(N-M+1):
        for c in range(N-M+1):
            temp = 0
            for i in range(M):
                for j in range(M):
                    temp += arr[r+i][c+j] * fil[i][j]
            result[r][c] = temp

    # print(result)

    print(f'#{tc}')
    for row in result:
        print(*row)