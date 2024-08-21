import sys

def fib(n):
    global fibcnt
    global fibonaccicnt
    if n==1 or n==2:
        fibcnt+=1
        return 1
    # fibonaccicnt+=1
    fib(n-1)
    fib(n-2)
fibcnt=0
fibonaccicnt = 0
        


n= int(sys.stdin.readline())
fib(n)

print(fibcnt,n-2,(1-2**n-3)//(-1))
# 이렇게 짰었는데 시간초과가 나서 동적프로그래밍을 사용

import sys
def fib(n):
    f[1]=1
    f[2]=1
    for i in range(3,n+1):
       f[i]=f[i-1]+f[i-2]
    return f[n]


n= int(sys.stdin.readline())
f= [0]*(n+2)
        


print(fib(n),n-2)
