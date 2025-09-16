# swea 4839. 이진탐색


def binary_serach(page, target_page):
    start = 1
    
    end = page
    count = 0 # 몇번째 탐색에 찾았는지

    while start <= end:
        count += 1
        mid = (start + end) // 2

        if target_page == mid:
            return count
        
        elif target_page < mid:
            end = mid -1

        else:
            start = mid +1
    

T = int(input())

for tc in range(1, T+1):
    page, Pa, Pb = map(int, input().split())

    a_count = binary_serach(page,Pa)
    b_count = binary_serach(page,Pb)

    print(a_count)
    print(b_count)

    answer = 0
    if a_count < b_count:
        answer = 'A'
    elif a_count > b_count:
        answer = 'B'
    else:
        answer = 0



    print(f'#{tc} {answer}')

