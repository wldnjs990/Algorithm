# 병합 정렬

# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.
# 5<=N<=1,000,000, 0 <= ai <= 1,000,000

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,
# N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력한다.

# 병합 정렬
def combine_sort(arr, N):
    global left_bigger
    # 최소단위로 쪼개졌으면 뒤로가기
    if len(arr) == 1:
        return arr

    # 왼쪽, 오른쪽 나누기
    mid = N//2
    l_arr = arr[0:mid]
    r_arr = arr[mid:N]

    # 아니면 왼쪽, 오른쪽으로 쪼개기
    left = combine_sort(l_arr, len(l_arr))
    right = combine_sort(r_arr, len(r_arr))

    # 쪼갠거 정렬해서 합친 배열
    combine_arr = []

    # 쪼갠것들 합쳐서 새 배열로 만들어주기(투 포인터 이용)
    # 왼쪽점
    left_idx = 0
    # 오른쪽점
    right_idx = 0
    # 둘 중 하나의 포인터를 다 쓸때까지 진행
    while left_idx < len(left) and right_idx < len(right):
        left_now = left[left_idx]
        right_now = right[right_idx]
        if left_now > right_now:
            combine_arr.append(right_now)
            right_idx += 1
        elif left_now < right_now:
            combine_arr.append(left_now)
            left_idx += 1
        # 같으면 둘 다 한번에 넣기
        elif left_now == right_now:
            combine_arr.append(right_now)
            combine_arr.append(left_now)
            left_idx += 1
            right_idx += 1

    # 둘 다 동일하게 끝났으면 바로 출력
    if left_idx == len(left) and right_idx == len(right):
        return combine_arr
    # 왼쪽점을 다 찾은거면 오른쪽 남은거 채워주기
    elif left_idx == len(left):
        for i in range(right_idx, len(right)):
            combine_arr.append(right[i])
    # 오른쪽점을 다 찾은거면 왼쪽 남은거 채워주기
    elif right_idx == len(right):
        # 여기서 왼쪽 끝점이 오른쪽 끝점보다 더 큰 값인지 확인 후, 크면 경우의 수 1 추가
        # 이게 문제였네 => 문제가 좀 말을 이상하게 함;;
        # 조건에선 "왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다."라고 하고
        # 출력조건에선 "오른쪽 원소가 먼저 복사되는 경우의 수를 출력한다." 이러는데
        # 뭘 들어야 할 지 헷갈려;;
        if left[-1] > right[-1]:
            left_bigger += 1
        for i in range(left_idx, len(left)):
            combine_arr.append(left[i])

    # 재조합한 정렬 반환하기
    return combine_arr


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    # 왼쪽 배열의 마지막 원소가 오른쪽 배열 마지막 원소보다 큰 경우의 수를 담을 배열
    left_bigger = 0

    # 퀵 정렬 실행
    sorted_arr = combine_sort(arr, n)

    print(f'#{tc} {sorted_arr[n//2]} {left_bigger}')