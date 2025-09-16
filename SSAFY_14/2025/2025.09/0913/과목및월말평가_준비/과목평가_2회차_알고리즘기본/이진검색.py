# binary_search 
# 자료의가운데 있는 항목의 키 값과 비교와하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
# 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 함.

# arr 배열, N 배열의 길이, key 찾는 값
def binary_search(arr, N, key):
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            end = mid-1
        else: 
            start = mid+1
    return -1

def binary_search(arr, start, end, key):
    if start > end:
        return False

    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key:
            return True
        elif key < arr[mid]:
            return binary_search(arr, start, mid-1, key)
        else:
            return binary_search(arr, mid+1, end, key)