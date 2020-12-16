nums=[2,5,6,8,1,2]
l=0
r=len(nums)
c=[]
mid=(l+(r-l))//2
a=nums[:mid]
b=nums[mid:]
print(a)
print(b)
for i in range(mid):
    c+=[a[i],b[i]]
    print(c)
