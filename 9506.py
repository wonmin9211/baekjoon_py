while True:
    n=int(input())
    if n == -1:
        break
    a=[]
    sum=0
    for i in range(1,n):
        if n % i == 0:
            if n == i:
                continue
            a.append(i)
            sum += i
    if sum == n:
        print(n, '=', end=' ')
        for i in range(len(a)-1):
            print(a[i], '+', end=' ')
        print(a[len(a)-1])
    else:
        print(n, 'is NOT perfect.')
        