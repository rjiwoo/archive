# SWEA 1232. [S/W 문제해결 기본] 9일차 - 사칙연산

T = 10

def postorder(node):
    if len(tree[node]) == 4: # 자식노드가 둘 다 있는 경우
        left = postorder(tree[node][2])
        right = postorder(tree[node][3])
        if tree[node][1] == '+':
            return left + right
        elif tree[node][1] == '-':
            return left - right
        elif tree[node][1] == '*':
            return left * right
        elif tree[node][1] == '/':
            return left / right
    elif len(tree[node]) == 3: # 왼쪽 자식노드만 있는 경우
        return postorder(tree[node][2])
    else: # 자식노드가 없는 경우(리프노드)
        return int(tree[node][1])


for tc in range(1, T + 1):
    N = int(input())
    tree = {}
    for _ in range(N):
        node = list(input().split()) # 노드번호, 값, 왼쪽자식노드번호, 오른쪽자식노드번호
        tree[node[0]] = node # 딕셔너리에 노드번호를 key로, 나머지를 value로 저장

    ans = postorder('1')
    print(f'#{tc} {int(ans)}')

