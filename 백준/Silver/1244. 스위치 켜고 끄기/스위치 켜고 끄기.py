# 스위치 끄고 켜기

# 스위치는 1, 0으로 이루어져 있음
# 남학생, 여학생에게 각각 1 ~ N의 숫자를 줌
# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
# 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

# 입력으로 스위치들의 처음 상태가 주어지고, 각 학생의 성별과 받은 수가 주어진다.
# 학생들은 입력되는 순서대로 자기의 성별과 받은 수에 따라 스위치의 상태를 바꾸었을 때, 스위치들의 마지막 상태를 출력하는 프로그램을 작성하시오.

# [입력]
# 첫째 줄에는 스위치 개수가 주어진다.(100 이하인 양의 정수)
# 둘째 줄에는 각 스위치의 상태가 주어진다.
# 셋째 줄에는 학생수가 주어진다.(100 이하인 양의 정수)
# 넷째 줄부터 마지막 줄까지 한 줄에 한 학생의 성별, 학생이 받은 수가 주어진다.
# 남학생은 1로, 여학생은 2로 표시하고, 학생이 받은 수는 스위치 개수 이하인 양의 정수이다

# [출력]
# 스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다. 
# 예를 들어 21번 스위치가 있다면 이 스위치의 상태는 둘째 줄 맨 앞에 출력한다.
# 켜진 스위치는 1, 꺼진 스위치는 0으로 표시하고, 스위치 상태 사이에 빈칸을 하나씩 둔다.

# [문제 풀이]
# 남자(1)는 현재 숫자의 배수 인덱스들의 값을 전부 교체해주기
# 여자(2)는 현재 숫자의 인덱스에서 while문 실행해서 양 옆에 값 비교 후, 같으면 값을 바꿔주고 다음으로 이동하면서 서로 다른 수가 나올때 까지 반복하기
# 결과는 20개씩 끊어서 한 줄씩 출력하기


# 남자 스위치 전환
def male_switch(start):
    queue = [start]

    while queue:
        # 현재 인덱스 뽑기
        now = queue.pop(0)
        # 스위치 끄기, 켜기(인덱스라 -1)
        switch[now - 1] = abs(switch[now - 1] - 1)
        # 다음 배수가 N을 넘지 않으면 queue에 추가해주기
        if now + start <= N:
            queue.append(now + start)

    

# 여자 스위치 전환
def female_switch(start):
    queue = [start]

    while queue:
        # 왼쪽 좌표, 오른쪽 좌표 뽑기
        left, right = queue.pop(0)
        # 왼쪽, 오른쪽 좌표 벗어나지 않았는지 검증 후 서로 같은 값인지 검증
        if left - 1 >= 0 and right - 1 < N and switch[left - 1] == switch[right - 1]:
            # 검증되면 스위치 변환
            switch[left - 1] = abs(switch[left - 1] - 1)
            switch[right - 1] = abs(switch[right - 1] - 1)
            # 다음 스위치 이동
            queue.append([left - 1, right + 1])

# 스위치 갯수
N = int(input())

switch = list(map(int, input().split()))

# 학생 수
M = int(input())

# 학생 수 만큼 반복문 진행
for _ in range(M):
    gender, idx = map(int, input().split())

    # 남학생이면
    if gender == 1:
        # 남자 스위치 전환
        male_switch(idx)
    # 여학생이면
    elif gender == 2:
        # 시작점 변환
        switch[idx - 1] = abs(switch[idx - 1] - 1)
        # 여자 스위치 전환
        female_switch([idx - 1, idx + 1])
    
# 결과 출력(10개씩 잘라서 출력)

cnt = 0
while cnt < N:
    # 마지막 인덱스일때
    if cnt == N - 1:
        print(switch[cnt])
    # 10번째 인덱스일때
    elif cnt % 10 == 9:
        print(switch[cnt])
    # 그 외
    else:
        print(switch[cnt], end=' ')
    cnt += 1


# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
# 20, 21, 22, 23, 24, 25, 26, 27, 28, 29