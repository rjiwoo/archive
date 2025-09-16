# def put():
#     for j in range(N):
#         for i in range(N):
#             print('■' if pos[i] == j else '□', end=' ')
#         print()
#     print()

def set(i):
    global count
    for j in range(N):
        if (not flag_a[j]
            and not flag_b[i + j]
            and not flag_c[i - j + (N - 1)]):
            pos[i] = j
            if i == (N - 1):
                # put()
                count += 1
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (N - 1)] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (N - 1)] = False


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    pos = [0] * N
    flag_a = [False] * N
    flag_b = [False] * (2 * N - 1)
    flag_c = [False] * (2 * N - 1)
    count = 0

    set(0)
    print(f'#{tc} {count}')



#####################################################
T = int(input())

def n_queen(row): # 이 row번째를 고르고 있어
    global answer

    if row == N : # 탈출조건. N개의 퀸을 다 골랐을 때 
        answer += 1
        return
    
    for col in range(N):
        # 세로 검사 통과 & 좌하향 통과 & 우하향 통과 => 모두 미방문 상태일때만
        if (not col_visited[col] and 
            not main_diag_visited[row-col+N-1] and 
            not sub_diag_visited[row+col]):    
            col_visited[col] = 1
            main_diag_visited[row-col+N-1] = 1
            sub_diag_visited[row+col] = 1

            n_queen(row+1)

            # 원상복구 -> 다음 열을 골랐을 경우를 봐야하기 때문에 방문했던 것을 다시 되돌리기
            col_visited[col] = 0
            main_diag_visited[row-col+N-1] = 0
            sub_diag_visited[row+col] = 0

for tc in range(1, T+1):
    N = int(input())

    col_visited = [0] * N
    main_diag_visited = [0] * (2*N-1) # 좌하향 대각선 방문
    sub_diag_visited = [0] * (2*N-1) # 우하향 대각선 방문
    answer = 0

    n_queen(0) # 지금까지 놓았던 퀸의 수를 인자로

    print(f'#{tc} {answer}')
