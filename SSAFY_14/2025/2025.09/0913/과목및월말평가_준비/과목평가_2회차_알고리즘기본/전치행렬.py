arr = [[1,2,3],
       [4,5,6],
       [7,8,9],
]

# 전치행렬
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j] 

for i in arr:
    print(*i)

print()

# i < j

arr = [[1,2,3],
       [4,5,6],
       [7,8,9],
]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i < j:
            print(arr[i][j], end=' ')
    print()
