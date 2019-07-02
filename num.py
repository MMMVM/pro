from itertools import combinations
m,a=map(int,input().split())
s=len(str(m))
l=list(combinations(str(m),s-a))
l=(sorted(l))
y="".join(l[0])
print(y)
