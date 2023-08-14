def gcd(a,b):  # 최대공약수 구하기
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):      # 최소공배수 구하기
    result = (a*b) // gcd(a,b)
    return result

n=int(input())

for i in range(n):
    a,b=map(int, input().split())
    print(lcm(a,b))