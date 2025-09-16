# 강사님 코드

T = 10

def inorder(node):
    if node*2 <= N:
        inorder(node*2)
    print(chars[tree[node]], end='')

    if node*2+1 <= N:
        inorder(node*2+1)

for tc in range(1, T+1):
    N = int(input()) # 노드의 수
    tree = [0] * (N+1)
    chars = [''] * (N+1)

    tree[1] = 1
    for i in range(N):
        info = input().split()

        if len(info) == 4:
            index, char, left, right =  info
            # 2. 왼쪽 자식노드 번호 등록해놓기
            tree[int(index)*2] = left
            # 3. 오른쪽 자식노드 번호 등록해놓기
            tree[int(index)*2+1] = right

        elif len(info) == 3:
            index, char, left =  info
            # 2. 왼쪽 자식노드 번호 등록해놓기
            tree[int(index)*2] = left
        
        else: 
            index, char =  info

        # 1. 자기 인덱스에 글씨 적어넣기
        chars[int(index)] = char

    print(f'#{tc} ', end='')
    inorder(1)
    print()