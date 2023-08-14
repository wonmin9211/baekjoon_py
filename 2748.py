a=int(input())
n=[]
n.append(0)
n.append(1)
for i in range(a-1):
    n.append(n[i]+n[i+1])
print(n[a])