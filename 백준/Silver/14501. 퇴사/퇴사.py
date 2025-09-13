# 퇴사

# 백준이는 퇴사를 하려고 한다.
# 오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.
# 백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.
# 각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

# 상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다.
# 예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다.
# 2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.
# 또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.

# 퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.
# 상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

# [입력]
# 첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
# 둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

# [출력]
# 첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.

# [문제 풀이]
# 일을 한다, 안한다로 상태변환 트리 만드니깐 일을 하고있냐에 따라 가지를 칠 수 있음
# 백트래킹으로 풀면 되는 문제인듯

# 가지치기 조건
# 1. 일을 하고 있다면 일을 받는 재귀 가지치기
# 2. 현재 남아있는 일 양이 남은 일 수 보다 큰 경우 가지치기

# 그리고 N일이 지났을때, 아직 일이 남아있으면 실패한거임
# 최대값이라서 돈의 총 합을 대상으로 가지치기는 못 함

# 현재 일 수, 일하고 있는 시간, 총 번 돈
def back_tracking(now_day, working, total_earn):
    global max_money

    # 현재 남아있는 일 양이 남은 일 수 보다 큰 경우 가지치기
    if now_day + working > N:
        return

    # N일에 도달했고, 일이 남아있지 않은 경우
    if now_day == N and working == 0:
        # 최대로 벌 수 있는 돈 계산하고 종료
        max_money = max(max_money, total_earn)
        return

    # 일을 하고 있지 않은 상태면 일 수락 / 거절 가능
    if working == 0:
        work_day = work_list[now_day][0]
        work_earn = work_list[now_day][1]
        back_tracking(now_day + 1, working + work_day - 1, total_earn + work_earn)
        # 일 안하고 넘어가기
        back_tracking(now_day + 1, working, total_earn)
    # 일 하고 있으면 working만 감소해주기
    else:
        back_tracking(now_day + 1, working - 1, total_earn)
    


N = int(input())
work_list = [list(map(int, input().split())) for _ in range(N)]

# 결과값
max_money = 0

# 백트래킹 실행
back_tracking(0, 0, 0)

print(max_money)