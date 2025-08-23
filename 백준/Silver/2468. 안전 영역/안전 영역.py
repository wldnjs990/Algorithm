import sys;
# 얘도 스택 1000개 넘는다고..?
# 아 N이 100까지 가네
sys.setrecursionlimit(100000)
# 안전구역

# 먼저 어떤 지역의 높이 정보를 파악한다. 
# 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사하려고 한다.
# 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.

# 어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수이다.

# 어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오.
# 안전한 영역이 붙어있는 경우에 1개로 취급함(영역이니깐)

# 장마를 1 부터 100까지 다 테스트 해봐야하네
# 시간복잡도는 전혀 문제 없으니 결과 카운트들을 배열 하나에 계속 담고, 그 배열의 최댓값을 출력해주면 될듯

# 문제는 그냥 섬 갯수 구하기 처럼 진행하는데 4방향 델타로 풀면 될듯

# DFS
def DFS(x, y, dx, dy, rain_deep):
    # 방문한 지역이면 종료
    if visited[y][x]:
        return 0
    # 방문 체크
    visited[y][x] = True
    # 다음 지역 이동(인접한 다른 안전지역 있는지 확인용)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 다음 지역 검증
        if nx >= 0 and ny >= 0 and nx < N and ny < N and area[ny][nx] > rain_deep:
            DFS(nx, ny, dx, dy, rain_deep)
    # 이미 안전지역으로 검증됐으니 1 반환
    return 1

# 지역 크기
N = int(input())
# 지역
area = [list(map(int, input().split())) for _ in range(N)]
# 전체가 침수될 수 있는 깊이
max_rain_deep = 0
# 전체가 침수될 수 있는 깊이 구하기
for y in range(N):
    for x in range(N):
        if area[y][x] > max_rain_deep:
            max_rain_deep = area[y][x]

# 델타
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# 가장 많은 안전지역 수 = result
result = 0

# 호우 깊이 1 부터 전체 지역이 침수될 경우(max_rain_deep) 까지 진행
# 설마 안 잠기는 경우도 있냐..?
for rain_deep in range(0, max_rain_deep):
    # 깊이별로 visited 하나씩 생성
    visited = [[False] * N for _ in range(N)]
    # 깊이별로 안전구역 갯수 구하기
    safty_area = 0
    for y in range(N):
        for x in range(N):
            # 호우 깊이 보다 현재 지역의 높이가 더 높은 경우 DFS 진행
            if rain_deep < area[y][x]:
                safty_area += DFS(x, y, dx, dy, rain_deep)
    # 현재 깊이의 안전구역이 result 보다 많을 경우 업데이트
    if result < safty_area:
        result = safty_area

print(result)