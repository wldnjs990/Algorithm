# 바이러스

# 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

# 첫째줄엔 컴퓨터의 수 : 1 <= N <= 100
# 둘째줄엔 연결되어있는 컴퓨터 쌍의 수 M
# 그 다음줄 부터 컴퓨터의 수 만큼 컴퓨터 번호 쌍 A, B

# 연결 리스트 만들고 BFS로 카운트 세면서 풀기
# 카운트 셀 필요가 없네
# 그냥 visited된 갯수만 구하면 끝이네 1번 컴퓨터 빼야하니깐 -1 하면 끝

# 근데 이건 DFS가 더 맞는 문제인거 같은데..?

# BFS
def BFS(start):
    queue = [start]

    while queue:
        now = queue.pop(0)
        
        # 방문 체크
        virused[now] = True

        # 현재 컴퓨터와 연결되어있는 다음 지역들 검증
        next_step = computer_link[now]
        for step in next_step:
            # 다음 컴퓨터가 바이러스 걸리지 않았으면 이동
            if not virused[step]:
                queue.append(step)


N = int(input())
M = int(input())

# 연결 리스트
computer_link = [[] for _ in range(N)]
# 바이러스 여부
virused = [False for _ in range(N)]

# 연결 리스트 만들기
for _ in range(M):
    # 연결되어있는 컴퓨터 쌍(양방향)
    a, b = map(int, input().split())
    A = a-1
    B = b-1
    # 양방향으로 연결
    computer_link[A].append(B)
    computer_link[B].append(A)

# 대충 BFS에서 나오는 ctn 최댓값이 답이지 않을까
result = -1
# 아 0번이 1이지
BFS(0)

# result 구하기
for virus in virused:
    if virus:
        result += 1

# 1번 컴퓨터 빼고 결과 출력
print(result)

    
