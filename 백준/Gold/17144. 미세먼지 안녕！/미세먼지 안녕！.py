import sys;
input = sys.stdin.readline
# 미세먼지 안녕!

# 공기청정기의 성능을 테스트하기 위해 구사과는 집을 크기가 R×C인 격자판으로 나타냈고, 1×1 크기의 칸으로 나눴다. 
# 구사과는 뛰어난 코딩 실력을 이용해 각 칸 (r, c)에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발했다. 
# (r, c)는 r행 c열을 의미한다.

# 공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다. 
# 공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다.

# 1초 동안 아래 적힌 일이 순서대로 일어난다.

# 1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
# (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
# 확산되는 양은 Ar,c/5이고 소수점은 버린다. 즉, ⌊Ar,c/5⌋이다.
# (r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수) 이다.

# 2. 공기청정기가 작동한다.
# 공기청정기에서는 바람이 나온다.
# 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

# 방의 정보가 주어졌을 때, T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자.

# [입력]
# 첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.
# 둘째 줄부터 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다. 
# 공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다. 
# -1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.

# [출력]
# 첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.

# [문제 풀이]
# 공기청정기가 좀 구린데?
# 구현은 되겠는데, 시간복잡도가 괜찮으려나 모르겠네

# [미세먼지 확산]
# 배열에서 먼지가 있는 지역을 발견하면 확산되는 먼지 양, 확산되는 칸 갯수를 구해서 먼지를 먼제 빼줌
# 그 다음 확산되는 지역의 먼지들의 좌표와 먼지수를 배열에 저장해두고 다음 먼지를 찾음
# 마지막에 배열에 확산되는 먼지들을 한번에 더해줘야함

# [공기청정기]
# 함수 만들기 전에 공기청정기의 윗 좌표와 아랫좌표를 먼저 구한다.
# 공기 청정기의 윗 좌표는 상 -> 우 -> 하 -> 좌 순으로 배열의 끝에 닿을때 까지 순회하면서, 만나는 먼지들을 움직이는 방향의 반대로 이동시키기
# (순환하는 방향의 반대로 해야지 밀리는 먼지가 겹치는 일이 없음)
# 공기 청정기의 아랫 좌표는 하 -> 우 -> 상 -> 좌 순으로 똑같이 진행
# 공기 청정기 좌표로 들어오는 먼지들은 전부 삭제

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# [미세먼지 확산]
def diffusion():
  # 확산 결과 담을 배열
  diffusion_arr = []
  for y in range(R):
    for x in range(C):
      # 먼지 있으면
      if clean_arr[y][x] > 0:
        # 확산 가능한 먼지인지 먼저 확인
        diffuse_mungi = clean_arr[y][x] // 5
        if diffuse_mungi == 0 : continue

        # 확산 가능하면 4방향 확산 진행
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          # 먼지가 갈 수 있는 지역이면 확산
          if nx >= 0 and ny >= 0 and nx < C and ny < R and clean_arr[ny][nx] != -1:
            # 먼지 확산되는 좌표, 먼지양 배열에 저장
            diffusion_arr.append([nx, ny, diffuse_mungi])
            # 확산되는 양 만큼 빼주기
            clean_arr[y][x] -= diffuse_mungi

  # 확산 진행
  for diffuse in diffusion_arr:
    tx, ty, mungi = diffuse
    clean_arr[ty][tx] += mungi

# [공기 청정기]
def cleaner(locate):
  # 돌아갈 싸이클
  cycle = []
  # 공기청정기 분기영역
  divide = 0
  if locate == top:
    cycle = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    divide = bottom
  elif locate == bottom:
    cycle = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    divide = top
  
  turn = 0
  dx = cycle[turn][0]
  dy = cycle[turn][1]

  x = 0 + dx
  y = locate + dy
  # 처음 위치(공기청정기 킬각 볼 수 있는 곳)에 먼지가 있으면 그거 바로 없애기
  clean_arr[y][x] = 0
  # 공기청정기 1번 순회할 때 까지 반복
  while clean_arr[y][x] != -1:
    # 먼지 발견시 끌어당기기(위치 변경)
    if clean_arr[y][x] > 0:
      clean_arr[y][x], clean_arr[y - dy][x - dx] = clean_arr[y - dy][x - dx], clean_arr[y][x]
    # 다음 좌표가 벽에 걸리거나, 분기 영역에 걸리는지 확인하고, 걸리면 방향 틀어주기
    nx = x + dx
    ny = y + dy
    if nx >= 0 and ny >= 0 and nx < C and ny < R and ny != divide:
      pass
    # 걸린 경우 방향 틀어주기
    else:
      turn += 1
      dx = cycle[turn][0]
      dy = cycle[turn][1]
    x += dx
    y += dy

# 이대로 T초 까지 반복한 후에 먼지 수 전부 출력
R, C, T = map(int, input().split())
# 미세먼지 판
clean_arr = [list(map(int, input().split())) for _ in range(R)]

# 미세먼지 상, 하 좌표
top = 0
bottom = 0
for y in range(R):
  if clean_arr[y][0] == -1 : 
    top = y
    bottom = y+1
    break

while T > 0:
  # 시간 빼기
  T -= 1
  # 미세먼지 확산
  diffusion()
  # 청정기 상단 BFS
  cleaner(top)
  # 청정기 하단 BFS
  cleaner(bottom)

ans = 0
for i in range(R):
  ans += sum(clean_arr[i])
# 공기 청정기 -1 빼주기
print(ans + 2)