# 11022번 A+B-8

T = int(input())

for i in range(1, T+1):
    A, B = list(map(int, input().split()))
    print(f'Case #{i}: {A} + {B} = {A+B}')