ms=[]
nm=[]
os=[]
n=int(input('How many people?'))
t=0
for i in range(n):
    s=int(input('score:'))
    ns=input('name:')
    ms.append(s)
    nm.append(ns)
def high (nm,ms,os):
    h=0
    for i in range(len(ms)):
        if ms[i]>h:
            h=ms[i]
            hn=nm[i]
    os.append(h)
    os.append(hn)
    return os
    
def low (nm,ms,os):         
    l=100
    for i in range(len(ms)):
       if ms[i]<l:
           l=ms[i]
           ln=nm[i]
    os.append(l)
    os.append(ln)
    return os
def average (t,ms):
    for i in range(len(ms)):
        t=t+ms[i]
    a=t/len(ms)
    return a
a = average(t,ms)
es = high(nm,ms,os)
es = low(nm,ms,os) 
print('average:',a)
print('high:',es[0],es[1])
print('low:',es[2],es[3])

    