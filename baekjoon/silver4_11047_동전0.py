import sys

N,K = map(int, sys.stdin.readline().split())
money = []
for i in range(N):
    val = int(sys.stdin.readline().strip())
    if val<=K:
        money.append(val)
    else:
        pass
result=0
len_money = len(money)
check=K
for i in range(len_money-1,-1,-1):
    if check>=money[i]:
        a=check//money[i]
        b=check%money[i]
        if b == 0:
            result+=a
            break
        check = b
        result+=a
    else:
        pass
print(result)