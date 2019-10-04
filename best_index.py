import sys
n=int(input())
a=list(map(int,input().split()))
b=[]
ans=-sys.maxsize-1
b.append(0)
for i in range(1,n+1):
    b.append(b[i-1]+a[i-1])
for j in range(n):
    x=0
    sum1=0
    size=2*(n-j+1)
    while (x*(x+1))<=size:
        x=x+1
    ind=int((x*(x-1))/2+j-1)
    sum1=sum1+b[ind]-b[j-1]
    if(ans<sum1):
        ans=sum1
print(ans)
print (b)
