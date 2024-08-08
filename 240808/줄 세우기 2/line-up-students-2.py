def lining(copy,a):
    for j in range(a):
        if(j+1==a):
            break
        elif copy[j][0]==copy[j+1][0]:
            if(copy[j][1]<copy[j+1][1]):
                tempe=copy[j]
                copy[j]=copy[j+1]
                copy[j+1]=tempe
                if(j+1!=1):
                    lining(copy,a)

a=int(input())
base=[]

cnt=1

for i in range(a):
    ar = list(map(int, input().split()))
    base.append(ar)

copy=base

for i in copy:
    i.append(cnt)
    cnt=cnt+1
    
copy.sort()

lining(copy,a)

for h in copy:
    print(*h)