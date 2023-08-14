n=int(input())
for j in range(n):
    a=list(input())
    count=0
    score=0
    for i in a:
        if i == 'O':
            count+=1
            score+=count
        elif i == 'X':
            count=0
    print(score)