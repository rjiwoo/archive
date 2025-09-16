# 움직이지 않음, 상, 우, 하, 좌
# dr = [0, -1, 0, 1, 0]
# dc = [0, 0, 1, 0, -1]

# 행열이 바뀌어있으니까 
# 제상우하좌
dr = [0, 0, 1, 0, -1]
dc = [0, -1, 0, 1, 0]
 
T = int(input())
 
for tc in range(1, T+1):
    N, BC_count = map(int, input().split())
 
    A_path = list(map(int, input().split()))
    B_path = list(map(int, input().split()))
    A_path.insert(0, 0)
    B_path.insert(0, 0)
 
    A = [1, 1]
    B = [10, 10]
    answer = 0
 
    # 각 충전기 정보
    BC_info = [0]*BC_count
    for i in range(BC_count):
        BC_info[i] = tuple(map(int, input().split()))
     
    # 순차적으로 이동하며 충전하기
    for step in range(N+1):
         
        # 1. A와 B를 이동하기
        a_dir, b_dir = A_path[step], B_path[step]
        A[0] += dr[a_dir]
        A[1] += dc[a_dir]
        B[0] += dr[b_dir]
        B[1] += dc[b_dir]
 
        # 2. A, B 각각이 충전 가능한 충전소를 파악하기
        #    > 충전 가능한 충전소의 인덱스를 저장하겠다
        A_BCs = []
        B_BCs = []
        for i in range(len(BC_info)):
            BC_r, BC_c, distance, charge = BC_info[i]
 
            if abs(A[0]-BC_r) + abs(A[1]-BC_c) <= distance:
                A_BCs.append((i, charge))
            if abs(B[0]-BC_r) + abs(B[1]-BC_c) <= distance:
                B_BCs.append((i, charge))
        A_BCs.sort(key=lambda x:x[1], reverse=True)
        B_BCs.sort(key=lambda x:x[1], reverse=True)
 
        # 3. 최대 충전량이 확보 가능한 충전기를 고르기
        #    ㄱ. 충전기가 겹치지 않는 경우
        set_BCs = set(A_BCs).union(B_BCs)
        if len(set_BCs) == len(A_BCs) + len(B_BCs):
            if A_BCs:
                answer += A_BCs[0][1]
            if B_BCs:
                answer += B_BCs[0][1]
        #    ㄴ. 충전기가 겹치는 경우
        else:
            answer += A_BCs[0][1]
 
            # 최고 충전기가 겹치는 경우
            if A_BCs[0][0] == B_BCs[0][0]:
                # A가 양보해야만 하는 경우
                if len(A_BCs) > 1 and len(B_BCs) == 1:
                    answer += A_BCs[1][1]
                # B가 양보해야만 하는 경우
                elif len(A_BCs) == 1 and len(B_BCs) > 1:
                    answer += B_BCs[1][1]
                # A와 B 중 양보할 녀석을 비교해야 하는 경우
                elif len(A_BCs) > 1 and len(B_BCs) > 1:
                    answer += max(A_BCs[1][1], B_BCs[1][1])
            # 최고 충전기가 겹치지 않는 경우
            else:
                answer += B_BCs[0][1]
 
    print(f'#{tc} {answer}')