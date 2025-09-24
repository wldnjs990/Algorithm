# 숨바꼭질

# 수빈이는 동생과 숨바꼭질을 하고 있다. 
# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
# 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 

# 수빈이는 걷거나 순간이동을 할 수 있다. 
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# [입력]
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# [출력]
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# [문제 풀이]
# BFS 활용하는 문제
# visited 배열 만들고 시작점 부터 -1, +1, *2 케이스를 전부 실행해서 가장 먼저 동생한테 도착했을때 return 해주면 됨
# 최대 거리가 100_000까지인데, 널널하게 200_000으로 잡자

from collections import deque

def BFS():
    deq = deque()
    # 시작 위치 초기화(내 위치, 0초)
    deq.append([N, 0])
    while deq:
        now, time = deq.popleft()
        # 동생한테 도착했으면 걸린 시간 반환
        if now == M:
            return time
        
        # 경로 체크 후 모든 이동경로 돌기
        if now + 1 < 200_000 and not visited[now + 1]:
            visited[now + 1] = True
            deq.append([now+1, time+1])
        if now - 1 < 200_000 and now - 1 >= 0 and not visited[now - 1]:
            visited[now - 1] = True
            deq.append([now-1, time+1])
        if now * 2 < 200_000 and not visited[now*2]:
            visited[now*2] = True
            deq.append([now*2, time+1])

# 나 = N, 동생 = M
N, M = map(int, input().split())
# 최대 10만인데, 널널하게 20만으로 설정
visited = [False] * 200_001

ans = BFS()

print(ans)