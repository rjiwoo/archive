# 재귀없이 단순 반복문

# 특징
# 꼭짓점부터 우하로 2칸, 좌하로 3칸 가기로 했다면 나머지는 길이가 동일함
# 이 모양(직사각형)이 다 있다는 걸 검증하는 방법?


# 강사님은 가서 먹는 것이기 때문에 마지막에 체크할 필요가 없어?


# 우하향, 좌하향, 좌상향, 우상향 
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

T = int(input())

# 디저트를 먹었는지 방문체크
def dessert_run(r, c, turn1, turn2):
    dessert_set = set()

    # 0번 방향 수, 1번 방향 수, 2번 방향 수, 3번 방향 수
    counts = [turn1, turn2, turn1, turn2]

    for dir in range(4):
        for i in range(counts[dir]):
            r += dr[dir]
            c += dc[dir]

            if arr[r][c] in dessert_set:
                return -1 # 케이스를 찾은게 아니기 때문에
            dessert_set.add(arr[r][c])
    return len(dessert_set)

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = -1
    
    # 1. 시작점 정해주기
    for s_r in range(N-2):
        for s_c in range(1, N-1):

            # 2. turn1(우하), turn2(좌하)
            for turn1 in range(1,N-s_c):
                for turn2 in range(1,N-s_r-turn1):

                    if s_c-turn2 >= 0 and (turn1+turn2)*2 > answer:
                        answer = max(answer, dessert_run(s_r, s_c, turn1, turn2))
    
    print(f'#{tc} {answer}')