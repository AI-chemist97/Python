import sys
check=[0]*10
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())
result=str(a*b*c)
for i in range(len(result)):
    check[int(result[i])]+=1
for i in range(10):
    print(check[i])