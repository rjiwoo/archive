# 카운팅 정렬 : 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇개씩 있는지 세는 작업. 
# 선형시간에 정렬하는 효율적 방식
# 시간복잡도 : O(N+K)
# N = 리스트의 길이, K =정수의 최댓값

# 정수 혹은 정수로 표현될 수 있는 자료만 가능
# 카운트를 위한 충분한 공간 할당이 필요하기 때문에 집합 내의 가장 큰 정수의 값을 알아야 함. 

def counting_sort(data, temp, k):
    count = [0]*(k+1)

    for i in range(len(data)):
        count[data[i]] += 1
    
    for i in range(1, k+1):
        count[i] += count[i-1]
    
    for i in range(len(data)-1, -1, -1):
        count[data[i]] -= 1
        temp[count[data[i]]] = data[i]
