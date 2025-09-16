# swea 10580번 전봇대

# N개의 팽팽한 전선으로 연결되어 있음
# 두 전선이 끝점이 같은 경우는 없으나, 교차하는 경우는 있음

# 1. 새로운 선의 시작점이 기존선의 시작점보다 높고, 새로운 선의 도착점이 기존 선의 도착점보다 낮은 경우
# 2. 새로운 선의 시작점이 기존 선의 시작점보다 낮으며 새로운 선의 도착점이 기존 선의 도착점보다 높은 경우


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    wires = [tuple(map(int, input().split())) for _ in range(N)]

    ans = 0
    # 모든 전선 쌍을 비교
    for i in range(N):
        for j in range(i+1, N):
            a1, b1 = wires[i]
            a2, b2 = wires[j]
            if (a1 < a2 and b1 > b2) or (a1 > a2 and b1 < b2):
                ans += 1

    print(f"#{tc} {ans}")