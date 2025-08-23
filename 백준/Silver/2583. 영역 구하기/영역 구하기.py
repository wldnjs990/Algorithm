import sys;
sys.setrecursionlimit(10000)
# dfs로 억지로 푸는거라 파이썬에선 1000개로 걸려있는 스택 제한을 늘려줘야함
# 최대 100 * 100이라 10000번 스택이 쌓일 수 있음
# 영역 구하기

# 눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다.
# 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.


# 첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다.(M, N, K는 모두 100 이하의 자연수이다.)
# 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 
# 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 
# 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다.
# 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다.
# 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다. => 빈 공간이 무조건 1개 이상 나온다.


# 왜 사각형 좌표를 저따구로 설정해놨는지 모르겠는데 0, 0이 왼쪽 아래고, M, N이 오른쪽 위라는걸 알아둬야함
# 사각형 모양 이상하게 만들어지는거 보고 뭐지 이거 했는데 문제 자체가 이상해게 만듬 누가 만들었냐

# 2차원 배열에서 y가 반전된 버전이라고 생각하고 그래프를 만들어야함
# 직사각형 그릴때 y를 M - y로 주면 반전 좌표로 구해질거 같음

# DFS
def DFS(x, y, dx, dy):
    # 현재 영역 넓이 글로벌로 지정
    global width
    # 방문한 지역이면 종료
    if visited[y][x]:
        return
    # 방문 체크
    visited[y][x] = True
    # 넓이 추가
    width += 1
    # 다음 지역 방문
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 다음 위치 검증
        if nx >= 0 and ny >= 0 and nx < N and ny < M and area[ny][nx]:
            DFS(nx, ny, dx, dy)


# 세로, 가로, 직사각형 갯수
M, N, K = map(int, input().split())
# 공간 만들기
area = [[1] * N for _ in range(M)]
# 직사각형들 넣기
for _ in range(K):
    # 직사각형 좌표
    x1, y1, x2, y2 = map(int, input().split())
    # 직사각형 표시
    for y in range(M - y2, M - y1):
        for x in range(x1, x2):
            area[y][x] = 0

# 델타
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# 방문 확인용
visited = [[False] * N for _ in range(M)]


# 결과 영역 넓이
result = []
# 빈 영역 찾기
for y in range(M):
    for x in range(N):
        # 현재 영역이 빈 영역일 경우
        if area[y][x]:
            # 현재 영역 넓이값 초기화
            width = 0
            # 영역 넓이 구하기
            DFS(x, y, dx, dy)
            # 영역 넓이가 0이면 이미 방문했던 영역이니 패스, 0 이상이면 영역이 나온거니 width값 result에 담기
            if width:
                result.append(width)

# 결과 영역 넓이 오름차순 정렬
result.sort()
result_len = len(result)
# 결과 영역 갯수
print(result_len)
# 결과 영역들
for i in range(result_len):
    if i < result_len - 1:
        print(result[i], end=' ')
    else :
        print(result[i])

