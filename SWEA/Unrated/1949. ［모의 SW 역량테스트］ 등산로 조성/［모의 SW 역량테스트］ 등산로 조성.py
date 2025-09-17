# 등산로 조성

# 등산로를 만들기 위한 부지는 N * N 크기를 가지고 있으며, 이곳에 최대한 긴 등산로를 만들 계획이다.
# 등산로 부지는 아래 [Fig. 1]과 같이 숫자가 표시된 지도로 주어지며, 각 숫자는 지형의 높이를 나타낸다.

# 등산로를 만드는 규칙은 다음과 같다.
#    ① 등산로는 가장 높은 봉우리에서 시작해야 한다.
#    ② 등산로는 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결이 되어야 한다.
#        즉, 높이가 같은 곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가능하다.
#    ③ 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.
# N * N 크기의 지도가 주어지고, 최대 공사 가능 깊이 K가 주어진다.

# 이때 만들 수 있는 가장 긴 등산로를 찾아 그 길이를 출력하는 프로그램을 작성하라.

# [제약 사항]
# 1. 시간 제한 : 최대 51개 테스트 케이스를 모두 통과하는 데 C/C++/Java 모두 3초
# 2. 지도의 한 변의 길이 N은 3 이상 8 이하의 정수이다. (3 ≤ N ≤ 8)
# 3. 최대 공사 가능 깊이 K는 1 이상 5 이하의 정수이다. (1 ≤ K ≤ 5)
# 4. 지도에 나타나는 지형의 높이는 1 이상 20 이하의 정수이다.
# 5. 지도에서 가장 높은 봉우리는 최대 5개이다.
# 6. 지형은 정수 단위로만 깎을 수 있다.
# 7. 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.

# [입력]
# 입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 지도의 한 변의 길이 N, 최대 공사 가능 깊이 K가 차례로 주어진다.
# 그 다음 N개의 줄에는 N * N 크기의 지도 정보가 주어진다.

# [출력]
# 테스트 케이스 개수만큼 T개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.
# 각 줄은 "#t"로 시작하고 공백을 하나 둔 다음 정답을 출력한다. (t는 1부터 시작하는 테스트 케이스의 번호이다)
# 출력해야 할 정답은 만들 수 있는 가장 긴 등산로의 길이이다.

# [문제 풀이]
# 가장 높은 봉우리를 대상으로 만들 수 있는 가장 긴 등산로를 만듬
# 근데 등산로의 산은 계속해서 낮아져야함(같아도 안됨)
# 근데 필요하면 K를 소모해서 산을 깎을수도 있음
# 지도는 최대 8까지(8 * 8)

# 7. 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다. => 왜 지하에서부터 올라오려고 하냐?????

# 백트래킹 써야 할 거 같은데
# 지도가 최대 64라서 visited만 잘 체크해서 봉우리들 탐색하면 복잡도는 안 걸릴거 같음(스택 초과는 당연히 없고)
# 깎을 수 있는 여부 K랑 현재까지 등산로 길이 curpath를 파라미터에 담아서 백트래킹 함
# 만약에 다음 산이 지금 산 보다 놓거나 같을때, 가지고있는 K를 딱 한번만 사용해서 깎을 수 있음
# => 딱 한번만 깎아서 이동 가능
# => 여기서 중요한게 1 ~ k까지 깎을 수 있어서 이동 가능한 K 범위 내의 모든 경우를 추가시켜야 함(이거 체크 안하면 49개만 맞음)
# 그렇게 더 이상 등산로를 만들 수 없게 되면, 현재까지의 등산로 길이가 최대값인지 검증하고, 최대값이면 업데이트 한다.


# x좌표, y좌표, 이동횟수, 땅파기 사용 여부
def back_tracking(x, y, path, use_dig, now_h):
    global maximum_path
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < N and ny < N and not visited[ny][nx]:
            next_h = mountain_map[ny][nx]
            # 다음 산이 더 낮다면 이동
            if now_h > next_h:
                visited[ny][nx] = True
                back_tracking(nx, ny, path + 1, use_dig, next_h)
                visited[ny][nx] = False
            # 땅 파기 기회가 있고, 땅 파기를 써서 다음으로 이동할 수 있다면 이동
            elif not use_dig and now_h > next_h - K:
                # 땅 파서 갈 수 있는 경우 전부 넣기
                for j in range(1, K+1):
                    if now_h > next_h - j:
                        visited[ny][nx] = True
                        back_tracking(nx, ny, path + 1, use_dig + 1, next_h - j)
                        visited[ny][nx] = False
    # 못 갔으면 최대거리인지 검증
    if path > maximum_path:
        maximum_path = path

T = int(input())

# 델타
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain_map = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    higest = 0
    top_mountains = []
    for y in range(N):
        for x in range(N):
            if mountain_map[y][x] > higest:
                top_mountains = []
                higest = mountain_map[y][x]
                top_mountains.append([x, y])
            elif mountain_map[y][x] == higest:
                top_mountains.append([x, y])

    maximum_path = 0
    for start in top_mountains:
        sx = start[0]
        sy = start[1]
        # 모든 높은산 기준으로 백트래킹 시작
        visited[sy][sx] = True
        back_tracking(sx, sy, 1, 0, mountain_map[sy][sx])
        visited[sy][sx] = False

    print(f'#{tc} {maximum_path}')