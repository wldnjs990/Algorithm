# 틱택토

# 틱택토 게임은 두 명의 사람이 번갈아가며 말을 놓는 게임이다. 
# 게임판은 3×3 격자판이며, 처음에는 비어 있다. 
# 두 사람은 각각 X 또는 O 말을 번갈아가며 놓는데, 반드시 첫 번째 사람이 X를 놓고 두 번째 사람이 O를 놓는다. 
# 어느 때든지 한 사람의 말이 가로, 세로, 대각선 방향으로 3칸을 잇는 데 성공하면 게임은 즉시 끝난다. 
# 게임판이 가득 차도 게임은 끝난다.

# 게임판의 상태가 주어지면, 그 상태가 틱택토 게임에서 발생할 수 있는 최종 상태인지를 판별하시오.

# [입력]
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 
# 각 줄은 9개의 문자를 포함하며, 'X', 'O', '.' 중 하나이다. 
# '.'은 빈칸을 의미하며, 9개의 문자는 게임판에서 제일 윗 줄 왼쪽부터의 순서이다. 
# 입력의 마지막에는 문자열 "end"가 주어진다.

# [출력]
# 각 테스트 케이스마다 한 줄에 정답을 출력한다. 
# 가능할 경우 "valid", 불가능할 경우 "invalid"를 출력한다.

# [문제 풀이]
# valid가 되는 경우를 생각해보자.
# O는 후공, X는 선공임
# O가 이기는 경우
# 1. X와 O 숫자가 동일, O만 3줄이 완성됨
# X가 이기는 경우
# 1. X가 O보다 1개 더 많음, X만 3줄이 완성됨
# 아직 진행중인 경우
# 1. X가 O보다 1개 더 많거나 같음, 둘 다 3줄이 완성되지 않음
# 이거 외엔 전부 invalid 처리 해주면 되지 않을까?


# 1 : 30

# 8방향 델타
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 빙고찾기 dfs
def dfs(x, y, targ, dir, cnt):
  if cnt == 3:
    return True
  
  nx, ny = x + dx[dir], y + dy[dir]
  if nx >= 0 and ny >= 0 and nx < 3 and ny < 3 and t_arr[ny][nx] == targ:
    res = dfs(nx, ny, targ, dir, cnt+1)
    return res
  
  return False
  

# O, X 빙고 있는지 확인하는 함수
def find_bingo():
  O_bingo = False
  X_bingo = False
  for y in range(3):
    for x in range(3):
      if t_arr[y][x] == 'O':
        targ = 'O'
        for dir in range(8):
          if not O_bingo:
            O_bingo = dfs(x, y, targ, dir, 1)
      elif t_arr[y][x] == 'X':
        targ = 'X'
        for dir in range(8):
          if not X_bingo:
            X_bingo = dfs(x, y, targ, dir, 1)
  return O_bingo, X_bingo

while True:
  inp = input()
  if inp == 'end': break

  X = 0
  O = 0

  t_list = list(inp)
  t_arr = [['.'] * 3 for _ in range(3)]
  # 1. 갯수 세기
  for i in range(9):
    t = t_list[i]
    if t == 'X':
      X += 1
      t_arr[i // 3][i % 3] = 'X'
    elif t == 'O':
      O += 1
      t_arr[i // 3][i % 3] = 'O'
  # print()
  # for i in range(3):
  #   print(t_arr[i])

  # O가 더 많으면 잘못된거
  if O > X:
    print('invalid')
    continue
  # 2. 갯수에 따른 X, O 빙고 여부 판단
  # 마지막 턴이 O인 경우
  if O == X:
    # O가 빙고를 만들었고, X는 빙고를 만들지 못했는지 확인
    O_bingo, X_bingo = find_bingo()
    if O_bingo and not X_bingo:
      print('valid')
      continue
    else:
      print('invalid')
      continue
  # 마지막 턴이 X인 경우
  elif O+1 == X:
    # X가 빙고를 만들었고, O는 빙고를 만들지 못했는지 확인
    O_bingo, X_bingo = find_bingo()
    if X_bingo and not O_bingo:
      print('valid')
      continue
    # 무승부로 마무리 된 경우 추가
    elif not O_bingo and not X_bingo and O + X == 9:
      print('valid')
      continue
    else:
      print('invalid')
      continue
  # 나머진 전부 invalid
  else:
    print('invalid')
    continue