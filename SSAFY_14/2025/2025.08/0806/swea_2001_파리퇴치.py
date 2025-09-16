# SWEA 2001 파리퇴치

# N*N 배열 안의 숫자는 해당 영역에 존재한느 파리의 개수
# M*M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리 죽이기

# N*N 배열에서 M*M의 영역의 합이 최대를 구해라.
# 각 첫 줄 테스트 케이스 T
# 그 다음에 N, M 주어짐
# N*N 배열 입력값 주어짐

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for r in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                for h in range(M):
                    temp += arr[r+k][j+h]  

            if max_value < temp:
                max_value = temp
                
    print(f'#{tc} {max_value}')





    # for r in range(0, N, M):
    #     for c in range(0, N, M):
    #         temp += arr[r][c]
    #     total.append(temp)

    # answer = max(total)

    # print(f'#{tc} {answer}')
