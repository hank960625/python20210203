ms=[]
nm=[]
n=int(input('How many people?'))
h=0
l=100
t=0
for i in range(n):
    s=int(input('score:'))
    ns=input('name:')
    ms.append(s)
    nm.append(ns)
    t = t + s
for i in range(n):
    if ms[i]>h:
        h=ms[i]
        hn=nm[i]
    for i in range(n):
        if ms[i]<l:
            l=ms[i]
            ln=nm[i]
a=t/n
print('average:',a)
print('high:',h,hn)
print('low:',l,ln)

    