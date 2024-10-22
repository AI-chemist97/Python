import sys
n=int(sys.stdin.readline())
for t in range(1,n+1):
    checklist=sys.stdin.readline().strip()
    lenc=len(checklist)
    cnt=0
    hap=0
    for i in range(lenc):
        if checklist[i]=="X":
            cnt=0
        else:
            cnt+=1
            hap+=cnt
    print(hap)