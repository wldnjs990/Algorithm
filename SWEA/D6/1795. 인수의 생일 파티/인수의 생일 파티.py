# 인수의 생일 파티

# 인수가 사는 마을에는 N개의 집이 있고, 각 집에는 한 명의 사람이 살고 있다.

# N개의 집을 정점으로 볼 때,
# 도로는 어떤 집에서 다른 어떤 집으로 이동이 가능한 [단방향 간선]으로 볼 수 있으며,
# 각각에 대해서 이동하는데 시간이 정해져 있다.

# 도로는 모든 집들 간에 이동이 가능하도록 구성되어 있다.
# 집에 1번에서 N번까지의 번호를 붙일 때, 인수의 집은 X번 집이다.

# 오늘은 인수의 생일이기 때문에
# 모든 마을 사람들이 인수의 생일을 축하해주기 위해 X번 집으로 모인다.

# 각 사람들은 자신의 집에서 X번 집으로 오고 가기 위해 최단 시간으로 이동한다.
# 도로가 단 방향이기 때문에 이용하는 도로는 오고 갈 때 다를 것이다.

# X번 집으로 오고 가는데 드는 시간 중에서 가장 오래 걸리는 집은 어느 정도 걸리는지 구하는 프로그램을 작성하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 세 정수 N,M,X가 공백으로 구분되어 주어진다.
# X = 인수 정점
# N = 정점
# M = 간선 수
# (1 ≤ X ≤ N ≤ 1,000, 1 ≤ M ≤ 10,000)
# 다음 M개의 각 줄에는 세 정수 x, y, c 가 공백으로 구분되어 주어진다.
# (1 ≤ x, y ＜ N, 1 ≤ c ≤ 100)
# 이는 x번 집에서 y번 집으로 가는 데 시간이 c가 걸리는 단 방향 도로가 존재한다는 뜻이다.

# [출력]
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 오고 가는데 걸리는 시간이 가장 긴 거리를 출력한다.

# [문제 풀이]
# 정방향, 역방향 따로 다익스트라 구해서 각 정점별 합 중에서 최대값 구하면 됨
# 입력값 보니 인접 리스트 만들어서 구하면 됨

from heapq import heappop, heappush

def f_dijkstra(start_node):
    pq = [(0, start_node)]

    while pq:
        w, s = heappop(pq)

        # 현재가 최소가중치인지 검증
        if w >= f_minimum_list[s]: continue
        # 최소가중치 업데이트
        f_minimum_list[s] = w

        for next in f_adj_list[s]:
            # 다음 지역 가중치 체크
            nw = w + next[0]
            # 가중치가 작으면 힙큐 추가
            if f_minimum_list[next[1]] > nw:
                heappush(pq, (nw, next[1]))

def b_dijkstra(start_node):
    pq = [(0, start_node)]

    while pq:
        w, s = heappop(pq)

        # 현재가 최소가중치인지 검증
        if w >= b_minimum_list[s]: continue
        # 최소가중치 업데이트
        b_minimum_list[s] = w

        for next in b_adj_list[s]:
            # 다음 지역 가중치 체크
            nw = w + next[0]
            # 가중치가 작으면 힙큐 추가
            if b_minimum_list[next[1]] > nw:
                heappush(pq, (nw, next[1]))

T = int(input())

for tc in range(1, T+1):
    # 정점, 간선, 인수 정점
    N, M, X = map(int, input().split())

    # 인접 리스트(정방향)
    f_adj_list = [[] for _ in range(N+1)]
    # 인접 리스트(역방향)
    b_adj_list = [[] for _ in range(N+1)]

    # 인접 리스트 채우기(정방향, 역방향 둘 다)
    # 반드시 가중치를 먼저 담아야 함
    for i in range(M):
        # 출발, 도착, 시간(가중치)
        s, e, w = map(int, input().split())
        # 정방향 인접 리스트 담기
        f_adj_list[s].append((w, e))
        # 역방향 인접 리스트 담기
        b_adj_list[e].append((w, s))

    # 정방향 최단 거리 리스트
    f_minimum_list = [float('inf') for _ in range(N+1)]
    f_minimum_list[0] = 0
    # 역방향 최단 거리 리스트
    b_minimum_list = [float('inf') for _ in range(N+1)]
    b_minimum_list[0] = 0

    # 정방향 다익스트라
    f_dijkstra(X)
    # 역방향 디익스트라
    b_dijkstra(X)

    # 최대값(결과)
    maximum_path = 0

    # 최대값 구하기
    for i in range(1, N+1):
        now_path = f_minimum_list[i] + b_minimum_list[i]
        if now_path > maximum_path:
            maximum_path = now_path

    print(f'#{tc} {maximum_path}')