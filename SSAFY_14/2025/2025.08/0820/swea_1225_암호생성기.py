# 덱 사용
from collections import deque

T = 10

for tc in range(1, T+1):
    input()
    q = deque(map(int, input().split()))
    
    while (1):

        for j in range(1,6):
            a = q.popleft()
            if a - j <=0:
                q.append(0)
                break
            q.append(a-j)
        
        if q[-1] == 0:
            break

    print(f'#{tc} ', *q)


# 덱 사용X
T = 10

for tc in range(1, T+1):
    input()
    q = list(map(int, input().split()))

    while (1):

        for j in range(1,6):
            a = q.pop(0)
            if a - j <=0:
                q.append(0)
                break
            q.append(a-j)
        
        if q[-1] == 0:
            break

    print(f'#{tc} ', *q)