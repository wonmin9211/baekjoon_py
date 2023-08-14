n=int(input())
m=int(input())
cnt=0
A=[]
for i in range(n,m+1):
    isprime=True
    if i==1:
        isprime=False
    for j in range(2,i):
        if i%j==0:
            isprime=False
    if isprime==True:
        cnt+=i
        A.append(i)
if cnt==0:
    print(-1)
else:
    print(cnt)
    print(min(A))