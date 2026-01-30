import sys

# 다이나믹프로그래밍이라는데 이거는 늘 헷갈린다 이기회에 정리하고 넘어가야지
N,K=list(map(int,sys.stdin.readline().split()))
# if N<1 or N>100:
#     print(N,"error")
#     quit()
# if K<0 or K>100000:
#     print(K,"error")
#     quit()

things = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
    # if W<1 or W>100000:
    #     print("error")
    #     quit()
    # if V<0 or V>1000:
    #     print(V,"error")
    #     quit()

dp=[0 for _ in range(K+1)]

for W, V in things:
    for heavy in range(K, W-1,-1):
        dp[heavy]=max(dp[heavy-W]+V,dp[heavy])
print(max(dp))

# 이해가 된것같지만 안된것같으니 당분간 dp를 풀어봐야겠음
# 아 나 이거 잘했는데 억울하다.


    # global cals_num


    # if cals_num<plus:
    #     cals_num=plus
    # for i in range(now,N):
    #     if weighthap+things[i][0]>K or i+1>=N:
    #         continue
    #     else:
    #         calc(weighthap+things[i][0],i+1,plus+things[i][1])

# calc(0,0,0)

# print(cals_num)