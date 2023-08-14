n=int(input())
a=list(map(int, input().split()))
cnt=0
for i in a:
    isprime=True
    if i==1:
        isprime=False
    for j in range(2,i-1):
        if i%j==0:
            isprime=False
    if isprime==True:
        cnt+=1
print(cnt)