# 연구소
 
# 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 
# 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
# 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 
# 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

# 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

# [입력]
# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 
# 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
# 빈 칸의 개수는 3개 이상이다.

# [출력]
# 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

# [문제 풀이]
# 벽 3개 치는걸 백트레킹으로 칠려고 하면 25만 정도가 나옴
# 벽 치고 1로 둘러쌓여진 안전 영역을 찾게 하려면..
# 일단 N+1지역에 추가로 벽(1)을 쳐주면 좀 더 수월하지 않을까 싶음 => ㄴㄴ 더 좋은 방법 생각남

# 먼저 행열을 순회해서 바이러스 수, 벽 수(3개 추가한 것 까지)를 저장해두기
# 벽을 3개 치고 나서 바이러스를 확산시키기 => 확산할 때 마다 바이러스 수 +1 해주기
# 바이러스 다 퍼뜨리고 나서 총 판의 갯수 - (바이러스 + 벽 수) 해주면 안전 구역의 범위를 구할 수 있음
# 근데 복잡도가.... ㅋㅋ

# 벽 3개 백트레킹으로 구하기 26만
# 바이러스 확산 BFS... 어 64인거 같은데?
# 26만 * 64 = 1670만 정도
# 이론상 가능!


from copy import deepcopy
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 바이러스 확산 BFS
def expand_virus(bio_map_copy):
  global max_area
  # 시작 바이러스 좌표 담기
  deq = deque(virus_dir)
  cur_safe_area = safe_area

  # BFS 실행
  while deq:
    x, y = deq.popleft()
    # 다음 방향으로 바이러스 확산
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위 안 넘기고 다음 구역이 0일때
      if nx >= 0 and ny >= 0 and nx < M and ny < N and bio_map_copy[ny][nx] == 0:
        # 안전구역 빼주기
        cur_safe_area -= 1
        # 바이러스 체크
        bio_map_copy[ny][nx] = 2
        deq.append([nx, ny])
  # 가장 큰 안전구역이면 업데이트
  if cur_safe_area > max_area:
    max_area = cur_safe_area


# 벽 설치 백트레킹
def build_wall(build):
  # 벽 3개 깔았으면 BFS 실행
  if build == 3:
    expand_virus(deepcopy(bio_map))
    return
  
  # 벽 설치
  for y in range(N):
    for x in range(M):
      # 빈 공간에 벽 설치하고 다음 벽 찾기
      if bio_map[y][x] == 0:
        bio_map[y][x] = 1
        build_wall(build + 1)
        # 원복
        bio_map[y][x] = 0

N, M = map(int, input().split())
bio_map = [list(map(int, input().split())) for _ in range(N)]

# 바이러스 좌표
virus_dir = []
# 안전한 구역(0) - 벽 3개
safe_area = N * M - 3
# 바이러스 좌표랑 안전한 구역 구하기
for y in range(N):
  for x in range(M):
    # 벽이면 안전구역 - 1
    if bio_map[y][x] == 1:
      safe_area -= 1
    # 바이러스면 좌표 담기, 안전구역 - 1
    elif bio_map[y][x] == 2:
      virus_dir.append([x, y])
      safe_area -= 1
# 결과
max_area = 0

build_wall(0)

print(max_area)
