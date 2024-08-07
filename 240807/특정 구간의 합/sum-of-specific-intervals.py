a,b=map(int,input().split(" "))
ar = list(map(int, input().split()))
index =[]
for i in range(b):
    row = list(map(int, input().split()))
    index.append(row)

for i in index:
    cnt=0
    for j in range(i[0],i[1]+1):
        cnt+=ar[j-1]
    print(cnt)