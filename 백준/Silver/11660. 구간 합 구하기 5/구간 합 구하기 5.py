import sys;
input = sys.stdin.readline

# 구간 합 구기

# N×N개의 수가 N×N 크기의 표에 채워져 있다. 
# (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. 
# (x, y)는 x행 y열을 의미한다.

# [입력]

# 첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 
# 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 
# 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 
# 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)

# [출력]
# 총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.

# [문제 풀이]
# 시간복잡도만 안 걸리면 x1, y1은 인덱스 기준으로 -1 해주고 x2, y2는 range 특성상 그대로 집어넣어서 2중 for문으로 풀면 되겠는데
# 시간초과 뜨네
# 1행에 대해 누적합을 구한 행열을 하나 만들면 2중 for문까지 안 가고 풀 수 있음
# 이거 한번 해보자
# 이것도 시간초과 뜨네
# 열도 누적합 구해서 한번에 찍는게 가능한가??
# 일단 만들어보자

N, M = map(int, input().split())
num_arr = [list(map(int, input().split())) for _ in range(N)]
dir_arr = [list(map(int, input().split())) for _ in range(M)]

for y in range(N):
  # 1행의 누적합을 구할때 0번째는 그대로니깐 더하지말기
  for x in range(1, N):
    num_arr[y][x] = num_arr[y][x] + num_arr[y][x-1]

for x in range(N):
  # 1열의 누적합을 구할때 0번째는 그대로니깐 더하지말기
  for y in range(1, N):
    num_arr[y][x] = num_arr[y][x] + num_arr[y-1][x]

for dirs in dir_arr:
  # 아니 이건 입력값이 잘못됐잖아요
  y1,x1,y2,x2 = dirs
  x1 -= 1
  y1 -= 1
  x2 -= 1
  y2 -= 1
  now = num_arr[y2][x2]
    
  if y1 == 0 and x1 == 0:
    print(now)
  elif y1 == 0:
    print(now - num_arr[y2][x1-1])
  elif x1 == 0:
    print(now - num_arr[y1-1][x2])
  else:
    print(now + num_arr[y1-1][x1-1] - num_arr[y2][x1-1] - num_arr[y1-1][x2])
