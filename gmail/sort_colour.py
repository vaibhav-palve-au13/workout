arr=[1,0,2,1,2,0]
i=0
cnt=0
while i<len(arr) and cnt<len(arr):
    if arr[i]==0:
        del arr[i]
        arr.insert(0,0)
    elif arr[i]==2:
        del arr[i]
        i-=1
        arr.append(2)
    i+=1
    cnt+=1
print(arr)