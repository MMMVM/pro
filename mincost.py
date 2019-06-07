m,a=input().split()
s=abs(len(m)-len(a))
for i in range(len(m)):
    if len(a)==1 and a[i] in m:
        break
    if m[i]!=a[i]:
        s=s+1
print(s)
