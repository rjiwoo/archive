# 백준 10866 덱

# from collections import deque
# 내장함수 deque 써보기
import sys

def dequeue():
    N = int(sys.stdin.readline())
    dq = []
    for _ in range(N):

        command = list(sys.stdin.readline().split())

        if command[0] == 'push_front':
            dq.insert(0,int(command[1]))
        elif command[0] == 'push_back':
            dq.append(int(command[1]))
        elif command[0] == 'pop_front':
            if dq != []:
                print(dq.pop(0))
            else:
                print(-1)
        elif command[0] == 'pop_back':
            if dq != []:
                print(dq.pop())
            else:
                print(-1)
        elif command[0] == 'size':
            print(len(dq))
        elif command[0] == 'empty':
            if dq != []:
                print(0)
            else:
                print(1)
        elif command[0] == 'front':
            if dq != []:
                print(dq[0])
            else: 
                print(-1)
        elif command[0] == 'back':
            if dq != []:
                print(dq[-1])
            else: 
                print(-1)

dequeue()
