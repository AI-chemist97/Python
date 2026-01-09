import sys
T= int(sys.stdin.readline().strip())
for test in range(1,T+1):
    stud=list(map(int,sys.stdin.readline().split()))
    stud=stud[1:]
    # now=stud[0]
    cnt=0
    button=1
    while button!=20:
        button=1
        height=[stud[0]]    
        for i in range(1,20):
            if max(height)>stud[i]:
                cnt+=i
                height=[stud[i]]+height
            else:
                button+=1
                height.append(stud[i])
        stud=height[0:]
        
    print(test,cnt)