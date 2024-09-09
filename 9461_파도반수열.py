import sys

T = int(sys.stdin.readline().strip())
for test in range(T):
    n = int(sys.stdin.readline().strip())
    d = [0] * n 
    if n==1:
        print(1)
    elif n==2:
        print(1)
    elif n==3:
        print(1)
    else:
        d[0]=1
        d[1]=1
        d[2]=1
        for i in range(3,n):
            d[i]=d[i-2]+d[i-3]
        print(d[n-1])