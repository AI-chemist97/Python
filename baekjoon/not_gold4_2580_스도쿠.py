import sys



# for i in range(9):
perf = [1,2,3,4,5,6,7,8,9]
str_perf = [i for i in perf]
set_perf = set(str_perf)
memo_zero=[]
sdk_list = []
garo_dict = {}
sero_dict = {}
nemo_dict = {}
for i in range(9):
    sdk = list(map(int,sys.stdin.readline().split()))
    sdk_count = sdk.count(0)
    if sdk_count==0:
        continue
    elif sdk_count == 1:
        zero_index = sdk.index(0)
        set_sdk = set(sdk)
        val = set_perf - set_sdk

        sdk[zero_index] = list(val)[0]
        sdk_list.append(sdk)
        # continue

    else:
        for j in range(9):
            if sdk[j]==0:
                memo_zero.append((i,j))
                set_sdk = set(sdk)
                val = set_perf - set_sdk
                sero_dict[i][[].append(j)]=list(val)



for j in range(9):    
    sdk = []
    for i in range(9):    
        sdk.append(sdk_list[i][j])
    sdk_count = sdk.count(0)
    if sdk_count==0:
        continue
    elif sdk_count==1:
        zero_index = sdk.index(0)
        set_sdk = set(sdk)
        val = set_perf - set_sdk

        sdk_list[zero_index][j] = list(val)[0]           
        continue
    elif sdk.count(0)>1:
        for k in range(9):
            if sdk[k]==0:
                memo_zero.append((k,j))
                set_sdk = set(sdk)
                val = set_perf - set_sdk
                
                garo_dict[k][[].append(j)]=list(val)

for gob in range(0,7,3):
    for i in range(0+gob,3+gob):
        for hab in range(0,7,3):
            for j in range(0+hab,3+hab):
                     
    sdk = []
    for i in range(9):    
        sdk.append(sdk_list[i][j])
    sdk_count = sdk.count(0)
    if sdk_count==0:
        continue
    elif sdk_count==1:
        zero_index = sdk.index(0)
        set_sdk = set(sdk)
        val = set_perf - set_sdk

        sdk_list[zero_index][j] = list(val)[0]           
        continue
    elif sdk.count(0)>1:
        for k in range(9):
            if sdk[k]==0:
                memo_zero.append((k,j))
                set_sdk = set(sdk)
                val = set_perf - set_sdk
                
                garo_dict[k][[].append(j)]=list(val)




def dfs(fltmxm,n):
    if n==-1:
        return
    sdk_list[fltmxm[0]][fltmxm[1]]
    




#     sdk_list.append(sdk)
# k=len(memo_zero)
# round=0



target = memo_zero[0]
a=target[0]
b=target[1]
button=0
while round!=k:
    if sdk_list[a][b]!="0":
        round+=1
        if button==k:
            break
        target = memo_zero[round%k]



    # sero = []
    a = target[0]
    b = target[1]
    inst=[]
    for i in range(9):
        inst.append(sdk_list[i][b])
    
    if inst.count("0") == 1:
        zero_index = inst.index("0")
        set_inst = set(inst)
        val = set_perf - set_inst

        # inst[zero_index] = list(val)[0]
        sdk_list[a][b]=list(val)[0]
        button+=1
    else:
        pass
    # sero.append(inst)    

    if sdk_list[a][b]=="0":
        check = (a//3)*3
        inst=[]
        for i in range(check,check+3):
            cc= (b//3)*3
            for j in range(cc,cc+3):
                inst.append(sdk_list[i][j])
        if inst.count("0") == 1:

            # zero_index = inst.index("0")
            set_inst = set(inst)
            val = set_perf - set_inst

            sdk_list[a][b] = list(val)[0] 
            button+=1
        else:
            pass   
    else:
        continue  

    if sdk_list[a][b]=="0":
        inst = []
        for j in range(9):
            inst.append(sdk_list[a][j])
        if inst.count("0") == 1:

            # zero_index = inst.index("0")
            set_inst = set(inst)
            val = set_perf - set_inst

            sdk_list[a][b] = list(val)[0] 
            button+=1
        else:
            pass   
    else:
        continue  
last = []      
for i in range(k):
    if sdk_list[memo_zero[i][0]][memo_zero[i][1]]=="0":
        last.append(memo_zero[i])

    

for i in sdk_list:   
    print(*i)