import sys

n= int(sys.stdin.readline())
if n==0:
    print(1)
else:
    cnt=1
    a=(n%10)*10+(n//10+n%10)%10
    while a!=n:
        cnt+=1
        a=(a%10)*10+(a//10+a%10)%10
    print(cnt)
