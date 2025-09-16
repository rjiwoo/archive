# 백준) 7단계. 2차원 배열 - 2566번. 최댓값

# 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 
# 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램

# 에러 1. 변수를 초기화 안해서?
# 에러 2. 크거나 같다고 안해서? 크다고만 하면 뭐가 문제가 되는건가???
# 최댓값이 두 개 이상인 경우, 그 중 한 곳의 위치를 출력하면 된다는데 마지막에 나오는걸로 바꿔야해?
# -> 모든 수가 0이면, r,c의 위치가 업데이트 될 수 없어서 위치가 0 0 이 되버림. 
# 문제 출력 조건 잘 보자......................


# 2차원 배열 입력 받기
N = [list(map(int, input().split())) for _ in range(9)]

# print(N)

max_num = N[0][0]
max_num_r = 1
max_num_c = 1
for r in range(9):
    for c in range(9):
        if max_num < N[r][c]:
            max_num = N[r][c]
            max_num_r = r+1
            max_num_c = c+1

print(max_num)
print(max_num_r, max_num_c)


# 초기값 설정 때문에 오류.
# 2차원 배열 입력 받기
N = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
max_num_r = 0
max_num_c = 0
for r in range(9):
    for c in range(9):
        if max_num <= N[r][c]: # 처음 시도 시, max_num < N[r][c] 으로 작성.
            max_num = N[r][c]
            max_num_r = r+1     # if가 한 번도 실행 안되면 위치가 0 0 으로 되서 오류
            max_num_c = c+1

print(max_num)
print(max_num_r, max_num_c)