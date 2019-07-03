x1=int(input())
y1=list(map(int,input().split()))
a1=0
for x in range(len(y1)-2):
    for y in range(x+1,len(y1)-1):
        for z in range(y+1,len(y1)):
            if y1[x]<y1[y]<y1[z] and x<y<z:
                a1=a1+1
print(a1)
