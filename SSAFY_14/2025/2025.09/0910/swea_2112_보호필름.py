# SWEA 2112. [모의 SW 역량테스트] 보호 필름

T = int(input())

for tc in range(1, T+1):

    # 두께 D, 가로크기 W, 합격기준 K
    D, W, K = map(int, input().split())
    
    # 특성A는 0, 특성B는 1
    graph = [list(map(int, input().split())) for _ in range(D)]

    # 성능 검사 -> 세로 검사: 각 세로중에 합격기준만큼 연속으로 같으면 성능 통과
    # 통과 안되면 약품 처리기?
    # 연속이 안된 곳이 있어서 통과 안된거니까 그 부분을 체크하고 
    # 그 중에서 한줄씩 바꿔가면서 다시 확인해봐

    # 근데 이때 변경되면서 기존에 통과한 것도 변경된다면? 다시 검사해

    # 세로검사
    for c in range(W):
        count = 1 
        success = False
        for r in range(1,D):
            if graph[r][c] == graph[r-1][c]:
                count += 1
                if count >= K:
                    success = True 
                    break
            else:
                count = 1

        if not success:

