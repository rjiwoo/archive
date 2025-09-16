# N*M 배열의 크기와 저장된 값이 주어졌을 때 합을 구하는 방법

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# s = 0
# for r in range(N):
#     for c in range(M):
#         s += arr[r][c]

# # 열 우선 순회

# for r in range(N):
#     for c in range(M):
#         print(arr[c][r])

# for c in range(M):
#     for r in range(N):
#         print(arr[c][r])


# 지그재그 순회

arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
]

for r in range(len(arr)):
    if r%2 == 0:
        for c in range(len(arr[r])):
            print(arr[r][c], end=' ')
    else: 
        for c in range(len(arr[r])-1,-1,-1):
            print(arr[r][c], end= ' ')
    print()


arr[1].reverse()
print(arr)






################################################
# 2차원 배열 연습
################################################

# arr = [1,2,3,4,5,6,7,8,9]

# for i in range(len(arr),0,-1):
#     print(i, end = ' ')



# print()
# arr = [[1,2,3],
#        [4,5,6],
#        [7,8,9],
# ]

# for r in range(2,-1,-1):
#     for c in range(2,-1,-1):
#         print(arr[r][c], end=' ')


# arr = [[1,2,3],
#        [4,5,6],
#        [7,8,9],
# ]
# for i in reversed(arr):
#     for j in reversed(i):
#         print(j, end=' ')


# a = [1,2,3]
# a.reverse()
# print(a)

# for i in arr[::-1]:
#     for j in i[::-1]:
#         print(j)


# for i in range(N):
#     s += arr[i][i]