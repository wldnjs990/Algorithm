# N과 M (3)

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

# [입력]
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

# [출력]
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 
# 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# [문제풀이]
# 중복수열 구하는 문제
# 오름차순으로 공백 띄워서 뽑아야 하니 배열에 담아서 풀어야겠다
# 이제 보니 순열 함수 사용하면 알아서 오름차순이네

def get_perm(lev):
    # 배열 길이만큼 수열 만들면 담아주기
    if lev == M:
        perm_arr.append([*arr])
        return

    # 출력하기 편하게 문자열 형태로 담기
    for str_num in str_num_arr:
        arr.append(str_num)
        get_perm(lev+1)
        arr.pop()
N, M = map(int, input().split())

str_num_arr = [str(i) for i in range(1, N+1)]

arr = []
perm_arr = []
# 순열 실행
get_perm(0)
# 공백 띄워서 한 줄씩 출력해주기
for perm in perm_arr:
    print(" ".join(perm))