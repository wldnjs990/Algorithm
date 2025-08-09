# 지구온난화
# 지도에 X는 땅이고, .은 바다
# X상하좌우에 .이 3개 이상이면 그 땅은 제거되는 문제
# 땅이 제거되는걸 다른 특수기호로 바꾸자 X => #
# 왜냐하면 바다로 바꾸면 다른 섬이 잠기는 상황에 영향을 줄 수 있기 때문(.이 2개 인접해있고, 바로옆에 #이 있는 섬이 바로옆에 #가 .으로 바뀌면서 변할수도 있음)
# 바꾼 다음에 2중 for문을 돌려 행과 열을 각각 조사해 땅이 없는 행이나 열을 아예 제거하면 끝일듯

# 다 푼 소감 : 아 겁나 길고 복잡하네

R, C = map(int, input().split())

island_map = [list(input()) for _ in range(R)]

# 델타
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 잠길 섬 찾기
for y in range(R):
    for x in range(C):
        # 현재 좌표가 섬일 경우 실행
        if island_map[y][x] == 'X':
            # 현재 섬 주위에 바다가 몇 개인지 측정하기 위한 변수
            sea = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                # 현재 좌표가 지도를 벗어나는지 체크
                if ny >= 0 and ny < R and nx >= 0 and nx < C:
                    if island_map[ny][nx] == '.':
                        sea += 1
                # 지도를 벗어나는 곳은 전부 바다라고 했으니 sea 카운트 추가
                else :
                    sea += 1
                # 바다가 3개 이상 인접하면 곧 잠기는 섬 #로 변경
                if sea >= 3:
                    island_map[y][x] = '#'

# 끝 부분 바다면 지우기 - 행
row_start_sea = True
row_end_sea = True
# 바다를 더 지울 필요 없어질때 까지 반복문
while row_start_sea or row_end_sea:
    # 현재 바다 행 길이
    row_len = len(island_map)
    # 시작 바다 삭제
    if row_start_sea:
        isDel = True
        for x in range(C):
            if island_map[0][x] == 'X':
                isDel = False
                break
        # 삭제 대상이면 배열 지우고 현재 행 길이 1 차감(끝 부분 삭제 구할때 길이를 업데이트 해줘야 해서)
        if isDel:
            island_map.pop(0)
            row_len -= 1
        else:
            row_start_sea = False
    # 끝 바다 삭제
    if row_end_sea:
        isDel = True
        for x in range(C):
            if island_map[row_len - 1][x] == 'X':
                isDel = False
                break
        if isDel:
            island_map.pop()
        else:
            row_end_sea = False


# 끝 부분 바다면 지우기 - 열
col_start_sea = True
col_end_sea = True
col_start = 0
col_end = C - 1
# 바다를 더 지울 필요 없어질때 까지 반복문
while col_start_sea or col_end_sea:
    # 시작 바다 삭제
    if col_start_sea:
        isDel = True
        for y in range(row_len):
            if island_map[y][col_start] == 'X':
                isDel = False
                break
        if isDel:
            # 행처럼 pop으로 제거할 수 없으니 죽은영역 -로 만들어주고 뒤에 처리
            for y in range(row_len):
                island_map[y][col_start] = '-'
            # 다음 열로 넘어가기
            col_start += 1
        else:
            col_start_sea = False
    # 끝 바다 삭제
    if col_end_sea:
        isDel = True
        for y in range(row_len):
            if island_map[y][col_end] == 'X':
                isDel = False
                break
        if isDel:
            for y in range(row_len):
                island_map[y][col_end] = '-'
            # 다음 열로 넘어가기
            col_end -= 1
        else:
            col_end_sea = False


# 결과 담을 배열
result = []
for y in range(len(island_map)):
    result_row = []
    # 죽은 지역 아니면 result_row에 담기
    for island in island_map[y]:
        if island != '-':
            if island == '#':
                result_row.append('.')
            else :
                result_row.append(island)
    # 필터링 한 result_row result에 넣어주기
    result.append(result_row)


# 결과 반환
for y in range(len(result)):
    print(''.join(result[y]))