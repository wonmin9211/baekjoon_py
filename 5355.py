n = int(input())
for _ in range(n):
    c = list(map(str, input().split()))
    r = float(c[(-1)*len(c)])
    for i in range(1, len(c)):
        if c[i] == '@':
            r *= 3
        elif c[i] == '%':
            r += 5
        elif c[i] == '#':
            r -= 7
    print('%0.2f'%r)