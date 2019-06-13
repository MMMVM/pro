m,n=input().split()
s=abs(len(m)-len(n))
for i in range(len(m)):
    if len(n)==1 and n[i] in m:
        break
    if m[i]!=n[i]:
        s=s+1
print(s)
