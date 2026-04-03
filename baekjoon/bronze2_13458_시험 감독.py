import sys

N = int(sys.stdin.readline().strip())
a_list = list(map(int,sys.stdin.readline().split()))
B,C = map(int,sys.stdin.readline().split())
a_len = len(a_list)
count = 0
for i in range(a_len):
    now = a_list[i]
    if now <= B:
        count+=1
    else:
        now-=B
        if now%C==0:
            count+=(1+now//C)
        else:
            count+=2+now//C
    
print(count)


## 아침에 머리 리프레시 용으로 풀었는데 아침에 바보머리라 틀렸다.