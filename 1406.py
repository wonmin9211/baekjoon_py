import sys

s=list(sys.stdin.readline().rstrip())
s1=[]
for i in range(int(sys.stdin.readline())):

    command=list(sys.stdin.readline().rstrip().split())
    if command[0]=='L':
        if s:
            s1.append(s.pop())
    elif command[0]=='D':
        if s1:
            s.append(s1.pop())
    elif command[0]=='B':
        if s:
            s.pop()
    elif command[0]=='P':
        s.append(command[1])

print(''.join(s+list(reversed(s1))))