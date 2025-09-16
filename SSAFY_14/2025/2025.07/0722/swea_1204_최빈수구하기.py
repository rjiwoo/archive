# swea 1204번 최빈수 구하기

T = int(input()) # 테스트 케이스 개수

for test_case in range(1, T+1):
    T_number = input()  # 테스트 케이스 번호
    score = list(map(int, input().split())) 

    count_table = [0]*101 # 0~100점까지의 해당 점수가 몇 번 나왔는지 체크하기 위한 list

    # 각 점수의 횟수 count
    for num in score:
        count_table[num] += 1

    # 많이 나온 횟수
    max_count = max(count_table)

    many_score = []
    for i in range (101):
        if count_table[i]==max_count:
            many_score.append(i)

    many_score.reverse()
    print(f'#{T_number} {many_score[0]}')