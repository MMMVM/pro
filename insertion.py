#insertion and deletion
aaa,j2=map(str,input().split())
vj=0
if len(aaa)>len(j2):
  aaa,j2=j2,aaa
i=0
while i<len(aaa):
  vj+=(ord(j2[i])-ord(aaa[i]))
  i+=1
for i in range(i,len(j2)):
  vj+=ord(j2[i])-ord('a')+1
print(vj)
