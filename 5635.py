p=int(input())
lst=[]
for _ in range(p):
    n,d,m,y=input().split()
    lst.append([int(y),int(m),int(d),n])
lst.sort()
print(lst[-1][3])
print(lst[0][3])