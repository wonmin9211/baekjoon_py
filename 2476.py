n=int(input())
p=[]
for i in range(n):
    a,b,c=map(int, input().split())
    if a==b==c:
        p.append(10000 + a*1000)
    elif a!=b and b!=c and a!=c:
        p.append(max(a,b,c) * 100)
    elif a==b and b!=c:
        p.append(1000 + a*100)
    elif a==c and a!=b:
        p.append(1000 + a*100)
    elif b==c and b!=a:
        p.append(1000 + b*100)

print(max(p))