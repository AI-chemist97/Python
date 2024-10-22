import sys
n=int(sys.stdin.readline())
stack=[]
for i in range(n):
    check = sys.stdin.readline().split()
    if len(check)==2:
        if check[0]=="push":
            stack+=[int(check[1])]
    else:
        if check[0]=="pop":
            if len(stack)==0:
                print(-1)
            else:
                print(stack.pop())
        elif check[0]=="size":
            print(len(stack))
        elif check[0]=="empty":
            if len(stack)==0:
                print(1)
            else:
                print(0)
        elif check[0]=="top":
            if len(stack)==0:
                print(-1)
            else:
                print(stack[-1])