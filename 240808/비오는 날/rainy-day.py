a=int(input())
wlist=[]
for i in range(a):
    a=list(map(str,input().split(" ")))
    wlist.append(a)

for i in wlist:
    if(i[2]=="Rain"):
        print(*i)
        break