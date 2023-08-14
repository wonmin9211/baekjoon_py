T = int(input())
for i in range(T):
    r, s = input().split()
    for j in s:
        print(int(r) * j, end='')
    print()