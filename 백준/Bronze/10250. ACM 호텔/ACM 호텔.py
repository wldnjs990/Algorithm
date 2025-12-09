T = int(input())

for i in range(T) :
    H, W, N = map(int, input().split())
    Hcount = 0
    Wcount = 0
    for n in range(N) :
        if n == 0 :
            Hcount = 1
            Wcount = 1
        elif Hcount < H :
            Hcount = Hcount + 1
        else :
            Hcount = 1
            if Wcount < W :
                Wcount = Wcount + 1
    h = str(Hcount)
    if len(str(Wcount)) <= 1 :
        w = '0' + str(Wcount)
    else :
        w = str(Wcount)
    print(h + w)
