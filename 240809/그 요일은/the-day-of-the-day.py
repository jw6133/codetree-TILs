ar = list(map(int, input().split()))
day = str(input())

thirty=[4,6,9,11]
cnt=0
daynum = {'Mon': 0, 'Tue': 1, 'Wed':2, 'Thu':3,'Fri':4,'Sat':5,'Sun':6}
for i in range(ar[0],ar[2]+1):
    if(i==2):
        cnt=cnt+29
    elif(i in thirty):
        cnt=cnt+30
    else:
        cnt=cnt+31

cnt=cnt-ar[1]

if(ar[2]==2):
    cnt=cnt-(29-ar[3])
elif(ar[2] in thirty):
    cnt=cnt-(30-ar[3])
else:
    cnt=cnt-(31-ar[3])
cnt = cnt-daynum[day]
print(cnt//7+1)