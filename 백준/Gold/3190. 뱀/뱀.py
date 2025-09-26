# 뱀

# 'Dummy' 라는 도스게임이 있다.
# 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다.
# 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다.
# 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다.
# 뱀은 처음에 오른쪽을 향한다.

# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

# [입력]
# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다.
# 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며.
# 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.
# X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

# [출력]
# 첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

# [문제풀이]
# 빈공간은 0, 뱀은 1, 사과는 2
#

from collections import deque

# 게임 진행
def dummy(turn_info):
    # 이동 정보
    move_deq = deque()
    # 머리좌표, 시간 담기(1초 기준)
    move_deq.append([1, 2, 1])
    # 현재 방향
    now_dir = 0
    # 다음 회전 정보
    turning_time, turning_dir = turn_info.popleft()
    # 머리 뒤에 있는 뱀 좌표들 담기(꼬리 후보)
    tails = deque()
    tails.append((1, 1))
    # 꼬리 좌표
    tx, ty = tails.popleft()
    while move_deq:
        hy, hx, time = move_deq.popleft()
        # 사과가 존재하면 꼬리 자르지 말기
        if game_board[hy][hx] == 2:
            game_board[hy][hx] = 1
            # 꼬리 업데이트
            tails.append((hy, hx))
        # 사과 없으면 꼬리 자르기
        else:
            game_board[hy][hx] = 1
            game_board[ty][tx] = 0
            # 꼬리후보가 있으면 위치 변경
            if tails:
                ty, tx = tails.popleft()
                tails.append((hy, hx))
            # 없으면 지금 머리로 지정
            else:
                ty = hy
                tx = hx
        # 머리 회전시간이 되었을때 머리 회전하기
        if time == turning_time:
            # L일땐 왼쪽 회전(-1)
            # D일땐 오른쪽 회전(+1)
            if turning_dir == 'L':
                now_dir = (now_dir - 1 + 4) % 4
            elif turning_dir == 'D':
                now_dir = (now_dir + 1 + 4) % 4
            # 회전 정보가 남아있으면 다음 회전 정보 배치
            if turn_info:
                turning_time, turning_dir = turn_info.popleft()

        nhy = hy + dy[now_dir]
        nhx = hx + dx[now_dir]
        # 다음 방향 이동(시간 추가해서)
        if nhy >= 1 and nhx >= 1 and nhy <= N and nhx <= N and game_board[nhy][nhx] != 1:
            move_deq.append([nhy, nhx, time + 1])
        else:
            return time + 1


# 델타
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 보드 크기
N = int(input())
# 사과 갯수
K = int(input())
# 사과 위치
apples = [list(map(int, input().split())) for _ in range(K)]
# 뱀의 방향 전환 횟수
L = int(input())
# 뱀의 시간별 방향 전환 정보
turn_info = [list(input().split()) for _ in range(L)]
# 시간은 정수로 변환
for info in turn_info:
    info[0] = int(info[0])
# 덱으로 변환
turn_info = deque(turn_info)

# 게임판(벽 추가)
game_board = [[0] * (N+2) for _ in range(N+2)]
# 뱀 배치
game_board[1][1] = 1
# 사과 배치
for a_locate in apples:
    ay, ax = a_locate
    game_board[ay][ax] = 2

# 게임 시간 구하기(뱀의 시간별 방향 전환 정보 담아서)
game_time = dummy(turn_info)

print(game_time)