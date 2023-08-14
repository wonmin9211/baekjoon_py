m=int(input())
n=int(input())
s=[]
i=1
while i**2 <= n:
    if m <= i**2 <= n:
        s.append(i**2)
    i+=1
if s==[]:
    print(-1)
else:
    print(sum(s))
    print(min(s))