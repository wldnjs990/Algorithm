import sys;
input = sys.stdin.readline
# 홀수 홀릭 호석

# 호석이는 짝수랑 홀수 중에서 이니셜이 같은 홀수를 더 좋아한다. 운전을 하던 호석이는 앞차의 번호판이 홀수로 가득할 때 사랑스러움을 느낄 정도이다. 
# 전화번호도 홀수만 있고 싶다. 
# 그렇게 홀수 홀릭에 빠진 호석이는 가지고 있는 수 N을 일련의 연산을 거치면서, 등장하는 숫자들에서 홀수를 최대한 많이 많이 보고 싶다.

# 하나의 수가 주어졌을 때 호석이는 한 번의 연산에서 다음과 같은 순서를 거친다.

# 수의 각 자리 숫자 중에서 홀수의 개수를 종이에 적는다.
# 수가 한 자리이면 더 이상 아무것도 하지 못하고 종료한다.
# 수가 두 자리이면 2개로 나눠서 합을 구하여 새로운 수로 생각한다.
# 수가 세 자리 이상이면 임의의 위치에서 끊어서 3개의 수로 분할하고, 3개를 더한 값을 새로운 수로 생각한다.

# 호석이는 연산이 종료된 순간에 종이에 적힌 수들을 모두 더한다. 그렇게 최종적으로 얻은 수를 최종값이라고 하자. 
# 예를 들어, 시작하는 수가 82019 라고 하자. 
# 그럼 아래와 같이 나누게 되면 5개의 홀수를 볼 수 있기 때문에, 최종값이 5가 된다.

# 시작할 때 호석이가 가진 수를 N 이라고 했을 때, 만들 수 있는 최종값 중 최솟값과 최댓값을 구해주자.

# [입력]
# 첫번째 줄에 호석이가 처음 시작할 때 가지고 있는 수 N 이 주어진다.

# [출력]
# 첫 번째 줄에 호석이가 만들 수 있는 최종값 중에서 최솟값과 최댓값을 순서대로 공백으로 구분하여 출력한다.

# [제한]
# 1 ≤ N ≤ 10^9-1, N 은 자연수이다.

# [문제 풀이]
# 3개 이상의 수는 임의의 숫자 3개로 나눈다는게 진짜 개오반데
# N도 10^9면 경우의 수가 도대체 얼마나 나오는거야
# 일단 그냥 해보자

# 1. 홀수 세기
# 현재 숫자를 문자열로 변환하고 반복문 실행해서 홀수 찾으면 결과에 +1 해주기
# 2. 숫자 분할하기
# 1자리 숫자면 패스, 두 자라 숫자면 중간 잘라줘서 더해주기, 3자리 이상이면 모든 3번 자르는 케이스를 실행시켜주기
# BFS 느낌으로 큐에 담아서 해보자 일단

# 왜 빠르지..?

from collections import deque

def BFS(start):
  global max_c
  global min_c
  deq = deque()
  deq.append(start)

  while deq:
    now_num, cnt = deq.popleft()
    # 홀수 숫자 cnt에 더해주기
    now_num = str(now_num)
    for num in now_num:
      # 홀수 더해주기
      if int(num) % 2 == 1:
        cnt += 1
    # 숫자 분할해서 더하고 다음으로 이동
    # 1이면 종료하고 카운트 최소, 최대 검사 후 업데이트 해주기
    if len(now_num) == 1:
      # 첫 번째 교체라면 최소, 최대 둘 다 변경
      if max_c == -1:
        max_c = cnt
        min_c = cnt
      elif max_c < cnt:
        # 업데이트될 최대값이 최소값이 되는 경우 교체
        if min_c > max_c :
          min_c = max_c
        # 최대값 업데이트
        max_c = cnt
      elif min_c > cnt:
        min_c = cnt

      
    # 2일 경우 2개로 나눠서 더한 후 deq에 담기
    elif len(now_num) == 2:
      next_num = int(now_num[0]) + int(now_num[1])
      deq.append([next_num, cnt])
    # 3 이상일 경우 모든 3등분 합들을 배열에 담아주기(이게 맞나...)
    elif len(now_num) >= 3:
      for i in range(len(now_num) - 2):
        st = int(now_num[0 : i+1])
        for j in range(i+1, len(now_num) - 1):
          nd = int(now_num[i+1 : j+1])
          rd = int(now_num[j+1 : len(now_num)])
          deq.append([st + nd + rd, cnt])


start_num = int(input())
max_c = -1
min_c = -1

BFS([start_num, 0])

print(min_c, max_c)