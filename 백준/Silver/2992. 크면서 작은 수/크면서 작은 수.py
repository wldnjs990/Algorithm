# 크면서 작은 수
# 같은 글자 조합을 가지고 있으면서, 현재값 보단 큰 수 중에서 가장 작은 값을 구하는 문제
# 이건 조합 구현하는 방법을 한번 찾아보는게 좋을듯
# 4글자라고 하면 4C4를 전부 구하고 거기서 반복문을 돌려 기존값 보다 큰 바로 다음 값을 구하면 되는 문제
# 조합 공식이 뭐징

# 정수 X 받기((리스트로 받을게유)
X = input()

# 정수 X로 만들수 있는 조합 담는 배열
combination = []

# X의 문자 조합들 구하기
# 뭔가 잘못된거 같아 조합의 수가 너무 많이 나와
# 27711이 중복된 숫자들이 있어서 그런진 모르겠는데 중복된 결과들이 너무 많이 나오는데 이게 제대로 된 조합들인지, 아니면 조합이 중복으로 생성되는건지 모르겠네
def get_comb(X, now_idx, word, length, visited):
    # 이미 사용된 인덱스면 중단
    if not visited[now_idx]:
        return

    # 사용여부 체크
    visited[now_idx] = False

    # 문자 추가
    word += X[now_idx]
    
    # 길이가 X만큼인 문자열이 완성되었으면 combination에 추가
    if length == len(X):
        combination.append(word)
        return
    
    # 지금 문자 빼고 문자 싹 다 집어넣기
    for next_idx in range(len(X)):
        if next_idx != now_idx:
            # visited 참조를 다르게 사용해야 하니 스프레드 연산자 써서 얕은복사
            get_comb(X, next_idx, word, length + 1, [*visited])

# combination에서 결과값 찾는 함수
def get_result(X, combination):
    # combination에서 X보다 큰 수 나오면 그거 출력하고 종료
    for now in combination:
        if int(X) < int(now):
            return now
    return 0

# combination 구하기
for i in range(len(X)):
    # 사용한 인덱스 체크해주는 배열
    visited = [True] * len(X)
    # get_comb 실행
    get_comb(X, i, '', 1, visited)

# 에라 모르겠다 중복 겁나 많은거 set으로 없애주고 정렬해서 구하면 답은 나옴
combination = [*set(combination)]
combination.sort()

# 나중에 시간복잡도도 고려한 코드 보고 공부해보자

# 결과 출력
print(get_result(X, combination))
