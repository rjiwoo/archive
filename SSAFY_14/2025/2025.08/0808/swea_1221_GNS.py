# swea 1221번 GNS

T = int(input())

for _ in range(T):
    tc, N = input().split()
    arr = input().split()

    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]


    # 해당 숫자의 개수를 세서 저장하자.
    # dict 사용?

    num_count = {}
    # 제발 초기값 설정 잊지마..............
    for char in num:
        num_count[char] = 0
    for char in arr:
        num_count[char] += 1

    # print(num_count)

    answer = []
    for char in num:
        answer += [char] * num_count[char]

    # print(answer)
    answer = ' '.join(answer)

    print(tc)
    print(answer)
