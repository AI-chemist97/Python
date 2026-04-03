import sys

S = int(sys.stdin.readline().strip())
k = 1
count = 0
l = 0
while True:
    l+=1
    if count + k == S:
        break
    elif count +k +k+1>S:
        l-=1
        k+=1
    else:
        count+=k
        k+=1
print(l)