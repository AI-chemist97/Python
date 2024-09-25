import sys

arr = list(map(int,sys.stdin.readline().split()))
if arr[0] ==0:
    print(0)
else:
    i = 1
    power=2
    memo = [arr[0]]
    while arr[i]!=0:
        if len(memo)==1:
            if arr[i] in memo:
                power+=1
            else:
                power+=2
                memo.append(arr[i])

        else:
            if arr[i] in memo:
                power+=1
            else:
                if arr[i]==4:
                    for k in range(2):
                        if memo[k]==1 or memo[k]==3:
                            power+=3
                            memo[k]=4
                            break
                    else:
                        power+=4
                        memo[0]=4
                elif arr[i]==1:
                    for k in range(2):
                        if memo[k]==2 or memo[k]==4:
                            power+=3
                            memo[k]=1
                            break
                    else:
                        power+=4
                        memo[0]=4
                else:
                    for k in range(2):
                        if memo[k]+1==arr[i] or memo[k]-1==arr[i]:
                            power+=3
                            memo[k]=arr[i]
                            break
                    else:
                        power+=4
                        memo[0]=arr[i]
            
        i+=1
    print(power)         
                
        # if arr[i] in memo:
