import sys; 
input = sys.stdin.readline
# 최단경로

# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 
# 단, 모든 간선의 가중치는 10 이하의 자연수이다.

# [입력]
# 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 
# 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 
# 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 
# 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 
# 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. 
# u와 v는 서로 다르며 w는 10 이하의 자연수이다. 
# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

# [출력]
# 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 
# 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된

# [문제 풀이]
# 간선이 양방향이 아니네
# 간선이랑 간선끼리 1개 이상의 경로가 있을 수 있음
# 1 -> 2, 2 -> 1 이렇게
# 힙큐를 사용해서 현재 이동 가능한 간선 가중치중 가장 낮은 경로를 뽑아 해당 위치의 가중치를 업데이트 해준다
# 도착 노드랑 가중치를 시작 노드의 인덱스에 담아줘 배열을 만들어줘야 할 듯
# 그리고 최단 경로를 담을 inf 배열도 만들어줘야 할 듯

# 1 -> 2로 가는 경로가 2개 이상일 가능성도 있음
# 이 경우에 큐에 담기 전에 같은 경로의 최솟값을 먼저 구해야 할 거 같은데
# 간선 정보를 담을때부터 같은 경로의 노드인 경우에 가중치를 비교해 없애는 방법이 없을까?
# 노드 길이만큼의 배열을 가진 딕셔너리 하나 만들면 O(1) 만들거 같긴 하네

from heapq import heappop, heappush

V, E = map(int, input().split())
# 시작 노드
start_node = int(input())

# 최단 경로 배열
minimum_path = [100_000_000] * (V + 1)
# 시작 경로는 최단 경로가 필요없으니 0
minimum_path[start_node] = 0

# 노드별 이동 정보([가중치, 다음 노드])
move_info = [[] for _ in range(V+1)]
# 노드별 최소 가중치 정보 딕셔너리에 담기
for i in range(E):
    u, v, w = map(int, input().split())
    # 가중치 담기
    move_info[u].append((w, v))
    

# 우선순위 큐 pq
pq = []
# 시작점 간선, 가중치 담아주기
heappush(pq, (0, start_node))

# 다익스트라 진행
while pq:
    # 가중치가 작은 간선 먼저 빼기
    weight, node = heappop(pq)
    # 현재 가중치가 해당 노드의 최단경로보다 높다면 중단하고 다음으로 이동
    if weight > minimum_path[node]: continue
    # 도착 지점이랑 연결되어있는 노드의 가중치 더해서 pq에 새로 추가
    for next_edge in move_info[node]:
        # 현재 노드랑 연결되어있는 다음 가중치, 다음 노드 뽑기
        next_weight, next_node = next_edge
        # 다음 노드의 가중치가 현재 노드까지의 가중치 + 다음 노드의 가중치보다 크다면 추가하지 않기
        if weight + next_weight >= minimum_path[next_node]: continue
        # 아니면 다음 next_weight 가중치 더해서 업데이트 후 pq에 담아주기
        minimum_path[next_node] = weight + next_weight
        heappush(pq, (weight + next_weight, next_node))

# 결과 출력(0번째는 인덱스 맞추기용으로 끼워놓은거라 제외하기)
for i in range(1, V+1):
    # 값이 10보다 큰 수라면 정점 연결이 없다는 뜻 => INF 반환
    if minimum_path[i] == 100_000_000:
        print('INF')
    else:
        print(minimum_path[i])