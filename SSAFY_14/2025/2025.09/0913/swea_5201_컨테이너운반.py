# SWEA 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

# 화물이 실려 있는 N개의 컨터이너를 M대의 트럭으로 A도시에서 B도시로 옮겨
# 트럭 당 한개의 컨테이너를 운반할 수 있음. 
# 트럭의 적재용량을 초과하는 컨테이너를 운반할 수 없음

# 컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고, A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행
# 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지

# 컨터이너를 한 개도 옮길 수 없을 경우는 0 출력

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_weight = list(map(int, input().split()))
    M_weight = list(map(int, input().split()))

    answer = 0 # 한 개도 못 옮길 경우가 최소


    # 무거운 순서로 정렬. 
    N_weight.sort(reverse=True) 
    M_weight.sort(reverse=True)

    # print(N_weight)
    # print(M_weight)

    # 해당 트럭에 컨테이너를 적재하면, 컨테이너 무게 저장
    M_plus = [0]*M

    for i in range(M):
        for j in range(len(N_weight)):
            if M_weight[i] >= N_weight[j]:
                M_plus[i] = N_weight[j]
                N_weight.pop(j)
                break
                
    # print(M_plus)
    # print(N_weight)
    # print(sum(M_plus))
    answer = max(answer, sum(M_plus))                

    print(f'#{tc} {answer}')