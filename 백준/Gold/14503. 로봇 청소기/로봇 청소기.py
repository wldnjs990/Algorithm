import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
X, Y, D = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
clean = [[False] * M for _ in range(N)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ctn = 0
while True:
    if room[X][Y] == 0 and clean[X][Y] == False:
        ctn += 1
        clean[X][Y] = True
    find = False
    for i in range(4):
        ex, ey = X + dx[i], Y + dy[i]
        if room[ex][ey] == 0 and clean[ex][ey] == False:
            find = True
            break
    if find:
        D = (D - 1) % 4
        ex, ey = X + dx[D], Y + dy[D]
        if room[ex][ey] == 0 and clean[ex][ey] == False:
            X = ex
            Y = ey
    else:
        ex, ey = X - dx[D], Y - dy[D]
        if room[ex][ey] == 0:
            X = ex
            Y = ey
        else:
            break
        

print(ctn)