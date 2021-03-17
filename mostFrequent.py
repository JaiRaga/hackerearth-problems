def freq(lis):
    l = set(lis)
    c = 0
    t = 0

    print('set', l)
    # print(lis)
    for i in l:
        # if c == 0:
        #     c = i
        #     t = lis.count(i)
        if t <= lis.count(i):
            c = i
            t = lis.count(i)
        print('l', i, 'count', lis.count(i))
    return c


if __name__ == "__main__":
    n = int(input().strip())
    lis = list(map(int, input().strip().split()))
    print(freq(lis))
