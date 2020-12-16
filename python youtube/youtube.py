k=11
a=[1,2,3,4,7,8,10,11,13]
l=0
r=len(a)-1
if l<=r:
    mid=(l+r)//2
    if a[mid]==k:
        print(mid,end=" ") 
    elif a[mid]>k:
        r=mid-1
    else:
       l=mid+1
else:
    print("error")


def search(arr,l,r,x):
    if l<=r:
        mid=(l+r)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            search(arr,l,mid-1,x)
        else:
            search(arr,mid+1,r,x)
if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7]
    l=0
    r=len(arr)-1
    print(search(arr,l,r,4))
