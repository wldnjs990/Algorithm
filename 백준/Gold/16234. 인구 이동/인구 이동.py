import sys;
input = sys.stdin.readline
# 인구 이동

# N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다.
# 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다.
# 인접한 나라 사이에는 국경선이 존재한다.
# 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

# 오늘부터 인구 이동이 시작되는 날이다.

# 인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다.
# 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.
# 각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

# [입력]
# 첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
# 둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다.
# r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)
# 인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

# [출력]
# 인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.

# [문제 풀이]
# 2 단계로 나눠서 풀어야겠네

# [연합 만들기]
# 현재 국가를 기준으로 4방향의 국가들끼리 연합 가능여부 판단하기
# 연합 가능하면 따로 준비해둔 visited 배열에 표시해주기
# visited 배열 순회하면서 True인 국가 발견하면 BFS 실행
# 연합 국가가 하나도 없으면 이동 기간 반환하고 종료


# [연합 병합]
# True인 국가로 부터 4방향 탐색
# 국가의 좌표를 저장하고, 국가의 인구수를 더해주기
# 전부 다 더했으면 국가의 인구수를 좌표 길이만큼 나눠주고, 나눈 인구 배분해주기

# 이거 2개를 1싸이클로 쳐서 이동까지 했으면 결과값에 1 더해주면 될듯

from collections import deque

N, L, R = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(N)]
# 연합
visited = [[0] * N for _ in range(N)]

# 델타
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# [연합 만들기]
def make_association():
    # 결과 일수
    day = 0
    while True:
        idx = 1
        for y in range(N):
            for x in range(N):
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 국가가 있고, 연합이 안되어있는지 확인
                    if nx >= 0 and ny >= 0 and nx < N and ny < N and not visited[ny][nx]:
                        # 인구수 차이
                        peoples = abs(map_arr[y][x] - map_arr[ny][nx])
                        # 연합 가능한지 판단
                        if L <= peoples and peoples <= R:
                            # 연합 BFS 진행
                            visited[y][x] = idx
                            find_association(x, y, idx)
                            # 연합 idx 변경
                            idx += 1
                            break

        # 연합 하나도 없으면 ans 반환하고 종료
        if idx == 1:
            return day

        # 연합 이동
        for y in range(N):
            for x in range(N):
                if visited[y][x]:
                    idx = visited[y][x]
                    visited[y][x] = 0
                    association_move(x, y, idx)
        day += 1

# [연합 찾기]
def find_association(sx, sy, idx):
    deq = deque()
    deq.append((sx, sy))
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < N and ny < N and visited[ny][nx] == 0:
                # 인구수 차이
                peoples = abs(map_arr[y][x] - map_arr[ny][nx])
                # 연합 가능한지 판단
                if L <= peoples and peoples <= R:
                    visited[ny][nx] = idx
                    deq.append((nx, ny))

# [연합 이동]
def association_move(sx, sy, idx):
    deq = deque()
    deq.append((sx, sy))
    # 연합 인구 수
    total_peoples = map_arr[sy][sx]
    # 국가 좌표
    countrys = [(sx, sy)]
    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 연합 국가인지 확인
            if nx >= 0 and ny >= 0 and nx < N and ny < N and visited[ny][nx] == idx:
                # 연합국가면 인구 수, 국가 좌표 추가
                visited[ny][nx] = 0
                total_peoples += map_arr[ny][nx]
                countrys.append((nx, ny))
                # 큐에 추가
                deq.append((nx, ny))

    # 연합 인구수 만들어주기
    country_people = total_peoples // len(countrys)
    # 인구 분배
    for mx, my in countrys:
        map_arr[my][mx] = country_people

res = make_association()
print(res)