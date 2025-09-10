# 이진탐색
 
# 서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다
# 그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다.
 
# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 A와 B에 속한 정수의 개수 N, M이 주어지고,
# 두 줄에 걸쳐 N개와 M개의 백만 이하의 양의 정수가 주어진다.
# 1<=N, M<=500,000
 
# 무슨 양쪽 구간을 번갈아 선택하는 숫자만 담으래
 
from collections import deque
 
# 이분탐색
def binary_search(l, r, target, now):
    # now default = -1 / 왼쪽 : 0, 오른쪽 : 1
    deq = deque()
    deq.append([l, r, target, now])
    st_mid = (l+r) // 2
    # 첫번째 중앙이 target이면 1 반환
    if arr[st_mid] == target:
        return 1
 
    while deq:
        l, r, target, now = deq.popleft()
        # 왼쪽 좌표가 오른쪽 좌표 넘어가면 탐색 종료하고 0 반환
        if l > r:
            return 0
        # 현재 위치의 중앙 좌표
        mid = (l + r) // 2
        # 중앙값
        mid_val = arr[mid]
        # 중앙값이 target이 맞다면 1 반환
        if mid_val == target:
            return 1
 
        # target값이 더 크다면 중앙 기준 오른쪽 좌표로 이동
        elif mid_val < target:
            # 아직 방향 안 잡혀있으면 오른쪽 설정
            if now == -1:
                deq.append([mid + 1, r, target, 1])
            # 방향 잡혔으면 왼쪽인지 검증하고, 맞으면 오른쪽으로 이동
            elif not now:
                deq.append([mid + 1, r, target, 1])
            # 아니면 종료
            else :
                return 0
        # target값이 더 작다면 중앙 기준 왼쪽 좌표로 이동
        elif mid_val > target:
            # 아직 방향 안 잡혀있으면 왼쪽 설정
            if now == -1:
                deq.append([l, mid - 1, target, 0])
            # 방향 잡혔으면 오른쪽인지 검증하고, 맞으면 왼쪽으로 이동
            elif now:
                deq.append([l, mid - 1, target, 0])
            # 아니면 종료
            else :
                return 0
 
T = int(input())
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 정수 배열
    arr = list(map(int, input().split()))
    # 찾아야 하는 정수들
    find_arr = list(map(int, input().split()))
 
    # 정렬을 하라는거야 정렬된걸 준다는거야..
    arr.sort()
 
    ans = 0
 
    for find in find_arr:
        ans += binary_search(0, N-1, find, -1)
 
    print(f'#{tc} {ans}')