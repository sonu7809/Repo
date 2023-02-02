num=28
sum=0
for i in range(1,(num//2)+1):
    rem=num%i
    if rem ==0:
        sum=sum+i

if sum==num:
    print('perfect')
else:
    print('not perfect')
