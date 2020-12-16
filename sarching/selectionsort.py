a=[5,6,2,3,4,1]

for i in range(len(a)):
    min_idx=i
    for j in range(i+1,len(a)):
        if a[min_idx]>a[j]:
            min_idx=j
        a[i],a[min_idx]= a[min_idx],a[i]
for i in range(len(a)-1):
    print(a[i],end=" ")
print()


