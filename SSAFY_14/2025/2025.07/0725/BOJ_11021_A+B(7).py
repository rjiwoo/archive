# 11021번. A+B-7

# 두 정수 A와 B를 입력받은 다음, A+B를 출력

T = int(input())

for i in range(1, T+1):
    A, B = list(map(int, input().split()))
    print(f'Case #{i}: {A+B}')