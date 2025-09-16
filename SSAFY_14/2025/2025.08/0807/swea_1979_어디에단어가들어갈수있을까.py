# swea_1979_어디에 단어가 들어갈 수 있을까

# N*N 크기의 단어 퍼즐
# 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램

# 흰색 1, 검정 0. 흰색에 들어가야함. 흰색 확인

# T = int(input())

# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     r_count = 0 # 들어갈 수 있는 자리 수 
#     c_count = 0

#     # 가로 확인(행 확인)
#     r_line_sum = []
#     for r in range(N):
#         r_sum = 0
#         for c in range(N):
#             r_sum += arr[r][c]   
#         r_line_sum.append(r_sum)
#     print(r_line_sum)

#     for i in range(N):
#         if r_line_sum[i] >= K: # 각 행의 합이 K보다 크거나 같으면
#             # 해당 행에서 숫자가 연속적으로 붙어있는지 확인
#             for c in range(N-K+1):
#                 if sum(arr[i][c:c+K]) == K:
#                     r_count += 1
#     print(r_count)


#     # 세로 확인(열 확인)
#     c_line_sum = []
#     for r in range(N):
#         c_sum = 0
#         for c in range(N):
#             c_sum += arr[c][r]
#         c_line_sum.append(c_sum)

#     # print(c_line_sum)

#     for i in range(N):
#         if c_line_sum[i] >= K:
#             for r in range(N-K+1):
#             # i열의 r부터 r+K-1 행까지의 합
#                 column_sum = 0
#                 for row_index in range(r, r + K):
#                     column_sum += arr[row_index][i]

#                 # 합이 K이면, K개의 1이 연속
#                 if column_sum == K:
#                     c_count += 1         
#     print(c_count)      

#     count = r_count + c_count


#     print(f'#{tc} {count}')


# # 수정된 로직 (예시)
# count = 0
# for i in range(N): # 열(column)
#     for r in range(N - K + 1): # 시작 행(row)
#         # i열의 r부터 r+K-1 행까지의 합을 구합니다.
#         column_sum = 0
#         for row_index in range(r, r + K):
#             column_sum += arr[row_index][i]

#         # 합이 K이면, K개의 1이 연속으로 있다는 뜻입니다.
#         if column_sum == K:
#             count += 1





# swea_1979_어디에 단어가 들어갈 수 있을까

# N*N 크기의 단어 퍼즐
# 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램

# 흰색 1, 검정 0. 흰색에 들어가야함. 흰색 확인

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0 # 들어갈 수 있는 자리 수 

    # 가로 확인(행 확인)
    for r in range(N):
        r_sum = 0
        for c in range(N):
            # 1이면 더해
            if arr[r][c] == 1:
                r_sum += 1
            # 0을 만나거나 열이 끝에 도달하면
            if arr[r][c] == 0 or c == N-1:
                if r_sum == K: #sum이 K면
                    count += 1
                r_sum = 0


    # 세로 확인(열 확인)
    for r in range(N):
        c_sum = 0
        for c in range(N):
            # 1이면 더해
            if arr[c][r] == 1:
                c_sum += 1
            # 0을 만나거나 행이 끝에 도달하면
            if arr[c][r] == 0 or c == N-1:
                if c_sum == K:
                    count += 1
                c_sum = 0
    


    print(f'#{tc} {count}')