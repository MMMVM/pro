num=input()
num=int(num)
B=[]
for i in range(0,num):  
    m=input()
    B.append(m)
H=[]
for i in zip(*B):
    if i.count(i[0])==len(i): 
        H.append(i[0])
    else:
        break
print(''.join(H))
