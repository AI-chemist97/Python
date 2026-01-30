import sys

C = int(sys.stdin.readline().strip())
for i in range(C):
    score = list(map(int,sys.stdin.readline().split()))
    N=score[0]
    score=score[1:]
    avg = sum(score)/N
    check=0
    for j in score:
        if j>avg:
            check+=1
    
    print(f"{round(100*check/N,3)}%")