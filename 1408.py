H,M,S=map(int, input().split(':'))
h,m,s=map(int, input().split(':'))

# hour, minute, second
if H < h:
    hour = h-H
    if m < M:
        minute = m+60-M
        hour-=1
    else:
        minute = m-M
    if s < S:
        second = s+60-S
        minute-=1
    else:
        second = s-S
else:
    hour = 24-(H-h)
    if m < M:
        minute=m+60-M
        hour-=1
    else:
        minute=m-M
    if s < S:
        second=s+60-S
        minute-=1
    else:
        second=s-S
if second < 0:
    second += 60
    minute -= 1
if minute < 0:
    minute += 60
    hour -= 1
if hour < 0:
    hour += 24
if second == 60:
    second -=60
    minute+=1
if minute == 60:
    minute-=60
    hour+=1
if hour==24:
    hour-=24
    
print('%02d:%02d:%02d' %(hour, minute, second))