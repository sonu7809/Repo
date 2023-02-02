# n=[7,5,3,8,4]
# for x in range(len(n)-1):
#     for j in range(len(n)-1-x):
#         if n[j]>n[j+1]:
#             n[j],n[j+1]=n[j+1],n[j]
# print(n)

l=[7,6,5,3,2,1]
for a in range(len(l)-1):
    s=a
    for b in range(a+1,len(l)):
        if l[s]>l[b]:
            s=b
            l[a],l[s]=l[s],l[a]
print(l)