# 요리사

# 두 명의 손님에게 음식을 제공하려고 한다.
# 두 명의 손님은 식성이 비슷하기 때문에, 최대한 비슷한 맛의 음식을 만들어 내야 한다.

# N개의 식재료가 있다.

# 식재료들을 각각 N / 2개씩 나누어 두 개의 요리를 하려고 한다. (N은 짝수이다.)
# 이때, 각각의 음식을 A음식, B음식이라고 하자.
# 비슷한 맛의 음식을 만들기 위해서는 A음식과 B음식의 맛의 차이가 최소가 되도록 재료를 배분해야 한다.
# 음식의 맛은 음식을 구성하는 식재료들의 조합에 따라 다르게 된다.

# 식재료 i는 식재료 j와 같이 요리하게 되면 궁합이 잘 맞아 시너지 Sij가 발생한다.
# (1 ≤ i ≤ N, 1 ≤ j ≤ N, i ≠ j)
# 각 음식의 맛은 음식을 구성하는 식재료들로부터 발생하는 시너지 Sij들의 합이다.

# 식재료 i를 식재료 j와 같이 요리하게 되면 발생하는 시너지 Sij의 정보가 주어지고,
# 가지고 있는 식재료를 이용해 A음식과 B음식을 만들 때,
# 두 음식 간의 맛의 차이가 최소가 되는 경우를 찾고 그 최솟값을 정답으로 출력하는 프로그램을 작성하라.

# [제약사항]
# 1. 시간 제한 : 최대 50개 테스트 케이스를 모두 통과하는 데 C / C++ / Java 모두 3초
# 2. 식재료의 수 N은 4이상 16이하의 짝수이다. (4 ≤ N ≤ 16)
# 3. 시너지 Sij는 1이상 20,000이하의 정수이다. (1 ≤ Sij ≤ 20,000, i ≠ j)
# 4. i와 j가 서로 같은 경우의 Sij값은 정의되지 않는다. 입력에서는 0으로 주어진다.

# [입력]
# 입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고,
# 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 식재료의 수 N이 주어진다.
# 다음 N개의 줄에는 N * N개의 시너지 Sij값들이 주어진다. i와 j가 서로 같은 경우는 0으로 주어진다.

# [출력]
# 테스트 케이스 개수만큼 T개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.
# 각 줄은 "#t"로 시작하고 공백을 하나 둔 다음 정답을 출력한다. (t 는 1부터 시작하는 테스트 케이스의 번호이다.)
# 정답은 두 음식 간의 맛의 차이가 최소가 되도록 A음식과 B음식을 만들었을 때 그 차이 값이다.


# [문제풀이]
# 백준 링크와 스타트랑 똑같은 문제인데?
# 복습한다는 느낌으로 또 해보자
# nC(n//2)의 조합들을 구해 팀1을 구한다.
# 팀 1이 구해진 순간, 나머지 맴버들로 팀2는 자동으로 만들어짐
# 만들어진 2팀을 가지고 가지고 또 (팀)C(2) 구한 것들의 좌표에 있는 값들을 더해 음식 점수를 만들고,
# 만들어진 팀1과 팀2의 값의 차이의 절대값을 구해 가장 낮은 값을 반환하면 끝

# 식재료 선택하기
def get_food_comb(idx):
    # 조합이 완성되었을때 식재료 시너지 차이 구하기
    if len(comb_arr) == R:
        get_flavor_diff([*comb_arr])
        return
    if idx == N:
        return

    # 식재료 담기
    comb_arr.append(idx)
    get_food_comb(idx+1)
    # 식재료 담지 않기
    comb_arr.pop()
    get_food_comb(idx+1)

# 식재료 시너지 차이 구하기
def get_flavor_diff(food_arr1):
    global ans
    # 2번째 식재료 조합
    food_arr2 = []
    # 2번째 식재료 조합 담기
    for i in range(N):
        if i not in food_arr1:
            food_arr2.append(i)

    # 음식 총 시너지 구하기
    food1 = food_synergy(0, [*food_arr1])
    food2 = food_synergy(0, [*food_arr2])
    food_diff = abs(food1 - food2)
    # 시너지 차이가 ans보다 작으면 값 업데이트
    if ans > food_diff:
        ans = food_diff

# 음식 시너지 구하기
def food_synergy(idx, arr):
    res1 = 0
    res2 = 0
    if len(synergy) == 2:
        return foods_arr[synergy[0]][synergy[1]] + foods_arr[synergy[1]][synergy[0]]

    if idx == R:
        return 0

    synergy.append(arr[idx])
    res1 += food_synergy(idx + 1, arr)
    synergy.pop()
    res2 += food_synergy(idx + 1, arr)

    return res1 + res2

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    foods_arr = [list(map(int, input().split())) for _ in range(N)]

    # 식재료 나누기용 R
    R = N // 2

    # 식재료 담은 배열1
    comb_arr = []

    # 시너지 배열
    synergy = []

    # 결과
    ans = 100_000_000

    # 실행
    get_food_comb(0)

    print(f'#{tc} {ans}')

