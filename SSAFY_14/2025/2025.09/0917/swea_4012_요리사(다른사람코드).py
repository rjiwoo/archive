# SWEA 4012 요리사 

# 다른 사람코드(1) : 최적화됨
T = int(input())

def cal(team):
    total = 0
    # ex) 재료 1,2,3,4인 경우
    #     ->  raw[1][2] + raw[2][1] = 각 team 음식 맛
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            total += raw[team[i]][team[j]] + raw[team[j]][team[i]]
    return total

def food(idx, cnt):
    global check
    global answer

    if cnt == check:
        # B팀 재료들 넣어주기
        team_b = []
        for i in range(N):
            if i not in team_a:
                team_b.append(i)
        
        taste = abs(cal(team_a) - cal(team_b))
        answer = min(answer, taste)
        return

    # ex) (1, 2, 3) 과 (1, 3, 2) 는 같은 경우임
    #     So, 인덱스 체크!
    for i in range(idx, N):
        team_a.append(i)
        food(i + 1, cnt + 1)
        team_a.pop()


for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]

    check = N // 2

    answer = 99999999999
    team_a = []

    # 0번째 인덱스를 항상 포함시켜 절반만 탐색
    # 꼭 0번째일 필요는 없음(But, 편의상 맨 앞 인덱스 넣어줌)
    team_a.append(0)
    food(1, 1)

    print(f"#{tc} {answer}")


######################################################################
## 다른 사람 코드(1)-2 
# 짜파게티 요리사

T = int(input())


def food(idx, cnt):
    global check
    global answer

    if cnt == check:
        # B팀 재료들 넣어주기
        team_b = []
        for i in range(N):
            if i not in team_a:
                team_b.append(i)
        
        total_a = 0
        total_b = 0
        # team_a와 team_b 길이는 똑같아서 하나의 for문으로 처리 가능
        for i in range(len(team_a)):
            for j in range(i+1, len(team_a)):
                total_a += raw[team_a[i]][team_a[j]] + raw[team_a[j]][team_a[i]]
                total_b += raw[team_b[i]][team_b[j]] + raw[team_b[j]][team_b[i]]

        taste = abs(total_a - total_b)
        answer = min(answer, taste)

        return

    # ex) (1, 2, 3) 과 (1, 3, 2) 는 같은 경우임
    #     So, 인덱스 체크!
    for i in range(idx, N):
        team_a.append(i)
        food(i + 1, cnt + 1)
        team_a.pop()


for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]

    check = N // 2

    answer = 99999999999
    team_a = []

    # 0번째 인덱스를 항상 포함시켜 절반만 탐색
    # 꼭 0번째일 필요는 없음(But, 편의상 맨 앞에꺼 넣어주기)
    team_a.append(0)
    food(1, 1)

    print(f"#{tc} {answer}")


#############################################################################
# 다른 사람 코드(1)
def cook(idx, ingre):
    global ans

    if ingre == N//2:
        foodB = []
        # 재료 다 모으면 남은 재료 B에 주고 차 구하기
        for i in range(N):
            if i not in foodA:
                foodB.append(i)

        A, B = 0, 0
        
        for i in foodA:
            for j in foodA:
                A += Sij[i][j]

        for i in foodB:
            for j in foodB:
                B += Sij[i][j]

        ans = min(ans, abs(A - B))
        return

    # 재료 조합하기
    for i in range(N):
        if i > idx:
            foodA.append(i)
            cook(i, ingre+1)
            foodA.pop()

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    Sij = [list(map(int, input().split())) for _ in range(N)]
    foodA = []
    ans = float('inf')
    cook(0, 0)
    print(f'#{tc} {ans}')


