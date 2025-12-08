# 차이를 최대로

# 백트래킹 ㄱㄱ

N = int(input())
num_arr = list(map(int, input().split()))
visited = [False] * N

arr = []

ans = 0
def get_max():
  global ans
  now = 0
  for i in range(N-1):
    now += abs(arr[i] - arr[i+1])
  ans = max(ans, now)

def backtracking(lev = 0):
  if lev == N:
    get_max()
    return
  
  for i in range(N):
    if not visited[i]:
      visited[i] = True
      arr.append(num_arr[i])
      backtracking(lev+1)
      visited[i] = False
      arr.pop()

backtracking()

print(ans)