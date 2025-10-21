# swea 2001. 파리 퇴치

# 3회차 월말평가 대비

# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수
# M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = 0 # 정답

    for r in range(N-M+1):
        for c in range(N-M+1):
            temp = 0
            for i in range(M):
                for j in range(M):
                    temp += graph[i][j]
            if answer < temp:
                answer = temp

    print(f'#{tc} {answer}')