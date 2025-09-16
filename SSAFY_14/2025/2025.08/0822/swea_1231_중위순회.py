# SWEA 1231번 중위순회(필수제출)

# 주어진 트리를 in-order 형식으로 순회'

def inorder_traverse(T):
    if T > N:
        return
    inorder_traverse(T*2)
    print(word[T][1], end='')
    inorder_traverse(T*2+1)

T = 10

for tc in range(1, T+1):
    N = int(input())
    
    	
    graph = [[] for _ in range(N+1)]
    word = []
    word.insert(0, '0') 

    # 트리 입력 받기
    for i in range(N):
        word.append(list(input().split())[:2])
    
    # print(word)
    print(f'#{tc} ', end='')
    inorder_traverse(1)
    print()


####################################################
################ 트리 입력 다르게 받기 ################

# SWEA 1231번 중위순회(필수제출)

# 주어진 트리를 in-order 형식으로 순회'

# def inorder_traverse(T):
#     if T > N:
#         return
#     inorder_traverse(T*2)
#     print(word[T], end='')
#     inorder_traverse(T*2+1)

# T = 10

# for tc in range(1, T+1):
#     N = int(input())
    
    	
#     graph = [[] for _ in range(N+1)]
#     word = []
#     word.insert(0, '0') 

#     # # 트리 입력 받기
#     # for i in range(N):
#     #     temp.append(list(input().split())[:2])

#     for _ in range(N):
#         info = list(input().split())

#         if len(info) == 2:
#             word.append(info[1])

#         elif len(info) > 2:
#             for i in range(2, len(info)):
#                 graph[int(info[0])].append(int(info[i]))
#             word.append(info[1])
    
#     # print(word)
#     print(f'#{tc} ', end='')
#     inorder_traverse(1)
#     print()