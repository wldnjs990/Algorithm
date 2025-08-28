# 숨바꼭질

# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고
# 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

N, K = map(int, input().split())

# 현재위치 - 1
# 현재위치 + 1
# 현재위치 * 2
# 이 3가지 캐이스들 전부 반복하면서 동생 위치를 넘어가지 않는 선에서 도착 카운트 구하기
# 이건 최단거리 구하기라서 BFS 맞네

# 방문여부
visited = [False for _ in range(K)]

def BFS(start):
    global time
    queue = [start]
    while queue:
        now, ctn = queue.pop(0)

        # 거리가 0보다 작아지면 종료
        if now < 0:
            continue
        # 동생보다 더 앞서갔으면 나머지 거리 계산 후 time 비교해서 time 업데이트 하고 종료
        if now > K:
            if time > ctn + (now - K):
                time = ctn + (now - K)
            continue
        # 동생한테 도착하면 종료
        if now == K:
            if time > ctn:
                time = ctn
            continue

        # 방문한 지역이면 이동 중단
        if visited[now - 1]:
            continue
        # 방문 체크
        visited[now - 1] = True

        # 뒤로
        queue.append([now - 1, ctn + 1])
        # 앞으로
        queue.append([now + 1, ctn + 1])
        # 순간이동
        queue.append([now * 2, ctn + 1])

# 최단시간 구하기
time = 100_000_000
BFS([N, 0])

print(time)