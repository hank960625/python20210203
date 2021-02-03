ms=[]
n=int(input('How many people?'))
h=0
l=100
t=0
for i in range(n):
    s=int(input('score:'))
    ms.append(s)
    t = t + s
    s=input('name:')
    ms.append(s)
    
   
for i in range(0,n*2,2):
    if ms[i]>h:
        h=ms[i]
        hn=ms[i+1]
for i in range(0,n*2,2):
        if ms[i] < l:
            l=ms[i]
            ln=ms[i+1]
a=t/n
print(ms)
print('average:',a)
print('high:',h,hn)
print('low:',l,ln)

    