# 백준 2573 빙산

# 빙산을 2차원 배열에 표시한다
# 빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장된다.
# 빙산 이외의 바다에 해당되는 칸에는 0이 저장된다

# 배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다.
# 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다.
# 바닷물은 호수처럼 빙산에 둘러싸여 있을 수도 있다.

# 한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오

# [입력]
# 첫 줄에는 이차원 배열의 행의 개수와 열의 개수를 나타내는 두 정수 N과 M이 한 개의 빈칸을 사이에 두고 주어진다
# N과 M은 3 이상 300 이하이다.

# 그 다음 N개의 줄에는 각 줄마다 배열의 각 행을 나타내는 M개의 정수가 한 개의 빈 칸을 사이에 두고 주어진다.
# 각 칸에 들어가는 값은 0 이상 10 이하이다.

# 1 이상의 정수가 들어가는 칸의 개수는 10,000 개 이하이다.

# [풀이 과정]
# 최대 300 * 300 필드가 만들어짐 = 9000 => DFS 불가능
# BFS로 접근하자
# 로직을 2가지로 짜야할듯
# 1번째 : 섬 분리되었는지 구하기
# 2번째 : 섬 녹이기
# 섬이 2개로 분리될 때 까지 계속해서 반복하고, 분리되었을 경우에 분리된 년을 출력


# 섬 갯수 세기 BFS
def island_cnt(start):
    queue = [start]

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < M and ny < N and field[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append([nx, ny])
    return 1

def melt_island():
    # 녹는 지역 표시
    melting_area = []
    for y in range(N):
        for x in range(M):
            # 현재 지역이 섬이면
            if field[y][x]:
                # 바다 갯수
                sea = 0
                # 4면 검사해서 바다 있으면 +1
                for i in range(4):
                    # 짜피 외곽은 0이니 if문 필요없겠넴
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 인접한 면이 바다면 +1
                    if not field[ny][nx]:
                        sea += 1
                # 녹는 지역이면 melting_area에 좌표랑 인접 바다 수 담기
                if sea:
                    melting_area.append([x, y, sea])

    # 섬 녹이기
    for melt_targ in melting_area:
        x, y, sea = melt_targ
        if field[y][x] - sea < 0:
            field[y][x] = 0
        else:
            field[y][x] -= sea


N, M = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 결과
year = 0
while True:
    visited = [[False] * M for _ in range(N)]

    # 섬 갯수
    i_cnt = 0
    # 섬 갯수 세기
    for y in range(N):
        for x in range(M):
            if field[y][x] and not visited[y][x]:
                visited[y][x] = True
                i_cnt += island_cnt([x, y])
    if i_cnt == 0:
        year = 0
        break
    elif i_cnt > 1:
        break

    # 1년 추가
    year += 1

    # 섬 녹이기
    melt_island()

print(year)