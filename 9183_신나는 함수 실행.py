import sys

def w(a,b,c):
    global dp
    if a<= 0 or b <= 0 or c<=0:
        dp[0][0][0]
        return 1
    elif a>20 or b>20 or c>20:
        return dp[20][20][20]
    elif a<b and b<c:
        dp[a][b][c]=dp[a][b][c-1]+dp[a][b-1][c-1]-dp[a][b-1][c]
        return dp[a][b][c]
    else:
        global button
        if a==-1 and b==-1 and c==-1:
            button=1
            return
        
        dp[a][b][c]=dp[a-1][b][c]+dp[a-1][b-1][c]+dp[a-1][b][c-1]-dp[a-1][b-1][c-1]
        return dp[a][b][c]

button=0
dp=[[[1]*21 for _ in range(21)] for _ in range(21)]
for i in range(1,21):
    for j in range(1,21):
        for k in range(1,21):
            if i<j and j<k:
                dp[i][j][k]=dp[i][j][k-1]+dp[i][j-1][k-1]-dp[i][j-1][k]
            else:
                dp[i][j][k]=dp[i-1][j][k]+dp[i-1][j-1][k]+dp[i-1][j][k-1]-dp[i-1][j-1][k-1]
            
# print(dp)
while button==0:
    a,b,c=list(map(int,sys.stdin.readline().split()))

    if a==-1 and b==-1 and c==-1:
        break
    elif a<=0 or b<=0 or c<=0:
        print(f'w({a}, {b}, {c}) = 1')
    elif a>20 or b>20 or c>20:
        print(f'w({a}, {b}, {c}) = {w(20,20,20)}')
    else:
        print(f'w({a}, {b}, {c}) = {dp[a][b][c]}')
    