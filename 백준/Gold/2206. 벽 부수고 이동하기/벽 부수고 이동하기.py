import sys;
# 벽 부수고 이동하기

# N×M의 행렬로 표현되는 맵이 있다.
# 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
# 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
# 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

# [입력]
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다.
# 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

# [출력]
# 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

# [문제 풀이]
# 늘 보던 맛인거 같은데
# 벽은 한개까지 부술 수 있음
# 최단경로니깐 BFS를 써야함
# 3차원 visited로 벽을 부순 경우까지 합쳐서 구하면 될듯
# 벽 부수기는 썻다, 안썻다로 나눌 수 있어서 오히려 편함

from collections import deque

def bfs():
    while deq:
        # 좌표, 이동횟수, 파괴가능(0, 1)
        x, y, cnt, destroy = deq.popleft()

        # 목적지 도착했으면 이동경로 반환
        if x == M - 1 and y == N - 1:
            return cnt

        # 다음 경로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 현재 지역 이동 가능한지 체크
            if nx >= 0 and ny >= 0 and nx < M and ny < N:
                # 다음 지역이 벽인데, 부술 수 있으면 벽 부수고 다음으로 이동
                if map_arr[ny][nx] == 1 and destroy and not visited[ny][nx][destroy - 1]:
                    visited[ny][nx][destroy - 1] = True
                    deq.append([nx, ny, cnt+1, destroy - 1])
                # 0이면 방문여부 확인 후 이동
                elif map_arr[ny][nx] == 0 and not visited[ny][nx][destroy]:
                    visited[ny][nx][destroy] = True
                    deq.append([nx, ny, cnt + 1, destroy])

    # 도착 못했으면 -1 반환
    return -1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
map_arr = [list(map(int, input())) for _ in range(N)]

# 3차원 visited
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = True

deq = deque()
deq.append([0, 0, 1, 1])

print(bfs())

