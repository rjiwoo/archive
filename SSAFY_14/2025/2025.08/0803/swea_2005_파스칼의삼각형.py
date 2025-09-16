# 2005. 파스칼의 삼각형
# 1. 첫 번째 줄은 항상 숫자 1이다.
# 2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
# 파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 삼각형의 크기

    # 빈 리스트 만들기. (2차원 빈리스트 만드는거 계속 기억 못함. 숙지하기)
    shape = [[0]*(i+1) for i in range(N)]
    for i in range(N):
        for j in range(i+1):
            if j==0 or j==i:    # 열의 맨 앞과 맨 뒤는 숫자 1
                shape[i][j] = 1

            else:
                shape[i][j] = shape[i-1][j-1] + shape[i-1][j]    

    print(f'#{tc}')

    for row in shape:
        print(*row)