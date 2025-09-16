# 백준) 6단계. 심화 1 - 25206번. 너의 평점은

# 전공 평점 3.3 이상이어야 졸업가능
# 전공 평점 = 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값
# 등급 p 는 계산에서 제외
# 20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.


# 딕셔너리가 어려워서 조건문으로 풀어봄
# 반복적으로 런타임 에러, 틀렸습니다 => 오타.............ㅎ 그런데 왜 vs코드는 돌아갔냐;;

# 전공과목별 (학점 × 과목평점)의 합
subject_score = 0.0
# 학점의 총합
total = 0.0

for _ in range(20):
    subject = input().split()

    # 과목 학점
    subject[1] = float(subject[1])

    # 과목 평점
    grade = subject[2]

    if grade == 'P':
        continue

    if grade == 'A+':
        score = 4.5
    elif grade == 'A0':
        score = 4.0
    elif grade == 'B+':
        score = 3.5
    elif grade == 'B0':
        score = 3.0
    elif grade == 'C+':
        score = 2.5
    elif grade == 'C0':
        score = 2.0
    elif grade == 'D+':
        score = 1.5
    elif grade == 'D0':
        score = 1.0
    elif grade == 'F':
        score = 0.0

    # 학점 * 과목 평점
    subject_score += subject[1] * score
    total += subject[1]

avg = subject_score/total
print(avg)

# 딕셔너리 사용해서 해결

grade={'A+':4.5, 
      'A0':4.0, 
      'B+':3.5, 
      'B0':3.0, 
      'C+':2.5, 
      'C0':2.0, 
      'D+':1.5, 
      'D0':1.0, 
      'F':0.0,
      }

# 변수 초기화 안해서 런타임 에러 발생
score_sum = 0.0  # (학점 * 과목평점)의 합
b_sum = 0.0      # 학점의 총합

for _ in range(20):
    a, b, c = input().split() # 과목명, 학점, 등급

    if c != 'P':
        score = float(b) * grade[c] # 학점*과목평점
        score_sum += score # 전공과목별 (학점 × 과목평점)의 합
        b_sum += float(b) # 학점의 총합

print(score_sum/b_sum)