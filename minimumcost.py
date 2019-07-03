a,se=input().split()
ram=abs(len(a)-len(se))
for i in range(len(a)):
    if len(se)==1 and se[i] in a:
        break
    if a[i]!=se[i]:
        ram+=1
print(ram)
