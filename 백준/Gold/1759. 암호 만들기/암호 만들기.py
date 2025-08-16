# 암호 만들기

# 암호는 서로 다른 L개의 알파벳 소문자들로 구성
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
# 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것
# => abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.
# 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다
# C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

# 이것도 부분집합 구해서 L자리수일때를 기준으로 구하면 되지 않을까?
# 일단 부분집합을 전부 다 구하기 때문에 시간복잡도는 완탐이긴 한데, 일단 최대 2^15면 가능은 할 거 같은데
# 0. 배열 정렬 하기
# 1. 부분집합을 전부 구하면서, 길이가 L인 경우만 따로 배열에 추가하기
# 2. 모음 수를 전부 구해 1개 이상인지 먼저 확인하고, 나머지 글자 수가 2개를 넘는지 확인해야함


L, C = map(int, input().split())
# 배열 받기
str_list = list(input().split())
# 배열 정렬
str_list.sort()
# L 길이의 배열 담을 리스트
L_len_list = []

for i in range(1<<C):
    # 현재 담을 문자열
    now = []
    for j in range(C):
        if i & 1<<j:
            now.append(str_list[j])
    if len(now) == L:
        L_len_list.append(now)

result = []

for i in range(len(L_len_list)):
    # 모음 체크
    ctn = 0
    for j in range(L):
        # 현재 글자
        word = L_len_list[i][j]
        if word == 'a' or word == 'i' or word == 'o' or word == 'u' or word == 'e':
            ctn += 1
    # 모음 1개 이상, 자음 2개 이상인 경우 result에 추가
    if ctn >=1 and L - ctn >= 2:
        result.append(L_len_list[i])
    
# 사전순 정렬
result.sort()

for res in result:
    print(''.join(res))
