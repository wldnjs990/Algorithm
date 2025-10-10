# 거짓말

# 지민이는 파티에 가서 이야기 하는 것을 좋아한다.
# 파티에 갈 때마다, 지민이는 지민이가 가장 좋아하는 이야기를 한다.
# 지민이는 그 이야기를 말할 때, 있는 그대로 진실로 말하거나 엄청나게 과장해서 말한다.
# 당연히 과장해서 이야기하는 것이 훨씬 더 재미있기 때문에, 되도록이면 과장해서 이야기하려고 한다.
# 하지만, 지민이는 거짓말쟁이로 알려지기는 싫어한다.
# 문제는 몇몇 사람들은 그 이야기의 진실을 안다는 것이다.
# 따라서 이런 사람들이 파티에 왔을 때는, 지민이는 진실을 이야기할 수 밖에 없다.
# 당연히, 어떤 사람이 어떤 파티에서는 진실을 듣고, 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다.
# 지민이는 이런 일을 모두 피해야 한다.

# 사람의 수 N이 주어진다.
# 그리고 그 이야기의 진실을 아는 사람이 주어진다.
# 그리고 각 파티에 오는 사람들의 번호가 주어진다.
# 지민이는 모든 파티에 참가해야 한다.
# 이때, 지민이가 거짓말쟁이로 알려지지 않으면서,
# 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 프로그램을 작성하시오.

# [입력]
# 첫째 줄에 사람의 수 N과 파티의 수 M이 주어진다.
# 둘째 줄에는 이야기의 진실을 아는 사람의 수와 번호가 주어진다.
# 진실을 아는 사람의 수가 먼저 주어지고 그 개수만큼 사람들의 번호가 주어진다.
# 사람들의 번호는 1부터 N까지의 수로 주어진다.
# 셋째 줄부터 M개의 줄에는 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다.
# N, M은 50 이하의 자연수이고, 진실을 아는 사람의 수는 0 이상 50 이하의 정수, 각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수이다.

# [출력]
# 첫째 줄에 문제의 정답을 출력한다.

# [문제 풀이]
# 백트레킹 해볼까
from collections import deque

def dfs(level, lie):
    global max_lie

    if level == M:
        if max_lie < lie:
            max_lie = lie
        return

    now_member = party_member[level]
    num = now_member[0]+1

    can_lie = True
    for i in range(1, num):
        memb = now_member[i]
        if member_dict[memb] == 1:
            can_lie = False
            break
    if can_lie:
        # 원복용
        before_arr = []
        for i in range(1, num):
            memb = now_member[i]
            before_arr.append(member_dict[memb])
            member_dict[memb] = 2
        dfs(level+1, lie+1)
        # 원복
        for i in range(1, num):
            memb = now_member[i]
            member_dict[memb] = before_arr[i-1]
        # 진실 말하기
        can_true = True
        for i in range(1, num):
            memb = now_member[i]
            if member_dict[memb] == 2:
                can_true = False
                break
        if can_true:
            # 원복용
            before_arr = []
            for i in range(1, num):
                memb = now_member[i]
                before_arr.append(member_dict[memb])
                member_dict[memb] = 1
            dfs(level + 1, lie)
            # 원복
            for i in range(1, num):
                memb = now_member[i]
                member_dict[memb] = before_arr[i - 1]
        else:
            return
    else:
        can_true = True
        for i in range(1, num):
            memb = now_member[i]
            if member_dict[memb] == 2:
                can_true = False
                break
        if can_true:
            # 원복용
            before_arr = []
            for i in range(1, num):
                memb = now_member[i]
                before_arr.append(member_dict[memb])
                member_dict[memb] = 1
            dfs(level + 1, lie)
            # 원복
            for i in range(1, num):
                memb = now_member[i]
                member_dict[memb] = before_arr[i - 1]
        else:
            return



N, M = map(int, input().split())

know_true = deque(map(int, input().split()))
know_cnt = know_true.popleft()

party_member = [list(map(int, input().split())) for _ in range(M)]

# 파티맴버 dict
member_dict = {}
for i in range(1, N+1):
    member_dict[i] = 0
# 파티맴버 dict 채우기
for know in know_true:
    member_dict[know] = 1

max_lie = 0
dfs(0, 0)
print(max_lie)

