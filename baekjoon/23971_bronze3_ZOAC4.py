import sys

H,W,N,M = map(int,sys.stdin.readline().split())
i = H//(N+1)
if H-i*(1+N)>=1:
    i+=1

j= W//(M+1)

if W-j*(1+M)>=1:
    j+=1
print(i*j)