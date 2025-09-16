# 선택정렬
# 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치 교환하는 방식

# 주어진 리스트에서 최소값 찾기
# 그 값을 맨 앞에 위치한 값과 교환
# 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정 반복

# 시간복잡도 O(n**2)

def selection_sort(arr, N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def selection_sort2(arr,N):
    for i in range(N-1):
        min_idx = i # 첫번째 원소를 최소로 가정
        for j in range(i+1,N):   
            if arr[min_idx] > arr[j]:
                min_idx = j 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]   