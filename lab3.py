#lab3
p=0
k=1
i=1
x=0.1
while x**i/i>=0.01:
    p=p+k*(x**i/i)
    k=-k
    i+=1
print(p)
