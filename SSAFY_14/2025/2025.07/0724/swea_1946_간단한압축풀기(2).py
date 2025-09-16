# swea 1946번 간단한 압축 풀기

# 두번째 풀이 

T = int(input())

for tc in range(1, T+1):
    n = int(input()) # 줄 번호
    count = 0

    print(f'#{tc}')
    for _ in range(n):
        alpha, num = input().split()
        num = int(num)

        for _ in range(num):
            print(alpha, end='')
            count += 1

            if count == 10:
                print()
                count = 0
    if count != 0:
        print()