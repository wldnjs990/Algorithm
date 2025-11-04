import sys;
input = sys.stdin.readline
# 1 : 38
# 연산자 끼워넣기

# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다
# 사칙연산 없음

# [출력]
# 첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다.

# 백트래킹 진행
def backtracking(lev, res):
    global max_v
    global min_v
    # 연산식 다 썻으면
    if lev == N-1:
        # 처음 도달한 경우
        if max_v == 0 and min_v == 100_000_000:
            # 최대 최소 둘 다 업데이트
            max_v = res
            min_v = res
        else:
            # 최대 최소 업데이트
            max_v = max(max_v, res)
            min_v = min(min_v, res)
        return

    # 연산해야 하는 숫자
    now_num = perm[lev + 1]
    for i in range(4):
        # 연산식 있으면
        if calculator[i]:
            # 연산식 소비
            calculator[i] -= 1
            # 연산시켜서 다음으로 이동
            if i == 0:
                backtracking(lev + 1, res + now_num)
            elif i == 1:
                backtracking(lev + 1, res - now_num)
            elif i == 2:
                backtracking(lev + 1, res * now_num)
            elif i == 3:
                if res >= 0:
                    backtracking(lev + 1, res // now_num)
                else:
                    backtracking(lev + 1, -(abs(res) // now_num))
            # 연산식 원복
            calculator[i] += 1

N = int(input())

# 수열
perm = list(map(int, input().split()))

# + - * /
calculator = list(map(int, input().split()))

max_v = -float('inf')
min_v = float('inf')

backtracking(0, perm[0])

print(max_v)
print(min_v)