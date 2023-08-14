n=int(input())
for i in range(n):
    p=int(input())
    players=dict()
    for j in range(p):
        c,name=input().split()
        players[int(c)]=name
    print(players.get(max(players.keys())))