# 시간 초과로 고생한 문제 

import sys
# sys를 import하는 이유는 input 보다 속도가 빠르기 때문
M = int(sys.stdin.readline().strip())
# 숫자를 받으면 보통 정수형태가 아니라 문자열로 오기 때문에 계산에 이용할 수 없다. 때문에 int()를 사용하여 형변환을 해주고, 
# readline()을 통해 줄을 읽어오고 혹시 숫자외에 있을지 모르는 공백을 제거하기 위해 strip()을 해준다.
S = set()
# set은 {}으로 생긴 집합형태인데 {}이 빈 기호는 이미 dict가 차지하고 있어 빈 set는 set()로 표기한다.
for test in range(M):
    doit = sys.stdin.readline().split() # split()은 ()안에든 걸 기준으로 나눠준다. 빈칸은 스페이스바 기준으로 분리
    if len(doit)==2:
        do,num = doit[0],int(doit[1])
        if do == "add":
            S.add(num)
        elif do == "remove":
            # elif 는 else if 느낌
            S.discard(num)
        elif do == "check":
            print(1 if num in S else 0)
        elif do == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)
    else:
        if doit[0]=="all":
            S={i for i in range(1,21)}
        else:
            S=set()
