n=int(input())
if n<5 and n%3!=0:
    print(-1)
else:
    if n%5==0:
        print(n//5)
    elif n%5==4:
        t=n-9
        t=t//5
        print(t+3)
    elif n%5==3:
        t=n-3
        t=t//5
        print(t+1)
    elif n>12 and n%5==2:
        t=n-12
        t=t//5
        print(t+4)
    elif n%5==1:
        t=n-6
        t=t//5
        print(t+2)
    elif n%3==0:
        t=n//3
        print(t)
    else:
        print(-1)