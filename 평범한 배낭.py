n,k=map(int, input().split()) # n=물건 갯수, k=버틸수 있는 무게
a=[]
for i in range(n):
    w,v=map(int, input().split()) # w=물건 무게, v=물건의 가치
    a.append(w)
    for j in range(len(a)):
        