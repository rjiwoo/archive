# SWEA 1208번 Flatten

# 10개의 테스트 케이스 주어짐
for tc in range(1,11):
    dump = int(input()) # 덤프횟수
    data = list(map(int, input().split())) # 상자 높이 

    for _ in range(dump): # 덤프 횟수만큼 반복

        # 데이터에서 최고, 최저 찾기
        max_height = max(data)
        min_height = min(data)

        # 최고, 최저 값의 인덱스 번호 찾기
        max_index = data.index(max_height)
        min_index = data.index(min_height)

        # 최고에서 -1, 최저에서 +1 에서 평탄화
        data[max_index] -= 1
        data[min_index] += 1

    # 평탄화 작업이 끝난 후, 최고최저 찾기
    final_max = max(data)
    final_min = min(data)

    print(f'#{tc} {final_max - final_min}')