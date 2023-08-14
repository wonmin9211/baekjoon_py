a,b=map(int, input().split())
for i in range(min(a,b),0,-1):  # 최대공약수
    if a%i==0 and b%i==0:
        print(i)
        break
print(int(a*b/i))  # 두수 곱한값에 최대공약수를 나눈값 -> 최소공배수