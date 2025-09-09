# 벽돌 깨기

# 구술을 쏘아 벽돌을 깨트리는 게임을 하려고 한다.
# 구슬은 N번만 쏠 수 있고, 벽돌들의 정보는 아래와 같이 W x H 배열로 주어진다.
# ( 0 은 빈 공간을 의미하며, 그 외의 숫자는 벽돌을 의미한다. )

# 게임의 규칙은 다음과 같다.
# 1. 구슬은 좌, 우로만 움직일 수 있어서 항상 맨 위에 있는 벽돌만 깨트릴 수 있다.
# 2. 벽돌은 숫자 1 ~ 9 로 표현되며, 구술이 명중한 벽돌은 상하좌우로 ( 벽돌에 적힌 숫자 - 1 ) 칸 만큼 같이 제거된다.
# 3. 제거되는 범위 내에 있는 벽돌은 동시에 제거된다.
# 4. 빈 공간이 있을 경우 벽돌은 밑으로 떨어지게 된다.

# N 개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거하려고 한다
# N, W, H, 그리고 벽돌들의 정보가 주어질 때, 남은 벽돌의 개수를 구하라

# [입력값]
# 1 ≤ N ≤ 4
# 2 ≤ W ≤ 12
# 2 ≤ H ≤ 15

# [입력]
# 가장 첫 줄에는 총 테스트 케이스의 개수 T 가 주어지고,
# 그 다음 줄부터 T 개의 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 N, W, H 가 순서대로 공백을 사이에 두고 주어지고,
# 다음 H 줄에 걸쳐 벽돌들의 정보가 1 줄에 W 개씩 주어진다.

# [출력]
# 출력은 #t 를 찍고 한 칸 띄운 다음 정답을 출력한다.
# (t 는 테스트 케이스의 번호를 의미하며 1 부터 시작한다)

# [풀이]
# 저번에 풀었던 골4 문제 슈퍼 상위호환인데?
# bfs로 접근해야 하나?
# 위에서부터 돌을 하나씩 깨는 케이스를 queue에 담아줌

# 만들어야 하는 함수들
# 0. 시퀸스 한 번 할때마다 queue로 담는 BFS 함수
# 1. 돌 깼을때, 연쇄작용하는 함수
# 2. 벽돌 중력으로 내려주는 함수


from collections import deque
import copy

# 0. BFS
def BFS():
    global result
    deq = deque()
    for x in range(W):
        # 시작점, board 복사본, 블럭 부순 갯수, 남은 파괴 횟수
        deq.append([[x, start_y[x]], copy.deepcopy(board), N])

        while deq:
            # 시작점, board 복사본, 블럭 부순 갯수
            start, copy_board, least_break = deq.popleft()

            # 남은 파괴횟수가 다 돼면 종료
            if least_break == 0:
                # 남은 블럭 계산
                res = 0
                for y in range(H):
                    for x in range(W):
                        if copy_board[y][x]:
                            res += 1
                # 가장 많이 부순 블럭으로 담기
                result = min(result, res)
                continue
            
            # 현재 위치 파괴 진행(일단 깊은복사로 넣어)
            breaked_board = break_block(start, copy.deepcopy(copy_board))
            # 블럭 내려주기
            downed_board = down_block(copy.deepcopy(breaked_board))
            # 다시 시작 위치 잡기
            next_start_y = find_tops(copy.deepcopy(downed_board))
            # 다음 파괴 진행
            is_all_break = True
            for nx in range(W):
                # 현재 열에 블럭이 하나라도 존재하면 진행
                if next_start_y[nx] != -1:
                    is_all_break = False
                    deq.append([[nx, next_start_y[nx]], copy.deepcopy(downed_board), least_break - 1])
            # 만약 다 부숴졌으면 True 반환
            if is_all_break:
                return True
    # 다 돌렸는데 블럭 남았으면 False 반환
    return False

# 1. 맨 위의 블록 찾기
def find_tops(copy_block):
    # 맨 위의 블록 y좌표 담을 배열(없으면 -1)
    res = [-1] * W
    # 맨 위의 블럭 좌표 찾기
    for x in range(W):
        for y in range(H):
            # 블럭을 발견했으면
            if copy_block[y][x] != 0:
                # 해당 위치에 블럭 좌표 세기기
                res[x] = y
                break
    
    return [*res]


# 2. 돌 깨기 + 연쇄작용(복사한 board 받기)
def break_block(start, copy_board):
    deq = deque()
    deq.append(start)

    while deq:
        x, y = deq.popleft()
        # 연쇄할 블럭 갯수
        chain = copy_board[y][x] - 1
        # 현재 블럭 파괴
        copy_board[y][x] = 0

        for i in range(4):
            # 현재 위치 지정
            nx = x
            ny = y
            # chain만큼 반복
            for _ in range(chain):
                # nx, ny 연쇄범위만큼 순차적으로 키우기
                nx += dx[i]
                ny += dy[i]
                # 맵 밖을 벗어나지 않고, 방문하지 않았고, 블럭인 경우 부수기
                if nx >= 0 and ny >= 0 and nx < W and ny < H and copy_board[ny][nx]:
                    # 큐에 담기
                    deq.append([nx, ny])

    # 깬 블럭 갯수랑 copy_board 출력
    return copy.deepcopy(copy_board)


# 3. 벽돌 내리기
def down_block(breaked_board):
    for x in range(W):
        # 변환점(첫번째 0 지점)
        change_point = -1
        # 밑에서 위로 진행
        for y in range(H - 1, -1, -1):
            # 블럭이 있다면
            if breaked_board[y][x] > 0:
                # 변환점이 존재한다면
                if change_point >= 0:
                    # 위치 바꿔주기
                    breaked_board[change_point][x], breaked_board[y][x] = breaked_board[y][x], breaked_board[change_point][x]
                    # 변환점 변경
                    change_point -= 1
            # 블럭이 없다면(0이라면)
            else:
                # 변환점이 없다면
                if change_point == -1:
                    # 변환점으로 지정
                    change_point = y
    return copy.deepcopy(breaked_board)

T = int(input())

for tc in range(1, T+1):
    # 부술 돌 갯수 N, 넓이 W, 높이 H
    N, W, H = map(int, input().split())
    # 게임판
    board = [list(map(int, input().split())) for _ in range(H)]

    # 델타
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    # 처음 board에서 가장 먼저 등장하는 블럭의 y좌표들
    start_y = find_tops(board)

    # 결과값(가장 작은 값이 담겨야함)
    result = 100_000_000

    # 제발 잘 돌아가라
    is_all_breaked = BFS()

    if is_all_breaked:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {result}')
