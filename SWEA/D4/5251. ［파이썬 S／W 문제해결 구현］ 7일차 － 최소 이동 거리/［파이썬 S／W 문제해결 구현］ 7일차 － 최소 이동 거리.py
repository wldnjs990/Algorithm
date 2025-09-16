# 최소 이동 거리

# A도시에는 E개의 일방통행 도로 구간이 있으며,
# 각 구간이 만나는 연결지점에는 0부터 N번까지의 번호가 붙어있다.

# 구간의 시작과 끝의 연결 지점 번호,
# 구간의 길이가 주어질 때,
# 0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리가 얼마인지 출력하는 프로그램을 만드시오.

# 모든 연결 지점을 거쳐가야 하는 것은 아니다.

# [입력]
# 첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 연결지점 번호N과 도로의 개수 E가 주어진다.
# 다음 줄부터 E개의 줄에 걸쳐 구간 시작 s, 구간의 끝 지점 e, 구간 거리 w가 차례로 주어진다. ( 1<=T<=50, 1<=N, s, e<=1000, 1<=w<=10, 1<=E<=1000000 )
# 정점 갯수는 최대 1000개

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

# [문제풀이]
# 단방향 인접 리스트 문제인거 같음
# 이제 다익스트라를 곁들인
# 누적거리를 더하면서 최단거리 리스트를 업데이트 해주자

# 우선순위 큐 불러오기
from heapq import heappop, heappush

def dijkstra(start_node):
    # 우선순위 큐로 사용할 리스트에 시작정점과 가중치 담기
    pq = [(0, start_node)]

    while pq:
        # 현재 힙큐 현재 노드에서 가중치가 가장 짧은 노드 찾기
        w, e = heappop(pq)

        # 현재 정점의 가중치가 지금까지 나온 정점의 최소 거리보다 길거나 같으면 패쓰
        if minimum_paths[e] <= w: continue

        # 현재 정점의 최소값 업데이트
        minimum_paths[e] = w

        # 현재 정점과 연결된 인접 정점들 가중치 업데이트 후 우선순위 큐에 담아주기
        for next in adj_list[e]:
            # 현재 노드의 가중치가 지금까지 나온 정점의 최소 거리보다 짧다면 담아주기
            if next[0] + w < minimum_paths[next[1]]:
                heappush(pq, (next[0] + w, next[1]))

T = int(input())

for tc in range(1, T+1):
    # N = 0에서 가야하는 지역, E = 도로 갯수
    N, E = map(int, input().split())

    # 단방향 인접 리스트 만들기(최대 정점 갯수가 1000개)
    adj_list = [[] for _ in range(N+1)]

    # 인접 리스트 만들기
    for _ in range(E):
        s, e, w = map(int, input().split())
        # 시작 정점에 (가중치, 이동 정점) 담기
        adj_list[s].append((w, e))

    # 정점 최소 이동거리 담기
    minimum_paths = [float('inf') for _ in range(N+1)]

    dijkstra(0)

    print(f'#{tc} {minimum_paths[N]}')