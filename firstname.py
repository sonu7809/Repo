a=['munu','sonu','somu','manu','kartik','sohail']
b={}
for i in a:
    if i[0] not in b:
        b[i[0]]=1
    else:
        b[i[0]] += 1
print(b)