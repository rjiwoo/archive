# 백준 10828번 스택

# 정수를 저장하는 스택 구현
# 명령을 처리하는 프로그램 작성

# 명령의 수 N
# N개의 줄에는 명령이 하나씩 주어짐

# 아래 코드 시간초과 뜸

# def stack():

#     command = list(input().split())

#     if command[0] == 'push':
#         s.append(int(command[1]))
#     elif command[0] == 'pop':
#         if s != []:
#             print(s.pop())
#         else:
#             print(-1)
#     elif command[0] == 'size':
#         print(len(s))
#     elif command[0] == 'empty':
#         if s != []:
#             print(0)
#         else:
#             print(1)
#     elif command[0] == 'top':
#         if s != []:
#             print(s[-1])
#         else: 
#             print(-1)


# N = int(input())

# s = []

# for _ in range(N):
#     stack()



# 시간초과 해결 -> import sys
#             -> input() 대신 sys.stdin.readline 사용
import sys

def stack():

    command = list(sys.stdin.readline().split())


    if command[0] == 'push':
        s.append(int(command[1]))
    elif command[0] == 'pop':
        if s != []:
            print(s.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(s))
    elif command[0] == 'empty':
        if s != []:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if s != []:
            print(s[-1])
        else: 
            print(-1)


N = int(sys.stdin.readline())

s = []

for _ in range(N):
    stack()
