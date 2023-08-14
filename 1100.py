sum=0
chess=[[j for j in range(8)]for i in range(8)]
horse=[]

for i in range(8):
    for j in range(8):
        if i%2==0 and j%2==0:
            chess[i][j]=1
        elif i%2!=0 and j%2!=0:
            chess[i][j]=1
        else:
            chess[i][j]=0

for i in range(8):
    horse.append(input())

for i in range(8):
    for j in range(8):
        if horse[i][j]=='F' and chess[i][j]==1:
            sum+=1
print(sum)