def bfs():
    cnt=1
    i=0
    j=0

    checklist[i][j]=cnt
    queue = [[i,j]]
    while queue:
        i,j=queue.pop(0)
        cnt = checklist[i][j]
        # print(cnt)
        for r in range(4):
            nx=dx[r]+i
            ny=dy[r]+j
            # for l in range(n):
            #     print(checklist[l])
            if 0<=nx<n and 0<=ny<m:
                if miro[nx][ny]=="1" and checklist[nx][ny]>cnt+1:
                    i=nx
                    j=ny
                    checklist[i][j]=cnt+1
                    queue.append([i,j])

                     
import sys
    

n,m=map(int,sys.stdin.readline().split())
checklist=[[n*m]*m for _ in range(n)]
miro=[]
for i in range(n):
    miro.append(list(sys.stdin.readline().strip()))
dx=[1,-1,0,0]
dy=[0,0,1,-1]
bfs()
for i in range(n):
    print(checklist[i])
print(checklist[n-1][m-1])