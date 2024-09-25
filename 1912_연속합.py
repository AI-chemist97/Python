import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
# arr.reverse()
d=[0]*n
d[n-1]=arr[n-1]
for i in range(n-2,-1,-1):
    if d[i+1]>=0:
        d[i]=arr[i]+d[i+1]
    else:
        d[i]=arr[i]

print(max(d))