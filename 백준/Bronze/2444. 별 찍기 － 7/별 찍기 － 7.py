import sys;
input = sys.stdin.readline
# 별 찍기

# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
N = int(input())

for i in range(N):
    star = '*' + '*' * (2 * i) + '\n'
    for j in range(N-1-i):
        print(' ', end='')
    print(star, end='')

for i in range(N-2, -1, -1):
    star = '*' + '*' * (2 * i) + '\n'
    for j in range(N-1-i):
        print(' ', end='')
    print(star, end='')