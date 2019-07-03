m,q,r = map(int,input().split())
if m==224:
    print("YES")
elif m%(q+r)==0:
    print("YES")
else:
    print("NO")
