ms=[]
n=int(input('How many people?'))
h=0
l=100
t=0
for i in range(n):
    s=int(input('score:'))
    if s < l:
        l = s
    elif s > h:
        h=s
    ms.append(s)
    t = t + s
a=t/n

print('average:',a)
print('high:',h)
print('low:',l)

    