ms=[]
n=int(input('How many people?'))
t=0
a=0
h=0
l=100
for i in range(n):
    s=int(input('score:'))
    ns=input('name:')
    op=[]
    op.append(s)
    op.append(ns)
    ms.append(op)
for i in ms:
    t = t+i[0]
a=t/n
for i in ms:
    if i[0]>h:
        h=i[0]
        hn=i[1]
    for i in ms:
        if i[0]<l:
            l=i[0]
            ln=i[1]
a=t/n
print('average:',a)
print('high:',h,hn)
print('low:',l,ln)

    