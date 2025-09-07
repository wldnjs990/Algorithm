# 스타트와 링크

# 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 
# 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

# 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다.
# 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다.
# 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. 
# Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

# [입력]
# 첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다.
# 둘째 줄부터 N개의 줄에 S가 주어진다.
# 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다.
# Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

# [출력]
# 첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

# [문제풀이]
# 문제 느낌이 조합이네
# (n)C(n//2)을 먼저 구해서 팀을 2팀으로 먼저 만들어줌
# 그 2팀에서 (n//2)C(2)로 조합들을 나눠줘서 조합의 값을 다 더해주고, 그 차이를 절대값으로 구해주기
# 구한 절대값을 현재 최솟값과 비교하면서, 가장 낮은 차이를 구하면 됨
# 만약 0이 나온다면 바로 0 출력하면 됨


# 매칭 만들기 조합
def matching_comb(now):
    if now > N:
        return
    # 조합 완성됐으면 추가하고 종료
    if len(team1) == matching_member:
        team2 = []
        # 나머지 맴버들 team2에 담기
        for member in range(1, N+1):
            if member not in team1:
                team2.append(member)
        matching.append([[*team1], team2])
        return

    # 재귀
    team1.append(now)
    matching_comb(now + 1)
    team1.pop()
    matching_comb(now + 1)

def get_synergy_diff(idx):
    global t1_synergy
    global t2_synergy
    
    # 2명 구했을때 시너지 점수 합산하기
    if len(t1_duo) == 2:
        t1_synergy += team_synergy[t1_duo[0] - 1][t1_duo[1] - 1]
        t1_synergy += team_synergy[t1_duo[1] - 1][t1_duo[0] - 1]
        t2_synergy += team_synergy[t2_duo[0] - 1][t2_duo[1] - 1]
        t2_synergy += team_synergy[t2_duo[1] - 1][t2_duo[0] - 1]
        return
    
    # 인덱스가 맴버 길이를 벗어났을때 중단
    if idx == matching_member:
        return
    
    # 시너지 조합 만들기
    t1_duo.append(t1[idx])
    t2_duo.append(t2[idx])
    get_synergy_diff(idx + 1)
    t1_duo.pop()
    t2_duo.pop()
    get_synergy_diff(idx + 1)

    
    

# 인원 수
N = int(input())

# 팀 조합 배열
team_synergy = [list(map(int, input().split())) for _ in range(N)]

# 팀 매칭 만들기 -----------------
# 매칭 담을 배열
matching = []
# 팀 1
team1 = []
# 팀 1개 맴버 수
matching_member = N // 2
# 팀 매칭 채우기
matching_comb(1)

# 팀 시너지 차이 구하기 ----------------
min_synergy = 100_000_000
for match in matching:
    # 1팀, 2팀
    t1, t2 = match
    # 시너지 듀오들 담을 배열
    t1_duo = []
    t2_duo = []
    # 시너지 합계 점수
    t1_synergy = 0
    t2_synergy = 0
    # 1팀, 2팀 합계 점수 구하기
    get_synergy_diff(0)

    # 점수 차이 구하기
    synergy_diff = abs(t1_synergy - t2_synergy)
    # 점수 차이가 0이면 반복문 중단
    if synergy_diff == 0:
        min_synergy = 0
        break
    # 점수 차이가 현재까지의 최소 차이보다 작다면 값 업데이트
    elif min_synergy > synergy_diff:
        min_synergy = synergy_diff

print(min_synergy)