import sys;
input = sys.stdin.readline

# 정민이의 수열 재조합

# 정민이는 1부터 N까지 한 개씩 들어있는 수열을 만드는 것을 목표로 한다. 
# 이를 위해 최소 개수의 양의 정수가 들어있는 수열을 준비했고, 목표를 달성할 때까지 다음 작업들을 반복했다.

# 수열에 있는 한 정수를 제곱한 수를 수열에 추가한다.
# 수열에 있는 두 정수를 곱한 수를 수열에 추가한다.

# 익준이는 모든 작업을 마친 정민이를 보고 어떤 정수들을 가지고 처음 작업을 시작했는지 물었다. 
# 그러자 정민이는 답을 알려주는 대신 익준이가 a와 b를 물어보면 초기 정수 중 a 이상 b 이하인 정수들의 개수를 알려 주겠다고 했다. 
# 익준이는 질문을 총 M번 할 것이다.
# 익준이의 질문에 답을 해주자.

# [입력]
# 첫 번째 줄에 정수 N,M이 공백으로 구분되어 주어진다.(1 <= N <= 5,000,000, 1 <= M <= 1,000,000)
# 두 번째 줄부터 M개의 줄에 정수 a,b가 공백으로 구분되어 주어진다. (1 <= a <= b <= N)

# [문제 풀이]
# 소수 구하는거네
# 1, 2, 3 ,5, 7, 11, 13 ...
# 제곱은 어떻게 거르지?

N, M = map(int, input().split())

no = [False for _ in range(N+1)]
sosu_cnt = [0 for _ in range(N+1)]
# 에라토스테네스 채로 소수 외에 거르는 배열 만들기
for i in range(1, int((N+1)**0.5)+1):
  if i == 1 : 
    continue
  if not no[i]:
    check = i * 2
    while check <= N:
      no[check] = True
      check += i

cnt = 0
for i in range(1, N+1):
  if not no[i]:
    cnt += 1
  sosu_cnt[i] = cnt

for _ in range(M):
  s, e = map(int, input().split())
  # 소수 범위 담기
  print(sosu_cnt[e] - sosu_cnt[s-1])

