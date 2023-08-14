v=int(input())
a=list(input())
num_a, num_b=0,0
for i in a:
    if i == 'A':
        num_a+=1
    else:
        num_b+=1
if num_a == num_b:
    print('Tie')
elif num_a > num_b:
    print('A')
else:
    print('B')