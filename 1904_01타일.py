import sys

N = int(sys.stdin.readline().strip())
if N==1:
    print(1)
elif N==2:
    print(2)
else:
    d = [0] *N

    d[0]=1
    d[1]=2
    for i in range(2,N):
        d[i]=(d[i-1]+d[i-2])%15746
    print(d[N-1])


# 15746s나눠서 저장하는걸 생각못함
# dp는 어떻게 나누는지가 중요한데 n-1,n-2 매번 잊음