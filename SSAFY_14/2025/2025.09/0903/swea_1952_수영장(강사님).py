# swea 1952번 수영장 (강사님 코드)
def dfs(idx, fee): # 
    global answer

    if answer <= fee:
        return

    if idx >= 12:
        answer = min(answer, fee)
        return

    # ㄱ. 일권을 사는 경우
    dfs(idx+1, fee + day*plans[idx])

    # ㄴ. 월권을 사는 경우
    if month < quarter:
        dfs(idx+1, fee + month)

    # ㄷ. 3개월권을 사는 경우
    dfs(idx+3, fee + quarter)




T = int(input())
for tc in range(1, T+1):
    day, month, quarter, year = map(int, input().split())
    plans = list(map(int,input().split()))

    # 최대비용은 연간회원권을 넘지 않음
    answer = year

    # ㄱ. 내가 몇 월의 의사결정을 하고 있는지
    # ㄴ. 해당 월 전까지의 누적 비용
    # 주의 : 월은 -1 처리해야 함

    dfs(0,0)

    print(f'#{tc} {answer}')