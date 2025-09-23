# 치즈

# 아래 <그림 1>과 같이 정사각형 칸들로 이루어진 사각형 모양의 판이 있고,
# 그 위에 얇은 치즈(회색으로 표시된 부분)가 놓여 있다.
# 판의 가장자리(<그림 1>에서 네모 칸에 X친 부분)에는 치즈가 놓여 있지 않으며 치즈에는 하나 이상의 구멍이 있을 수 있다.

# 이 치즈를 공기 중에 놓으면 녹게 되는데 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다.
# 치즈의 구멍 속에는 공기가 없지만 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가 들어가게 된다.
# <그림 1>의 경우, 치즈의 구멍을 둘러싼 치즈는 녹지 않고 ‘c’로 표시된 부분만 한 시간 후에 녹아 없어져서 <그림 2>와 같이 된다.

# 다시 한 시간 후에는 <그림 2>에서 ‘c’로 표시된 부분이 녹아 없어져서 <그림 3>과 같이 된다.

# <그림 3>은 원래 치즈의 두 시간 후 모양을 나타내고 있으며, 남은 조각들은 한 시간이 더 지나면 모두 녹아 없어진다.
# 그러므로 처음 치즈가 모두 녹아 없어지는 데는 세 시간이 걸린다.
# <그림 3>과 같이 치즈가 녹는 과정에서 여러 조각으로 나누어 질 수도 있다.

# 입력으로 사각형 모양의 판의 크기와 한 조각의 치즈가 판 위에 주어졌을 때,
# 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과
# 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 구하는 프로그램을 작성하시오.

# [입력]
# 첫째 줄에는 사각형 모양 판의 세로와 가로의 길이가 양의 정수로 주어진다.
# 세로와 가로의 길이는 최대 100이다.
# 판의 각 가로줄의 모양이 윗 줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다.
# 치즈가 없는 칸은 0, 치즈가 있는 칸은 1로 주어지며 각 숫자 사이에는 빈칸이 하나씩 있다.

# [출력]
# 첫째 줄에는 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력하고,
# 둘째 줄에는 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 출력한다.

# [문제풀이]
# 외곽의 치즈가 녹아야하는데, 치즈가 대각선으로 연결되어있다면 그 안에 빈 공간은 안 녹음
# 치즈판의 시작점을 기준으로 4방향 BFS를 돌린다.
# 치즈판의 빈 공간이라면 visited를 체크해주면서 이동한다.
# 만약에 다음 경로에 visited하지 않은 치즈가 존재한다면
# 그 곳은 이동 못하고,
# 녹는다는 의미의 좌표를 따로 배열에 저장하고,
# visited 체크를 해준다
# 한 번 순환을 끝마치면 좌표에 저장되었던 치즈들을 전부 녹인다.(0으로 바꿔주기)
# 모든 치즈가 녹아서 0이 되는 순간에 마지막에 녹은 치즈 갯수와 총 녹인 횟수를 출력해주면 끝

# 시간복잡도는 100 * 100 = 10000을 치즈가 다 녹을때 까지 순회하게 되는데, 초과는 안 날거 같음


from collections import deque
# 치즈 녹이기 1싸이클
def melt_cheese(start):
    global last_cheese
    global melting_cnt
    global start_at
    deq = deque()
    # 배열 아이템 채워주기
    for item in start:
        deq.append(item)
    # 현재 지우는 치즈
    now_cheese = 0
    # 선택된 치즈
    selected_cheeses = set()
    while deq:
        x, y = deq.popleft()

        # 다음 방향 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않았고, 방문하지 않은 지역일 경우
            if nx >= 0 and ny >= 0 and nx < M and ny < N and not visited[ny][nx]:
                # 치즈라면 selected_cheese에 좌표 담고 종료
                if cheese_arr[ny][nx]:
                    # set 담는데 튜플 써야함
                    selected_cheeses.add((nx, ny))
                # 빈 공간(0)이라면 다음 좌표로 이동하기
                else:
                    # 방문 체크
                    visited[ny][nx] = True
                    deq.append([nx, ny])
    # set 배열로 교체
    selected_cheeses = [*selected_cheeses]
    # 치즈 지우기
    for melt in selected_cheeses:
        now_cheese += 1
        mx, my = melt
        cheese_arr[my][mx] = 0
    # 다음 시작점 치즈 태두리 좌표로 저장(다음에 큐에 담는 용도)
    start_at = selected_cheeses

    # 체크가 된 치즈가 하나도 없다면 전부 다 녹인거임(싸이클 종료)
    if not now_cheese:
        return

    # 치즈 정보 업데이트
    last_cheese = now_cheese
    # 녹인 횟수 추가
    melting_cnt += 1





N, M = map(int, input().split())
cheese_arr = [list(map(int, input().split())) for _ in range(N)]
# 방문여부
visited = [[False] * M for _ in range(N)]
# 0, 0 초기화
visited[0][0] = True
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 녹인 횟수
melting_cnt = 0
# 마지막 남은 치즈
last_cheese = 0

# 시작점
start_at = [(0, 0)]

# 싸이클 여부
cycle = 1

# 녹일 수 있는 치즈가 없어질 때 까지 싸이클 반복
while start_at:
    # 치즈 녹이기 1싸이클 진행
    melt_cheese(start_at)

print(melting_cnt)
print(last_cheese)