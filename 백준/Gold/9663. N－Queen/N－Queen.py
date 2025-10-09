# N-Queen

# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# [입력]
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

# [출력]
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

# [문제 풀이]
# 이게 백트레킹으로 풀어지는거라고?
# 퀸이 8방향으로 쭉 직진 가능한 기물
# 퀸을 자리에 놓을때 8방향으로 쭉 visited를 체크해주기
# 배치 가능한 지역(visited가 체크되지 않은 지역)에 퀸을 배치한다 or 배치하지 않는다로 dfs 진행
# 배치할 때 마다 퀸의 갯수를 하나씩 빼면서 진행하고, 퀸을 끝까지 배치한 케이스가 나오면 결과 ans에 +1 해주기
# 다음 퀸 배치할 공간 찾으려면 배열을 풀 순회해야 할 거 같은데 이러면 복잡도 멸망할거 같은데
# 15 * 15가 225가 나오는데 이정도면 할만할지도

# 틀려서 종우형 문제풀이 봤음
# 퀸을 y한 칸씩 배치하는 그런 똑똑한 생각을 못했다...
# 퀸은 y축이고, 현재 y축에서 퀸이 이동할 수 있는 지역들을 대상으로 백트레킹 진행하면 됨

dx = [1, 1, 0,-1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def backtracking(y):
  global ans
  # queen 다 배치했으면 ans + 1
  if y == N:
    ans += 1
    return
  
  # 현재 행의 x 지역 체크
  for x in range(N):
    if not chess_board[y][x]:
      visited = []
      # 퀸 영역 표시
      chess_board[y][x] += 1
      for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        while nx >= 0 and ny >= 0 and nx < N and ny < N:
          chess_board[ny][nx] += 1
          visited.append([ny, nx])
          nx += dx[i]
          ny += dy[i]
      # 다음 퀸 이동
      backtracking(y + 1)
      # 퀸 원복
      chess_board[y][x] -= 1
      for ey, ex in visited:
        chess_board[ey][ex] -= 1

N = int(input())

chess_board = [[0] * N for _ in range(N)]

ans = 0

backtracking(0)

print(ans)