from collections import deque
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split())) # 녹아야하는 치즈의 양

    # 피자 번호, 치즈양
    pizza = deque()
    for i in range(M):
        pizza.append([i+1, cheese[i]]) 

    # 화덕. 화덕에 피자를 넣을 수 있을만큼 넣음
    oven = deque()
    for _ in range(N):
        oven.append(pizza.popleft())
    
    # 오븐에 피자가 하나 남을 때까지 
    while len(oven) > 1:

        # 오븐에서 피자번호, 치즈양 확인
        pizza_num, cheese = oven.popleft()

        # 치즈의 양을 반으로 줄이기
        cheese =  cheese//2

        # 치즈 양이 0이 아니면 다시 넣기
        if cheese != 0 :
            oven.append([pizza_num, cheese])
        else: # 치즈양이 0보다 작아지면
            # 피자가 남아있다면
            if pizza: 
                oven.append(pizza.popleft()) # 오븐에 남은 피자 넣기
    

    print(f'#{tc} {oven[0][0]}')