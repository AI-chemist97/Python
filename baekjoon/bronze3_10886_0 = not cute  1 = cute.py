import sys

N = int(sys.stdin.readline().strip())
check = 0
for i in range(N):
    k = sys.stdin.readline().strip()
    if k == "1":
        check+=1
    else:
        check-=1
if check<0:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")

