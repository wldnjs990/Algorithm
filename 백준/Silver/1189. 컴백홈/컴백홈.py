import sys;
input = sys.stdin.readline
# 컴백홈

# 한수는 캠프를 마치고 집에 돌아가려 한다.
# 한수는 현재 왼쪽 아래점에 있고 집은 오른쪽 위에 있다.
# 그리고 한수는 집에 돌아가는 방법이 다양하다.
# 단, 한수는 똑똑하여 한번 지나친 곳을 다시 방문하지는 않는다.

# 위 예제는 한수가 집에 돌아갈 수 있는 모든 경우를 나타낸 것이다.
# T로 표시된 부분은 가지 못하는 부분이다.
# 문제는 R x C 맵에 못가는 부분이 주어지고 거리 K가 주어지면 한수가 집까지도 도착하는 경우 중 거리가 K인 가짓수를 구하는 것이다.

# [입력]
# 첫 줄에 정수 R(1 ≤ R ≤ 5), C(1 ≤ C ≤ 5), K(1 ≤ K ≤ R×C)가 공백으로 구분되어 주어진다.
# 두 번째부터 R+1번째 줄까지는 R×C 맵의 정보를 나타내는 '.'과 'T'로 구성된 길이가 C인 문자열이 주어진다.

# [출력]
# 첫 줄에 거리가 K인 가짓수를 출력한다.

# [문제 풀이]
# 지도는 최대 25칸 => 재귀 + 백트레킹이 편할듯
# K 안에 집으로 도착하는 케이스 몇 개인지 구하기
# 시작점은 (R-1, 0), 집은 (0, C-1)
# 한번 방문한 지역은 다시 방문 안함
# dfs 돌려서 이동 횟수가 k에 도달했을때 (0, C-1)인지 확인시키게 하면 됨
# 4방향 탐색하면서 모든 이동 케이스에 visited 체크 / 원복 하면서 이동하면 될듯




dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# y, x, 목표 거리
R, C, K = map(int, input().split())
input = sys.stdin.read
inp = input()
map_arr = list(inp.split('\n'))
visited = [[False] * C for _ in range(R)]
visited[R-1][0] = True

def backtracking(lev=1, y=R-1, x=0):
    global ans
    if lev == K:
        if y == 0 and x == C - 1:
            ans += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < C and ny < R and not visited[ny][nx] and not map_arr[ny][nx] == 'T':
            visited[ny][nx] = True
            backtracking(lev + 1, ny, nx)
            visited[ny][nx] = False

ans = 0

backtracking()

print(ans)