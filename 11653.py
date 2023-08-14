N = int(input())

cnt = 0

if N != 1:
    for i in range(2, N):
        while N % i == 0:
            print(i)
            N /= i
            cnt += 1
        i+=1
    if cnt == 0:
        print(N)
