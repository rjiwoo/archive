# swea 1206번 View

for tc in range(10): # 10개의 테스트 
    N = int(input()) # 건물의 개수 N개 
    building = list(map(int, input().split())) # 건물 높이
    
    answer = 0
    
    # 인덱스 2부터 N-3까지 반복 (왼쪽 오른쪽 2개씩 건물 못지음)
    for i in range(2, N - 2): 
        # 현재 건물 building[i]가 양옆의 건물(총 4개)보다 높은지 확인
        if (building[i] > building[i-1] and 
            building[i] > building[i-2] and 
            building[i] > building[i+1] and 
            building[i] > building[i+2]): 
            
            # 네 건물 중 가장 높은 높이
            max_neighbor_height = max(building[i-1], building[i-2], building[i+1], building[i+2])
            
            # 현재 건물의 높이에서 주변 가장 높은 건물의 높이를 뺀 값
            answer += (building[i] - max_neighbor_height)
            
    
    print(f'#{tc+1} {answer}')