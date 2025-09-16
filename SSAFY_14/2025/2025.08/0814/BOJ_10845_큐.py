# 백준 10845번 큐

# 정수를 저장하는 큐를 구현
# 명령을 처리하는 프로그램 작성

# 명령의 수 N
# N개의 줄에는 명령이 하나씩 주어짐

import sys

def queue():
    
    command = list(sys.stdin.readline().split())

    if command[0] == 'push':
        q.append(int(command[1]))
    elif command[0] == 'pop':
        if q != []:
            print(q.pop(0))
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if q != []:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if q != []:
            print(q[0])
        else: 
            print(-1)
    elif command[0] == 'back':
        if q != []:
            print(q[-1])
        else: 
            print(-1)
    

N = int(sys.stdin.readline())

q = []

for _ in range(N):
    queue()            