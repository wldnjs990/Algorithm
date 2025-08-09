# 거북이 문제 풀이
# 일단 파이썬으로 풀고 주말에 자바로 수정하겠슴돠

# 0을 기준으로 상하좌우 기록
# 상하 / 좌우로 양수 중에 가장 큰 값, 음수중에 가장 큰 값을 각각 구함
# (상 + 하) * (좌 * 우) 하면 답 나올거 같음
# 둘 중 하나라도 값이 0이면 사각형이 만들어지지 않으니 0이 나올거임

T = int(input())

for tc in range(T):
    controler = list(map(str, input()))

    # +y = 0, +x = 1, -y = 2, -x = 3
    now_dir = 0
    # 컨트롤
    dir_arr = [[1, 1], [0, 1], [1, -1], [0, -1]]
    # 최대/최소 x,y좌표
    b_x = 0
    s_x = 0
    b_y = 0
    s_y = 0
    # 현재 좌표
    coordinate = [0, 0]
    
    for control in controler:
        if control == 'L':
            # -1을 자동처리 하는건 떠오르지가 않네..
            now_dir -= 1
            if now_dir < 0:
                now_dir = 3
        elif control == 'R':
            # 3의 나머지를 구하는 로직을 넣으면 4 이상으로 넘어가지 않고 정상적인 순서로 진행이 됨
            now_dir = (now_dir + 1) % 4
        elif control == 'F':
            coordinate[dir_arr[now_dir][0]] += dir_arr[now_dir][1]
        elif control == 'B':
            coordinate[dir_arr[now_dir][0]] -= dir_arr[now_dir][1]
        # 현재 위치가 고점일 경우 고점 업데이트
        if coordinate[0] > b_x :
            b_x = coordinate[0]
        if coordinate[0] < s_x :
            s_x = coordinate[0]
        if coordinate[1] > b_y :
            b_y = coordinate[1]
        if coordinate[1] < s_y :
            s_y = coordinate[1]
        
    
    # 길이 구하는 법 => 양의 좌표 + 음의 좌표
    row = b_x - s_x
    col = b_y - s_y

    print(row * col)