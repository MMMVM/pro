num=input()
num=int(num)
A=[]
for i in range(0,num):  
    m=input()
    A.append(m)
H=[]
for i in zip(*A):
    if i.count(i[0])==len(i): 
        H.append(i[0])
    else:
        break
print(''.join(H))
