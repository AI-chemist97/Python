

import sys


n = int(sys.stdin.readline())
gift = list(map(int,sys.stdin.readline().split()))
jido = [[] for _ in range(n+1)]
for tree in range(n):
    a,b=map(int,sys.stdin.readline().split())
    jido[a].append(b)
    jido[b].append(a)
print()
q=int(sys.stdin.readline().strip())
for que in range(q):
    x,y,z = map(int,sys.stdin.readline().split())
    gift[x-1]+=z
    gift[y-1]-=z
