# 뿌요뿌요

# 뿌요뿌요의 룰은 다음과 같다.

# 필드에 여러 가지 색깔의 뿌요를 놓는다.
# 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다.
# 뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다.
# 뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.
# 아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다.
# 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.

# 상대방의 필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날지 계산하기

# [입력]
# 총 12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개의 문자가 있다.
# 이때 .은 빈공간이고 .이 아닌것은 각각의 색깔의 뿌요를 나타낸다.
# R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.
# 입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태이다. 즉, 뿌요 아래에 빈 칸이 있는 경우는 없다.

# [출력]
# 현재 주어진 상황에서 몇연쇄가 되는지 출력한다. 하나도 터지지 않는다면 0을 출력한다.

# [풀이]
# 뿌요가 터지는 경우를 flag로 지정해서 flag가 false가 되기 전 까지 무한반복하기
# 1. 색깔 블럭 나오면 BFS 실행해서 4칸 이상인지 검증하고 맞다면 블럭 제거
# 2. 블럭이 1번이라도 깨졌으면 연쇄 추가하고, 아니면 반복문 종료
# 3. 블럭이 깨졌다면 열 마다 아래에서 위로 올라가면서 마지막 .의 좌표를 기억하고 그 위에 블럭이 있으면 위치값 교체하면서 블럭 업데이트 하기

# 동일한 색깔이 4칸 이상인 블럭 찾아서 부수기
def destroy_block(start, color):
    # 큐
    queue = [start]
    # 동일한 색깔일 경우에 체크하고, 4개 이상일 경우 .으로 바꿀 좌표 저장용 checked 배열 만들기
    checked = [[False] * 6 for _ in range(12)]
    # 델타
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 큐가 빌 때 까지 진행
    while queue:
        # 좌표 빼기
        x, y = queue.pop(0)
        # 방문 체크
        visited[y][x] = True
        # 동일블럭 체크
        checked[y][x] = True

        # 다음 블럭 있는지 확인 후 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 검증하기
            # 좌표에서 벗어나지 않았는지, 다음 블럭이 동일한 색깔의 블럭인지, 아직 방문하지 않은 지역인지
            if nx >= 0 and ny >= 0 and nx < 6 and ny < 12 and game[ny][nx] == color and not visited[ny][nx]:
                queue.append([nx, ny])
    
    # 동일 블럭이 4개 이상인지 확인할 변수
    checked_cnt = 0
    # 동일 블럭 갯수 체크
    for y in range(12):
        for x in range(6):
            # checked된 블럭이면 +1 하기
            if checked[y][x]:
                checked_cnt += 1

    # checked_ctn이 4개 이상이면 블럭들 전부 .으로 교체
    if checked_cnt >= 4:
        for y in range(12):
            for x in range(6):
                # checked된 블럭이면 블럭 파괴
                if checked[y][x]:
                    game[y][x] = '.'
        # 뿌요되었다는 결과 반환
        return True
    # 아니라면 뿌요되지 않았다는 결과 반환
    else:
        return False

# 블럭 깬 후에 블럭 중력으로 내리기
def down_block():
    # 새로로 끝에서 부터 위로 올라오는 반복문 진행
    for x in range(6 - 1, -1, -1):
        # . 최초 위치 point_at
        point_at = -1
        for y in range(12 - 1, -1, -1):
            # .을 발견하고, 최초 위치가 아직 등록되지 않은 경우 최초 위치 등록
            if game[y][x] == '.' and point_at == -1:
                point_at = y
            # 블럭을 발견하고 point_at의 좌표가 있는 상태에서 서로 위치 교환하고, .의 위치 -1 하기(-1이 올리는거임)
            if game[y][x] != '.' and point_at != -1:
                game[y][x], game[point_at][x] = game[point_at][x], game[y][x]
                point_at -= 1

# 게임판
game = [list(input()) for _ in range(12)]
# 연쇄 카운트(결과)
chain = 0

# 뿌요가 발생 안한 순간까지 while문 진행
while True:
    # 블럭 방문 여부
    visited = [[False] * 6 for _ in range(12)]
    # 한번이라도 뿌요되었음 여부
    is_puyo = False
    # 블럭 발견시 파괴 BFS 실행
    for y in range(12):
        for x in range(6):
            # .이 아니고, 방문한 블럭이 아닌 경우에 실행
            if game[y][x] != '.' and not visited[y][x]:
                # 블럭 4칸 이상인지 검증 후 파괴(현재 블럭 좌표, 블럭의 색깔)
                # 뿌요됐다면 True 반환, 안됐으면 False 반환
                success = destroy_block([x, y], game[y][x])
                # 뿌요 되었으면 뿌요되었음으로 바꾸기
                if success:
                    is_puyo = True

    # 한번이라도 뿌요 되었다면 chain 추가하고 블럭 내리기 진행
    if is_puyo:
        chain += 1
        down_block()
    # 아니면 while문 종료
    else:
        break

# 결과 출력
print(chain)