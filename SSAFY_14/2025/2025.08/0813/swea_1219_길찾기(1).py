# swea 1219번 길찾기

# 첫번째 제출

T = 10

for tc in range(1, T+1):

    # t = 테스트 케이스 번호,  road = 길의 총 개수
    t, road_len = map(int, input().split())
    pair = list(map(int, input().split()))

    a_node = [0]*100
    b_node = [0]*100

    for i in range(0,len(pair),2):
        if a_node[pair[i]] == 0:
            a_node[pair[i]] = pair[i+1]
        else: 
            b_node[pair[i]] = pair[i+1]

    # print(a_node)
    # print(b_node)


    # 스택을 이용하려면, 처음에 스택에 시작 부분 넣고, 방문을 체크할 리스트 만들기.
    # 시작 노드(0)을 스택에 추가?
    stack = [0]
    visited = [False]*100
    answer = 0

    # 스택이 빌 때까지
    while stack:
        # print('whlie시작')
        # print(stack)
        current_node = stack.pop()
        # print(current_node)
        # print(f'현재 노드를 뺀 stack {stack}')

        # 99번을 만나면 도착
        if current_node == 99:
            answer = 1
            break
        
        # 방문하지 않았던 노드면, 방문했다고 표시
        if visited[current_node] == False:
            visited[current_node] = True
            
            # a_node에 경로가 있으면
            if a_node[current_node] != 0:
                stack.append(a_node[current_node])
                # print('a_node 추가')
                # print(stack)


            # b_node에 경로가 있으면
            if b_node[current_node] != 0:
                stack.append(b_node[current_node])
                # print('b_node 추가')
                # print(stack)

    print(f'#{tc} {answer}')
