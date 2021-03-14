def processes(c, i):
    t = 0
    temp = None
    while True:
        if len(c) == 0:
            break
        if c[0] == i[0]:
            t += 1
            c.pop(0)
            i.pop(0)
        else:
            temp = c.pop(0)
            c.append(temp)
            t += 1
    return t


if __name__ == "__main__":
    N = input().strip()
    c = list(map(int, input().strip().split()))
    i = list(map(int, input().strip().split()))
    print(processes(c, i))
