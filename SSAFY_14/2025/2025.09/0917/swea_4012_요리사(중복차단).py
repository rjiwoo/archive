# 4012. [모의 SW 역량테스트] 요리사

# 두 명의 손님에게 음식 제공
# 최대한 비슷한 맛의 음식 만들어야 함

# N개의 식재료가 있다.
# 식재료들을 각각 N / 2개씩 나누어 두 개의 요리를 하려고 한다. (N은 짝수이다.)

# 각각의 음식을 A음식, B음식

def comb(count, idx):
    global answer
    if count == N//2:
        A = picked
        B = [i for i in range(N) if i not in picked]

        A_score = 0
        B_score = 0

        for r in range(len(A)):
            for c in range(r + 1, len(A)):
                A_score += arr[A[r]][A[c]] + arr[A[r]][A[c]]

        for r in range(len(B)):
            for c in range(r + 1, len(B)):
                A_score += arr[B[r]][B[c]] + arr[B[r]][B[c]]

        answer = min(answer, abs(A_score-B_score))
        return 

    for i in range(idx, N):
        if count == 0 and i != 0:
            continue  # 0번 재료를 고정해 중복 조합 차단
        picked.append(food_number[i])
        comb(count + 1, i + 1)
        picked.pop()


T = int(input())

for tc in range(1, T+1):

    N = int(input()) 
    arr = [list(map(int, input().split())) for _ in range(N)]

    food_number = [i for i in range(N)]
    answer = float('inf')
    picked = []
    comb(0,0)

    print(f'#{tc} {answer}')