n=4
mat=[1,1,1,1]
print(mat)
if len(mat)==0:
     print(-1)
else:
    i=0
    res=0
    n=4
    while i<len(mat):
        res+=2^n-i-1
        i+=1
print(res)
