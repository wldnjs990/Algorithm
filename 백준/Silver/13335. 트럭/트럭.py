# 트럭

# 강을 가로지르는 하나의 차선으로 된 다리가 하나 있다.
# 이 다리를 n 개의 트럭이 건너가려고 한다.
# 트럭의 순서는 바꿀 수 없으며, 트럭의 무게는 서로 같지 않을 수 있다.
# 다리 위에는 단지 [w 대의 트럭만 동시에 올라갈 수 있다.]
# 다리의 길이는 w 단위길이(unit distance)이며,
# 각 트럭들은 하나의 단위시간(unit time)에 하나의 단위길이만큼만 이동할 수 있다고 가정한다.
# [동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다. ]
# 참고로, 다리 위에 완전히 올라가지 못한 트럭의 무게는 다리 위의 트럭들의 무게의 합을 계산할 때 포함하지 않는다고 가정한다.

# 다리의 길이와 다리의 최대하중, 그리고 다리를 건너려는 트럭들의 무게가 순서대로 주어졌을 때,
# 모든 트럭이 다리를 건너는 최단시간을 구하는 프로그램을 작성하라.

# [입력]
# 입력 데이터는 표준입력을 사용한다. 입력은 두 줄로 이루어진다.
# 입력의 첫 번째 줄에는 세 개의 정수 n (1 ≤ n ≤ 1,000) , w (1 ≤ w ≤ 100) and L (10 ≤ L ≤ 1,000)이 주어지는데,
# n은 다리를 건너는 트럭의 수, w는 다리의 길이, 그리고 L은 다리의 최대하중을 나타낸다.
# 입력의 두 번째 줄에는 n개의 정수 a1, a2, ⋯ , an (1 ≤ ai ≤ 10)가 주어지는데, ai는 i번째 트럭의 무게를 나타낸다.

# [출력]
# 출력은 표준출력을 사용한다. 모든 트럭들이 다리를 건너는 최단시간을 출력하라.

# [문제풀이]
# 그리디로 못 푼대...
# BFS 써야한대

from collections import deque


# 트럭의 수: n, 다리의 길이: w, 다리의 최대하중: L
n, w, L = map(int, input().split())
# 트럭 무게
trucks = deque(list(map(int, input().split())))
# 트럭들 현재 이동 상황
trucks_moved = deque()
trucks_moved.append(w)
# 현재 다리에 있는 트럭들
bridge_trucks = deque()
bridge_trucks.append(trucks.popleft())
# 현재 다리에 있는 트럭 총 무게
now_weight = bridge_trucks[0]

# 다 빠져나갔을때 경우인 1 추가
time = 0
while trucks:
    # 다리에 있는 트럭 1칸씩 이동
    for i in range(len(trucks_moved)):
        trucks_moved[i] -= 1
    # 맨 앞의 트럭 도착했으면 빼기
    if not trucks_moved[0]:
        trucks_moved.popleft()
        now_weight -= bridge_trucks.popleft()
    # 다음 트럭을 추가 할 수 있는 경우
    if now_weight + trucks[0] <= L:
        # 트럭 추가
        now_weight += trucks[0]
        trucks_moved.append(w)
        bridge_trucks.append(trucks.popleft())
    # 다음 트럭을 추가 할 수 없는 경우
    elif now_weight + trucks[0] > L:
        while now_weight + trucks[0] > L:
            # 선두 트럭 빠질때 까지 이동
            head_truck = bridge_trucks.popleft()
            least_time = trucks_moved.popleft()
            # 선두 트럭 이동시간 추가
            time += least_time
            # 선두 트럭 무게 빼기
            now_weight -= head_truck
            # 나머지 트럭들도 이동 적용
            for i in range(len(trucks_moved)):
                trucks_moved[i] -= least_time
        # 트럭 추가
        now_weight += trucks[0]
        trucks_moved.append(w)
        bridge_trucks.append(trucks.popleft())
    # 결과시간 + 1
    time += 1

# 마지막 트럭 나오는거 추가해서 반환
print(time + trucks_moved.pop() + 1)
