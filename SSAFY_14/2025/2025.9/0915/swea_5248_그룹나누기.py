# SWEA 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    # 짝꿍 리스트 만들기
    groups = []
    for i in range(0, 2*M, 2):
        a = data[i]
        b = data[i+1]
        groups.append([a, b])

    # 2. 겹치는 그룹 합치기
    changed = True
    while changed:
        changed = False
        new_groups = []
        while groups:
            current = groups.pop()
            merged = False
            for i in range(len(groups)):
                # groups[i]와 current에 겹치는 사람이 있다면
                # 두 그룹을 중복 없이 하나로 합치고 다시 리스트로 저장
                if set(current) and set(groups[i]):
                    groups[i] = set(groups[i]).union(set(current))
                    merged = True
                    changed = True
                    break
            if not merged:
                new_groups.append(current)
        groups = new_groups

    print(new_groups)
    # 3. 그룹 외에 혼자 있는 사람 처리
    all_grouped = set()
    for g in groups:
        all_grouped.update(g)
    
    print(all_grouped)

    solo_count = N - len(all_grouped)
    total_groups = len(groups) + solo_count

    print(f'#{tc} {total_groups}')

