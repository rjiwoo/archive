# 백준 2447번 별 찍기 - 10

# 재귀적인 패턴으로 별 찍기
# n이 3의 거듭제곱일 때, n x n 크기의 패턴을 만듭니다.
# 패턴은 3x3 블록으로 나누어지며, 가운데 블록은 공백으로 채워집니다.

# ***
# * *
# ***

# N이 3보다 클 경우, 
# 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태

from pprint import pprint
def print_star(n, row, col):
    if n == 1:
        graph[row][col] = '*'
        return
    cnt = n // 3
    for i in range(3):
        for j in range(3):
            if not (i==1 and j==1):
                print_star(cnt, row+i*cnt, col+j*cnt)

N = int(input())
graph = [[' ']*N for _ in range(N)]

print_star(N, 0, 0)

for row in graph:
    print(''.join(row))