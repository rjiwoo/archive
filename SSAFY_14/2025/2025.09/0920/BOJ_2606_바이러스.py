# BOJ 2606번 바이러스

# 웜 바이러스
# 네트워크 상에서 연결되어 있으면 감염됨

N = int(input()) # 컴퓨터의 수
pair_count = int(input()) # 연결된 컴퓨터 쌍의 수

# 인접리스트?로 푸는게 좋을 것 같음. 인접행렬이 나은가? 몰라..
# 근데 그거 어케 설정해야하지
computer = [[] * N for _ in range(N)]

# print(computer)

for i in range(pair_count):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

