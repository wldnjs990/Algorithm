import sys;
# 문제 자체가 파이썬은 DFS로 못 푸는 문제네
# BFS 써서 풀어야 하는 문제긴 한데 일단 DFS로 풀 수 있게 콜스택 리미트 10000개로 설정
sys.setrecursionlimit(10000)
# 섬의 갯수

# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다.
# 섬의 개수를 세는 프로그램을 작성하시오.

# 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다.
# w와 h는 50보다 작거나 같은 양의 정수이다.
# 둘째 줄부터 h개 줄에는 지도가 주어진다
# 1은 땅, 0은 바다이다.

# [내 생각]
# 대각선끼리도 연결되어있으면 같은섬으로 취급
# 8방향 델타를 사용해서 탐색해야함
# visited는 하나만 만들어서 공유하도록 설정
# 함수가 종룔되었을때 무조건 1을 반환하는데, 연결되어있는 모든 섬의 visited를 채워주는게 관건

# DFS
def DFS(x, y, dx, dy):
    # 방문한 지역이면 0 반환
    if visited[y][x]:
        return 0
    # 방문한 섬 체크
    visited[y][x] = True
    # 다음 땅 이동(섬 표시용)
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        # 현재 좌표가 지도를 벗어나지 않았는지, 다음 지역이 땅인지 검증
        if nx >= 0 and ny >= 0 and nx < w and ny < h and land[ny][nx]:
            DFS(nx, ny, dx, dy)
    # 현재 지역은 섬이니 1 반환
    return 1
    
while True:
    # 가로, 세로 받기
    w, h = map(int, input().split())
    # 가로, 세로가 0, 0이면 문제 종료(뭐 이딴게 다있노)
    if w + h == 0:
        break
    # 섬 지도
    land = [list(map(int, input().split())) for _ in range(h)]
    # 섬 방문여부
    visited = [[False]* w for _ in range(h)]
    # 섬 갯수
    island_ctn = 0
    # 8방향 델타
    dx = [1, 0, -1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, 1, -1, 1, -1]

    # 반복문 돌려서 DFS 실행
    for y in range(h):
        for x in range(w):
            # 현재 지역이 땅이면 DFS 실행
            if land[y][x]:
                island_ctn += DFS(x, y, dx, dy)


    print(island_ctn)