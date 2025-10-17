import sys;
input = sys.stdin.read

inp = input()

arr = []

for a in inp:
    if a != ' ' and a != '\n':
        arr.append(int(a))

arr_len = len(arr) // 2

for i in range(arr_len):
    st = i*2
    nd = i*2+1
    print(arr[st] + arr[nd])

