a=int(input())

ar = list(map(int, input().split()))

result = []

for i in range(a):
    if((i+1)%2==1):
        slic=ar[:i+1]
        slic.sort()
        n=slic[len(slic)//2]
        result.append(n)

print(*result)