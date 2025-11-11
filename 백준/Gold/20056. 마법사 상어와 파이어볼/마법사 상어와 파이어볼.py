# 마법사 상어와 파이어볼

# 어른 상어가 마법사가 되었고, 파이어볼을 배웠다.
# 마법사 상어가 크기가 N×N인 격자에 파이어볼 M개를 발사했다.
# 가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다.
# i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si이다. 위치 (r, c)는 r행 c열을 의미한다.
# 격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.
# 파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향을 의미하며, 정수로는 다음과 같다.

# 마법사 상어가 모든 파이어볼에게 이동을 명령하면 다음이 일들이 일어난다.
# 1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
# (이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.)
# 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
# 3. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
# 4. 파이어볼은 4개의 파이어볼로 나누어진다.
# 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
# 1. 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
# 2. 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
# 3. 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
# 4. 질량이 0인 파이어볼은 소멸되어 없어진다.
# 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.

# [입력]
# 첫째 줄에 N, M, K가 주어진다.
# 둘째 줄부터 M개의 줄에 파이어볼의 정보가 한 줄에 하나씩 주어진다.
# 파이어볼의 정보는 다섯 정수 ri, ci, mi, si, di로 이루어져 있다.
# 서로 다른 두 파이어볼의 위치가 같은 경우는 입력으로 주어지지 않는다.

# [출력]
# 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 출력한다.

# [문제 풀이]
# 쓰읍...
# 미세먼지나 세포 문제에서 조건이 덕지덕지 붙은 문제인거 같은데
# 파이어볼은 일단 전부 발사한 상태로 보는거 같네
# 8방향 델타 만들어야 함
# 그리고 총 K번 동안 다음 사이클을 돌려줘야 함
# [파이어볼 이동]
# 파이어볼이 가지고 있는 방향으로 속력만큼 이동시킴
# [파이어볼 합치기]
# 해당 위치의 파이어볼의 질량, 속력, 갯수를 전부 합해준다.
# [파이어볼 분해하기]
# 현재 위치의 파이어볼 정보에 따라 4방향으로 나눔

# 파이어볼 이동, 분해마다 파이어볼을 합쳐야 하네;
# 이동한 파이어볼들은 따로 관리를 해줘야 할듯


from collections import deque

N, M, K = map(int, input().split())
fireballs = [list(map(int, input().split())) for _ in range(M)]
map_arr = [[[] for _ in range(N)] for _ in range(N)]

# 8방향 델타
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 파이어볼 좌표
fireballs_dir = deque()

# 위치 ri, ci
# 질량 mi
# 방향 di
# 속력 si
# 파이어볼 깔아주기
for ri, ci, mi, si, di in fireballs:
    fireballs_dir.append((ri-1, ci-1))
    map_arr[ri-1][ci-1].append((mi, di, si))


# [파이어볼 이동]
def move_fireball():
    now_fireballs_dir = set()
    now_map_arr = [[[] for _ in range(N)] for _ in range(N)]

    while fireballs_dir:
        ny, nx = fireballs_dir.popleft()
        for nm, nd, ns in map_arr[ny][nx]:
            move_y = ny + dy[nd] * ns
            move_x = nx + dx[nd] * ns
            now_map_arr[move_y % N][move_x % N].append((nm, nd, ns))
            now_fireballs_dir.add((move_y % N, move_x % N))

    return deque([*now_fireballs_dir]), now_map_arr

# [파이어볼 합치기 & 4개로 분해]
def merge_fireball():
    now_fireballs_dir = set()
    now_map_arr = [[[] for _ in range(N)] for _ in range(N)]

    for ny, nx in fireballs_dir:
        # 파이어볼 갯수
        fireball_cnt = len(map_arr[ny][nx])
        # 파이어볼 한 개면 걍 놔두기
        if fireball_cnt == 1:
            now_map_arr[ny][nx].append(map_arr[ny][nx][0])
            now_fireballs_dir.add((ny, nx))
            continue

        tm, ts = 0, 0
        is_even, is_odd = False, False

        for nm, nd, ns in map_arr[ny][nx]:
            tm += nm
            ts += ns
            if nd % 2 == 0:
                is_even = True
            else:
                is_odd = True

        split_dir = [1, 3, 5, 7]
        # 방향이 전부 홀수거나 짝수이면 0, 2, 4, 6으로 변경
        if (is_even and not is_odd) or (not is_even and is_odd):
            split_dir = [0, 2, 4, 6]

        tm //= 5
        ts //= fireball_cnt
        # 질량이 0이면 패쓰
        if tm == 0: continue

        # 파이어볼 분해
        for i in split_dir:
            now_map_arr[ny][nx].append((tm, i, ts))
        now_fireballs_dir.add((ny, nx))

    return deque([*now_fireballs_dir]), now_map_arr

for _ in range(K):
    fireballs_dir, map_arr = move_fireball()
    fireballs_dir, map_arr = merge_fireball()

ans = 0
for y in range(N):
    for x in range(N):
        if map_arr[y][x]:
            for m, _, _ in map_arr[y][x]:
                ans += m

print(ans)