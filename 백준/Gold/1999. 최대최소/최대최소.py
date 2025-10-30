N, B, K = map(int, input().split())
num_arr = [list(map(int, input().split())) for _ in range(N)]
ans_arr = [[0]*(N-B+1) for _ in range(N-B+1)]
for i in range(N-B+1):
    for j in range(N-B+1):
        min_value = 250
        max_value = 0
        for k in range(B):
            for l in range(B):
                min_value = min(min_value, num_arr[i+k][j+l])
                max_value = max(max_value, num_arr[i+k][j+l])
        ans_arr[i][j] = max_value - min_value
for _ in range(K):
    y, x = map(int, input().split())
    print(ans_arr[y-1][x-1])